"""Convert between local HTTrack mirror paths and original URLs (spec §4.2)."""
from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse


def mirror_path_to_url(file_path: str) -> str:
    """Convert a local mirror path back to its original URL.

    /mirrors/supplier_name/www.supplier.ir/catalog/page.html
      -> https://www.supplier.ir/catalog/page.html
    """
    path = Path(file_path)
    parts = list(path.parts)
    try:
        mirror_idx = parts.index("mirrors")
    except ValueError:
        return str(file_path)
    if mirror_idx + 2 >= len(parts):
        return str(file_path)
    domain = parts[mirror_idx + 2]          # skip project_name
    rest = "/".join(parts[mirror_idx + 3:])
    return f"https://{domain}/{rest}"


def url_to_mirror_path(url: str, output_dir: str) -> Path:
    """Convert a URL to the local path matching HTTrack's directory convention."""
    parsed = urlparse(url)
    host = parsed.netloc
    path = parsed.path.strip("/")
    if not path or path.endswith("/"):
        path = path + "index.html"
    elif "." not in path.split("/")[-1]:
        path = path + "/index.html"
    return Path(output_dir) / host / path


def extract_domain_from_mirror(file_path: str) -> str | None:
    parts = list(Path(file_path).parts)
    if "mirrors" in parts:
        idx = parts.index("mirrors")
        if idx + 2 < len(parts):
            return parts[idx + 2]
    return None
