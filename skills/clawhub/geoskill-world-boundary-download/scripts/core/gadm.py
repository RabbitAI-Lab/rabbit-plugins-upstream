"""GADM 4.1 data source client.

GADM 4.1 distributes one zip per country that contains the Shapefile
sets for every available level (0..5). The download URL pattern is::

    https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_{ISO3}_shp.zip

Inside the zip, each level has its own .shp/.shx/.dbf/.prj set named
``gadm41_{ISO3}_{level}.shp``.

GADM 4.1 license: free for non-commercial use; commercial use requires
a separate license. Callers that want GADM must explicitly select
``--source gadm`` and the ``GadmSource`` wrapper prints a one-time
license reminder.
"""

from __future__ import annotations

import shutil
import tempfile
import time
import zipfile
from pathlib import Path
from typing import Optional

import requests

from .cache import HttpCache
from .exceptions import DataSourceError, LicenseError, NetworkError

GADM_BASE = "https://geodata.ucdavis.edu/gadm/gadm4.1/shp/"
GADM_GPKG_BASE = "https://geodata.ucdavis.edu/gadm/gadm4.1/gpkg/"

RETRYABLE_STATUS = {429, 500, 502, 503, 504}
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_S = 1.5

GADM_LICENSE_NOTICE = (
    "GADM data are free for academic and non-commercial use. "
    "Commercial use requires a separate license from https://gadm.org/license.html. "
    "By selecting --source gadm you confirm your use case is permitted."
)


def build_country_shp_url(iso3: str) -> str:
    """URL of the GADM 4.1 SHP zip for a whole country (all levels)."""

    return f"{GADM_BASE}gadm41_{iso3.upper()}_shp.zip"


def build_country_gpkg_url(iso3: str) -> str:
    """URL of the GADM 4.1 single-file GeoPackage for a country (all levels)."""

    return f"{GADM_GPKG_BASE}gadm41_{iso3.upper()}.gpkg"


def _download(url: str, cache: Optional[HttpCache], timeout: float) -> Path:
    if cache is not None:
        cached = cache.get_path(url)
        if cached is not None:
            return cached

    last_err: Optional[Exception] = None
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            r = requests.get(url, timeout=timeout, stream=True)
        except requests.RequestException as e:
            last_err = e
            if attempt >= RETRY_ATTEMPTS:
                raise NetworkError(f"GET {url} failed: {e}") from e
            time.sleep(RETRY_BACKOFF_S * attempt)
            continue

        if r.status_code in RETRYABLE_STATUS:
            last_err = DataSourceError(
                f"GET {url} returned {r.status_code}", source="gadm"
            )
            if attempt >= RETRY_ATTEMPTS:
                raise last_err
            time.sleep(RETRY_BACKOFF_S * attempt)
            continue

        if r.status_code == 404:
            raise DataSourceError(
                f"GADM has no data for {url} (404)", source="gadm"
            )
        if not r.ok:
            raise DataSourceError(
                f"GET {url} returned {r.status_code}: {r.text[:200]}",
                source="gadm",
            )

        data = r.content
        if cache is not None:
            return cache.put(
                url,
                data,
                etag=r.headers.get("ETag"),
                content_type=r.headers.get("Content-Type"),
            )
        fd, name = tempfile.mkstemp(prefix="gadm-", suffix=".zip")
        with open(fd, "wb") as f:
            f.write(data)
        return Path(name)

    raise NetworkError(f"GET {url} failed after retries: {last_err}")


