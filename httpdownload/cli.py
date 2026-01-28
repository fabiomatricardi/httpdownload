# httpdownload/cli.py
import warnings
warnings.filterwarnings(action="ignore")

import sys
import os
from urllib.parse import urlparse
import requests
from rich.progress import (
    Progress,
    BarColumn,
    TimeRemainingColumn,
    DownloadColumn,
    TextColumn,
    TransferSpeedColumn,
)


def normalize_github_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc == "github.com" and "/blob/" in parsed.path:
        new_path = parsed.path.replace("/blob/", "/raw/", 1)
        return parsed._replace(path=new_path).geturl()
    return url


def get_filename_from_url(url: str) -> str:
    parsed = urlparse(url)
    name = os.path.basename(parsed.path)
    return name or "downloaded_file"


def download_with_progress(url: str, dest_path: str) -> None:
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total = int(response.headers.get("content-length", 0))
        chunk_size = 8192

        progress = Progress(
            TextColumn("[bold blue]Downloading"),
            TextColumn("{task.fields[filename]}"),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        )

        with progress:
            task_id = progress.add_task(
                "download",
                total=total if total > 0 else None,
                filename=os.path.basename(dest_path),
            )

            with open(dest_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if not chunk:
                        continue
                    f.write(chunk)
                    progress.update(task_id, advance=len(chunk))


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: httpdownload <URL>")
        sys.exit(1)

    url = normalize_github_url(sys.argv[1])
    filename = get_filename_from_url(url)
    dest_path = os.path.join(os.getcwd(), filename)

    try:
        download_with_progress(url, dest_path)
        print(f"\nFile '{filename}' downloaded successfully to '{dest_path}'.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download file: {e}")
        sys.exit(1)
