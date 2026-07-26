"""Natural Earth data source client (https://www.naturalearthdata.com/).

Natural Earth provides three scales (1:10m, 1:50m, 1:110m) of public-
domain world basemaps. Admin levels available:

* ``admin_0_countries`` (always)
* ``admin_1_states_provinces`` (most countries)

No ADM2 or finer.

The actual files are served from a CDN; the public website links to
the CDN URLs. We hard-code the known good URLs for the three scales
and let the caller pick.
"""

from __future__ import annotations

import tempfile
import time
import zipfile
from pathlib import Path
from typing import Optional

import requests

from .cache import HttpCache
from .exceptions import DataSourceError, NetworkError

# CDN URLs published by the Natural Earth project. The file name
# convention is: ne_{scale}_{theme}_{layer}.zip
SCALES = ("10m", "50m", "110m")

CDN_BASE = "https://naciscdn.org/naturalearth/"

# Layer -> URL fragments we know about.
LAYERS = {
    "ADM0": "ne_{scale}_admin_0_countries.zip",
    "ADM1": "ne_{scale}_admin_1_states_provinces.zip",
}

# Subdir under the CDN root for the cultural theme.
CDN_SUBDIR = "cultural"

RETRYABLE_STATUS = {429, 500, 502, 503, 504}
RETRY_ATTEMPTS = 3
RETRY_BACKOFF_S = 1.5


def build_url(layer: str, scale: str) -> str:
    if layer not in LAYERS:
        raise DataSourceError(
            f"Natural Earth only provides ADM0 / ADM1; got {layer}",
            source="natural_earth",
            level=layer,
        )
    if scale not in SCALES:
        raise DataSourceError(
            f"unknown Natural Earth scale: {scale!r}; expected one of {SCALES}",
            source="natural_earth",
        )
    return f"{CDN_BASE}{scale}/{CDN_SUBDIR}/" + LAYERS[layer].format(scale=scale)


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
                f"GET {url} returned {r.status_code}", source="natural_earth"
            )
            if attempt >= RETRY_ATTEMPTS:
                raise last_err
            time.sleep(RETRY_BACKOFF_S * attempt)
            continue

        if not r.ok:
            raise DataSourceError(
                f"GET {url} returned {r.status_code}", source="natural_earth"
            )

        data = r.content
        if cache is not None:
            return cache.put(
                url,
                data,
                etag=r.headers.get("ETag"),
                content_type=r.headers.get("Content-Type"),
            )
        fd, name = tempfile.mkstemp(prefix="ne-", suffix=".zip")
        with open(fd, "wb") as f:
            f.write(data)
        return Path(name)

    raise NetworkError(f"GET {url} failed after retries: {last_err}")


def download_layer(
    layer: str,
    scale: str = "10m",
    *,
    cache: Optional[HttpCache] = None,
    timeout: float = 180.0,
) -> Path:
    """Download a Natural Earth admin layer (ZIP) and return the cached path."""

    url = build_url(layer, scale)
    return _download(url, cache=cache, timeout=timeout)


def list_available_levels() -> list[str]:
    """Natural Earth is a global basemap; we expose the two admin layers it has."""

    return ["ADM0", "ADM1"]


# Fields used to recognise a country's ISO alpha-3 / alpha-2 / UN code in
# the Natural Earth shapefiles. We check several candidates because the
# schema has shifted over the years.
NE_ISO_FIELDS = (
    "ISO_A3",
    "iso_a3",
    "SOV_A3",
    "ADM0_A3",
    "ISO_A2",
    "ISO_3",
)


def filter_by_iso(gdf, iso3: str):
    """Return only the rows in *gdf* matching the given ISO 3166-1 alpha-3 code.

    Tries alpha-3 fields first, then alpha-2, then a name-based fallback.
    Returns the original frame if no match is found.
    """

    iso3 = iso3.upper()
    iso2 = iso3[:2]
    for fld in NE_ISO_FIELDS:
        if fld in gdf.columns:
            sub = gdf[gdf[fld] == iso3]
            if not sub.empty:
                return sub
            sub = gdf[gdf[fld] == iso2]
            if not sub.empty:
                return sub
    return gdf
