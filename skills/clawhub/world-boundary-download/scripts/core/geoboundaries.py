"""geoBoundaries (https://www.geoboundaries.org/) data source client.

Implements two releases:

* ``gbOpen`` (default) - every boundary, all licenses, can include
  contested / overlapping areas. CC BY 4.0 mostly, with public domain
  for many entries.
* ``gbAuthoritative`` - authoritative boundaries only.
* ``gbHumanitarian`` - humanitarian / OCHA-sourced only.

The API is JSON-based:

    https://www.geoboundaries.org/api/current/{release}/{ISO3}/{ADM}/

Each response contains a ``staticDownloadLink`` pointing to a ZIP
archive with Shapefile + GeoJSON + TopoJSON side-by-side, plus
metadata fields (year, source, license, area, vertex counts, etc.).

The implementation here is a thin wrapper that:
  - issues HTTP GETs with retries and exponential backoff,
  - caches raw JSON and the ZIP bodies on disk,
  - normalises the response into a flat dict that other modules use.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urljoin

import requests

from .cache import HttpCache
from .exceptions import DataSourceError, NetworkError

API_BASE = "https://www.geoboundaries.org/api/current/"
DEFAULT_RELEASE = "gbOpen"
ALLOWED_RELEASES = ("gbOpen", "gbAuthoritative", "gbHumanitarian")

# Standard retries; geoBoundaries is hosted on GitHub LFS and occasionally
# hiccups with 5xx, so 3 attempts with backoff are usually enough.
RETRYABLE_STATUS = {429, 500, 502, 503, 504}
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_S = 1.5


def _norm_release(release: str) -> str:
    r = (release or DEFAULT_RELEASE).strip()
    if r not in ALLOWED_RELEASES:
        raise DataSourceError(
            f"unknown geoBoundaries release: {release!r}. "
            f"Expected one of {ALLOWED_RELEASES}",
            source="geoboundaries",
        )
    return r


def _http_get_json(
    url: str,
    *,
    cache: Optional[HttpCache] = None,
    timeout: float = 60.0,
    force_network: bool = False,
) -> Any:
    """GET *url* and return parsed JSON. Caches the raw bytes by default."""

    if cache is not None and not force_network:
        cached = cache.get_bytes(url)
        if cached is not None:
            return json.loads(cached.decode("utf-8"))

    last_err: Optional[Exception] = None
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            r = requests.get(url, timeout=timeout)
        except requests.RequestException as e:
            last_err = e
            if attempt >= RETRY_ATTEMPTS:
                raise NetworkError(f"GET {url} failed: {e}") from e
            time.sleep(RETRY_BACKOFF_S * attempt)
            continue

        if r.status_code in RETRYABLE_STATUS:
            last_err = DataSourceError(
                f"GET {url} returned {r.status_code}",
                source="geoboundaries",
            )
            if attempt >= RETRY_ATTEMPTS:
                raise last_err
            time.sleep(RETRY_BACKOFF_S * attempt)
            continue

        if r.status_code == 404:
            # 404 on geoBoundaries means "no data for this ISO/ADM pair".
            return None
        if not r.ok:
            raise DataSourceError(
                f"GET {url} returned {r.status_code}: {r.text[:200]}",
                source="geoboundaries",
            )

        try:
            data = r.json()
        except ValueError as e:
            raise DataSourceError(
                f"GET {url} did not return JSON: {r.text[:200]}",
                source="geoboundaries",
            ) from e

        if cache is not None:
            cache.put(
                url,
                r.content,
                etag=r.headers.get("ETag"),
                content_type=r.headers.get("Content-Type"),
            )
        return data

    # Should be unreachable.
    raise NetworkError(f"GET {url} failed after retries: {last_err}")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def build_meta_url(release: str, iso3: str, adm: str) -> str:
    """Compose the metadata API URL."""

    return urljoin(API_BASE, f"{_norm_release(release)}/{iso3.upper()}/{adm}/")


def fetch_metadata(
    iso3: str,
    adm: str,
    *,
    release: str = DEFAULT_RELEASE,
    cache: Optional[HttpCache] = None,
) -> Optional[dict]:
    """Return the raw metadata dict for one (ISO3, ADM) pair.

    Returns ``None`` if geoBoundaries has no boundary for that pair
    (404). Raises :class:`DataSourceError` on malformed responses.
    """

    url = build_meta_url(release, iso3, adm)
    data = _http_get_json(url, cache=cache)
    if data is None:
        return None
    if not isinstance(data, dict):
        raise DataSourceError(
            f"expected dict from {url}, got {type(data).__name__}",
            source="geoboundaries",
            iso=iso3,
            level=adm,
        )
    return data


def fetch_all_metadata(
    *,
    release: str = DEFAULT_RELEASE,
    cache: Optional[HttpCache] = None,
) -> list[dict]:
    """Return metadata for every boundary in the given release.

    The full index is large (~1k entries) but is cached as a single
    JSON blob, so repeated calls are cheap.
    """

    url = urljoin(API_BASE, f"{_norm_release(release)}/ALL/ALL/")
    data = _http_get_json(url, cache=cache)
    if data is None:
        return []
    if not isinstance(data, list):
        raise DataSourceError(
            f"expected list from {url}, got {type(data).__name__}",
            source="geoboundaries",
        )
    return data


def list_available_levels(
    iso3: str,
    *,
    release: str = DEFAULT_RELEASE,
    cache: Optional[HttpCache] = None,
) -> list[str]:
    """Return sorted list of ADM levels that geoBoundaries has for *iso3*."""

    out: list[str] = []
    for adm in ("ADM0", "ADM1", "ADM2", "ADM3", "ADM4", "ADM5"):
        try:
            meta = fetch_metadata(iso3, adm, release=release, cache=cache)
        except DataSourceError:
            continue
        if meta is not None:
            out.append(adm)
    return out


def download_zip(
    iso3: str,
    adm: str,
    *,
    release: str = DEFAULT_RELEASE,
    simplified: bool = False,
    cache: Optional[HttpCache] = None,
    force: bool = False,
    timeout: float = 120.0,
) -> Path:
    """Download the boundary ZIP (or simplified GeoJSON) and cache it.

    Returns the absolute path of the cached file.
    """

    meta = fetch_metadata(iso3, adm, release=release, cache=cache)
    if meta is None:
        raise DataSourceError(
            f"geoBoundaries has no {adm} data for {iso3}",
            source="geoboundaries",
            iso=iso3,
            level=adm,
        )

    if simplified:
        url = meta.get("simplifiedGeometryGeoJSON")
        if not url:
            raise DataSourceError(
                f"no simplified geometry available for {iso3} {adm}",
                source="geoboundaries",
                iso=iso3,
                level=adm,
            )
    else:
        url = meta.get("staticDownloadLink") or meta.get("gjDownloadURL")
        if not url:
            raise DataSourceError(
                f"metadata for {iso3} {adm} has no download link",
                source="geoboundaries",
                iso=iso3,
                level=adm,
            )

    if cache is not None and not force:
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
                f"GET {url} returned {r.status_code}",
                source="geoboundaries",
            )
            if attempt >= RETRY_ATTEMPTS:
                raise last_err
            time.sleep(RETRY_BACKOFF_S * attempt)
            continue

        if not r.ok:
            raise DataSourceError(
                f"GET {url} returned {r.status_code}: {r.text[:200]}",
                source="geoboundaries",
                iso=iso3,
                level=adm,
            )

        # Read into memory (geoBoundaries zips are <50 MB).
        data = r.content
        if cache is not None:
            return cache.put(
                url,
                data,
                etag=r.headers.get("ETag"),
                content_type=r.headers.get("Content-Type"),
            )
        # No cache: write to a temporary file and return it.
        import tempfile
        suffix = ".geojson" if simplified or url.endswith(".geojson") else ".zip"
        fd, name = tempfile.mkstemp(prefix=f"gb-{iso3}-{adm}-", suffix=suffix)
        with open(fd, "wb") as f:
            f.write(data)
        return Path(name)

    raise NetworkError(f"GET {url} failed after retries: {last_err}")


# ---------------------------------------------------------------------------
# Metadata flattening
# ---------------------------------------------------------------------------

# JSON keys returned by geoBoundaries in camelCase, mapped to snake_case
# the rest of this skill uses.
_KEY_MAP = {
    "boundaryID": "boundary_id",
    "boundaryName": "name",
    "boundaryISO": "iso3",
    "boundaryYearRepresented": "year",
    "boundaryType": "level",
    "boundaryCanonical": "canonical_name",
    "boundarySource": "source",
    "boundaryLicense": "license",
    "licenseDetail": "license_detail",
    "licenseSource": "license_source",
    "boundarySourceURL": "source_url",
    "sourceDataUpdateDate": "source_data_update_date",
    "buildDate": "build_date",
    "Continent": "continent",
    "UNSDG-region": "unsdg_region",
    "UNSDG-subregion": "unsdg_subregion",
    "worldBankIncomeGroup": "world_bank_income_group",
    "admUnitCount": "adm_unit_count",
    "staticDownloadLink": "download_url",
    "gjDownloadURL": "geojson_url",
    "tjDownloadURL": "topojson_url",
    "simplifiedGeometryGeoJSON": "simplified_geojson_url",
    "imagePreview": "image_preview",
    "meanVertices": "mean_vertices",
    "minVertices": "min_vertices",
    "maxVertices": "max_vertices",
    "meanPerimeterLengthKM": "mean_perimeter_km",
    "minPerimeterLengthKM": "min_perimeter_km",
    "maxPerimeterLengthKM": "max_perimeter_km",
    "meanAreaSqKM": "mean_area_km2",
    "minAreaSqKM": "min_area_km2",
    "maxAreaSqKM": "max_area_km2",
}


def flatten_meta(meta: dict) -> dict:
    """Return a copy of *meta* with snake_case keys."""

    out: dict[str, Any] = {v: meta.get(k) for k, v in _KEY_MAP.items()}
    # Always add the source label.
    out.setdefault("source", "geoboundaries")
    return out