def _extract_level(zip_path: Path, iso3: str, level: int, target_dir: Path) -> Path:
    """Extract the SHP set for one level out of the country zip."""

    target_dir.mkdir(parents=True, exist_ok=True)
    iso = iso3.upper()
    base = f"gadm41_{iso}_{level}"
    # If the level's shp is already there, skip.
    expected = target_dir / (base + ".shp")
    if expected.exists():
        return target_dir

    suffixes = (".shp", ".shx", ".dbf", ".prj", ".cpg")
    with zipfile.ZipFile(zip_path) as zf:
        # Some archives nest under a sub-folder; tolerate both.
        names = zf.namelist()
        for name in names:
            if name.endswith("/"):
                continue
            stem = Path(name).name
            if not stem.startswith(base):
                continue
            if not any(stem.lower().endswith(s) for s in suffixes):
                continue
            with zf.open(name) as src, open(target_dir / stem, "wb") as dst:
                shutil.copyfileobj(src, dst)
    if not expected.exists():
        raise DataSourceError(
            f"GADM zip did not contain {base}.shp; country may not have this level",
            source="gadm",
            iso=iso3,
            level=f"ADM{level}",
        )
    return target_dir


def download_country_shp(
    iso3: str,
    level: int,
    *,
    cache: Optional[HttpCache] = None,
    timeout: float = 300.0,
) -> Path:
    """Download the country zip (cached), extract one level, return its dir."""

    if not 0 <= level <= 5:
        raise DataSourceError(
            f"GADM levels are 0..5; got {level}", source="gadm", iso=iso3, level=str(level)
        )

    url = build_country_shp_url(iso3)
    zip_path = _download(url, cache=cache, timeout=timeout)

    base_root = (cache.root / "gadm" / iso3.upper()) if cache is not None else Path(tempfile.mkdtemp(prefix=f"gadm-{iso3}-"))
    if cache is not None:
        base_root.mkdir(parents=True, exist_ok=True)
    level_dir = base_root / f"ADM{level}"
    return _extract_level(zip_path, iso3, level, level_dir)


def download_country_gpkg(
    iso3: str,
    *,
    cache: Optional[HttpCache] = None,
    timeout: float = 300.0,
) -> Path:
    """Download the single-file GADM GeoPackage for a country (all levels)."""

    url = build_country_gpkg_url(iso3)
    return _download(url, cache=cache, timeout=timeout)


def list_available_levels(
    iso3: str,
    *,
    cache: Optional[HttpCache] = None,
    timeout: float = 30.0,
) -> list[str]:
    """Return the list of levels (0-5) that GADM has for *iso3*.

    Strategy:
      1. If the country zip is already in cache, peek into its central
         directory to enumerate which ``gadm41_{ISO}_{N}.shp`` files
         are present.
      2. Otherwise, probe the country zip with a GET-Range (asking for
         the first 1 byte). If it exists we return all 0-5 levels as a
         permissive best guess; the actual level will be confirmed (or
         rejected) when the user requests a download.
    """

    iso = iso3.upper()
    if cache is not None:
        url = build_country_shp_url(iso)
        cached = cache.get_path(url)
        if cached is not None:
            return _levels_in_zip(cached, iso)

    url = build_country_shp_url(iso)
    try:
        r = requests.get(
            url,
            timeout=timeout,
            headers={"Range": "bytes=0-0"},
            stream=True,
        )
    except requests.RequestException:
        return []
    try:
        if r.status_code in (200, 206):
            # We only know the country exists; levels will be checked on demand.
            return [f"ADM{n}" for n in range(0, 6)]
    finally:
        try:
            r.close()
        except Exception:
            pass
    return []


def _levels_in_zip(zip_path: Path, iso: str) -> list[str]:
    """Return the list of ``ADM<n>`` levels present in the GADM country zip."""

    out: list[str] = []
    try:
        with zipfile.ZipFile(zip_path) as zf:
            for name in zf.namelist():
                stem = Path(name).name
                if not stem.startswith(f"gadm41_{iso}_"):
                    continue
                rest = stem[len(f"gadm41_{iso}_"):]
                if not rest.endswith(".shp"):
                    continue
                num = rest[:-4]  # strip ".shp"
                if num.isdigit():
                    out.append(f"ADM{num}")
    except (OSError, zipfile.BadZipFile):
        return []
    return sorted(set(out), key=lambda s: int(s[3:]))


def warn_license() -> str:
    """Return the GADM license notice (print once at first use)."""

    return GADM_LICENSE_NOTICE
