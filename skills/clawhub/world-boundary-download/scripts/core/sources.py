"""Source registry and fallback chain.

A *Source* is an object that, given (iso3, level), can return a
:mod:`.format`-ready file path. Each source is responsible for its
own URL scheme, cache, retry policy, and license handling.

The default :func:`fetch` function tries sources in a priority order
until one succeeds. Callers can also pin a specific source via
``--source`` to skip the fallback chain.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Protocol

from . import geoboundaries, gadm, natural_earth
from .cache import HttpCache
from .exceptions import DataSourceError


# ---------------------------------------------------------------------------
# Source protocol
# ---------------------------------------------------------------------------

class Source(Protocol):
    name: str
    description: str

    def list_levels(self, iso3: str, *, cache: HttpCache) -> list[str]: ...

    def fetch(
        self,
        iso3: str,
        level: str,
        *,
        cache: HttpCache,
        simplified: bool = False,
    ) -> Path: ...


# ---------------------------------------------------------------------------
# geoBoundaries
# ---------------------------------------------------------------------------

class GeoBoundariesSource:
    name = "geoboundaries"
    description = "geoBoundaries (CC BY 4.0); default; best metadata"

    def list_levels(self, iso3: str, *, cache: HttpCache) -> list[str]:
        return geoboundaries.list_available_levels(iso3, cache=cache)

    def fetch(
        self,
        iso3: str,
        level: str,
        *,
        cache: HttpCache,
        simplified: bool = False,
    ) -> Path:
        return geoboundaries.download_zip(
            iso3,
            level,
            cache=cache,
            simplified=simplified,
        )


# ---------------------------------------------------------------------------
# GADM 4.1
# ---------------------------------------------------------------------------

class GadmSource:
    name = "gadm"
    description = "GADM 4.1 (free for non-commercial use only)"

    def __init__(self) -> None:
        self._license_warned = False

    def list_levels(self, iso3: str, *, cache: HttpCache) -> list[str]:
        return gadm.list_available_levels(iso3, cache=cache)

    def fetch(
        self,
        iso3: str,
        level: str,
        *,
        cache: HttpCache,
        simplified: bool = False,
    ) -> Path:
        if not self._license_warned:
            print(f"[gadm] {gadm.warn_license()}")
            self._license_warned = True
        if level.upper() == "ALL":
            # ALL isn't a single file in GADM; refuse rather than guess.
            raise DataSourceError(
                "GADM does not support ALL levels in a single call; pick ADM0..ADM5",
                source=self.name,
            )
        level_num = int(level.upper().lstrip("ADM"))
        return gadm.download_country_shp(iso3, level_num, cache=cache)


# ---------------------------------------------------------------------------
# Natural Earth
# ---------------------------------------------------------------------------

class NaturalEarthSource:
    name = "natural_earth"
    description = "Natural Earth (public domain); ADM0 + ADM1 only"

    def list_levels(self, iso3: str, *, cache: HttpCache) -> list[str]:
        # Natural Earth is a global basemap, not country-specific.
        return natural_earth.list_available_levels()

    def fetch(
        self,
        iso3: str,
        level: str,
        *,
        cache: HttpCache,
        simplified: bool = False,
    ) -> Path:
        if level.upper() not in ("ADM0", "ADM1"):
            raise DataSourceError(
                "Natural Earth only provides ADM0 / ADM1; pick one of those",
                source=self.name,
                level=level,
            )
        zip_path = natural_earth.download_layer(level.upper(), cache=cache)
        # Natural Earth ships a world file; extract + filter by ISO to
        # match the request. We write the filtered SHP set to a stable
        # cache path so repeated calls don't redo the work.
        target = cache.root / "natural_earth" / iso3.upper() / level.upper()
        if (target / f"ne_{iso3.upper()}_{level.upper()}.shp").exists():
            return target
        import zipfile
        import shutil
        import tempfile
        import geopandas as gpd
        target.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as td:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(td)
            shp_files = list(Path(td).rglob("*.shp"))
            if not shp_files:
                raise DataSourceError(
                    f"Natural Earth zip {zip_path} contained no .shp",
                    source=self.name,
                )
            gdf = gpd.read_file(shp_files[0])
        gdf = natural_earth.filter_by_iso(gdf, iso3)
        if len(gdf) == 0:
            raise DataSourceError(
                f"Natural Earth has no {level} for {iso3}",
                source=self.name,
                iso=iso3,
                level=level,
            )
        out_shp = target / f"ne_{iso3.upper()}_{level.upper()}.shp"
        gdf.to_file(str(out_shp), driver="ESRI Shapefile")
        return target


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

REGISTRY: dict[str, Source] = {
    "geoboundaries": GeoBoundariesSource(),
    "gadm": GadmSource(),
    "natural_earth": NaturalEarthSource(),
}

DEFAULT_FALLBACK_CHAIN: list[str] = [
    "geoboundaries",
    "gadm",
    "natural_earth",
]


def get_source(name: str) -> Source:
    if name not in REGISTRY:
        raise DataSourceError(
            f"unknown source: {name!r}; expected one of {list(REGISTRY)}",
            source=name,
        )
    return REGISTRY[name]


# ---------------------------------------------------------------------------
# Fallback-aware fetch
# ---------------------------------------------------------------------------

@dataclass
class FetchResult:
    source: str
    path: Path
    iso3: str
    level: str
    note: str = ""


def fetch(
    iso3: str,
    level: str,
    *,
    cache: HttpCache,
    source: Optional[str] = None,
    simplified: bool = False,
    chain: Optional[list[str]] = None,
) -> FetchResult:
    """Fetch a boundary using either a pinned source or the fallback chain.

    Returns the first source that returns a file path. Raises
    :class:`DataSourceError` if every source in the chain fails.
    """

    if source:
        chain = [source]
    else:
        chain = chain or DEFAULT_FALLBACK_CHAIN

    last_err: Optional[Exception] = None
    notes: list[str] = []
    for src_name in chain:
        src = get_source(src_name)
        try:
            path = src.fetch(iso3, level, cache=cache, simplified=simplified)
            return FetchResult(
                source=src_name,
                path=path,
                iso3=iso3,
                level=level,
                note="; ".join(notes),
            )
        except DataSourceError as e:
            last_err = e
            notes.append(f"{src_name}: {e}")
            continue
        except Exception as e:  # pragma: no cover - defensive
            last_err = e
            notes.append(f"{src_name}: {e}")
            continue

    raise DataSourceError(
        f"all sources failed for {iso3} {level}: {' | '.join(notes)}",
        source=source or "fallback",
        iso=iso3,
        level=level,
    ) from last_err
