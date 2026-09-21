<!-- merged by groq/openai/gpt-oss-120b from 2 shard(s) on 2026-09-20 -->

**Summary** – This reference aggregates publicly documented ways to obtain offline map data (MWM, OSM extracts, tile packs), build routing engines, and use offline features in popular navigation apps, preserving all concrete facts from both research shards.

---

## 1. MWM region files (Maps.me, Organic Maps, CoMaps)

| Provider | Distribution method | URL template (example) | Region‑file naming | Approx. size per region | Update cadence | Third‑party download allowed? | Source |
|----------|--------------------|------------------------|--------------------|------------------------|----------------|------------------------------|--------|
| **Maps.me** (original) | Central server – ZIP of *.mwm* files per country/region | `https://maps.me/download/v5.0/2024-03-01/planet/2024-03-01-<region>.mwm` | `<region>.mwm` (ISO‑3166‑1 alpha‑2 or composite, e.g. `us_california.mwm`) | 5 – 150 MB (small islands ≈ 5 MB, large countries ≈ 150 MB) | Daily builds; new version published when OSM planet diff is applied (≈ once per day) | ✅ Yes – URLs listed in the Maps.me help page | [src](https://support.maps.me/hc/en-us/articles/360018459311-How-to-download-maps) |
| **Maps.me** (alternative claim) | In‑app download (no public URL documented) | `https://maps.me/maps/251209/US_New York_New York.mwm` | Similar ISO‑like naming | Varies by region (unspecified) | OSM data updated monthly; app updates more frequent | ⚠️ CONFLICT – Shard 1 says public URLs exist; Shard 2 says not officially supported | [src](https://maps.me/maps/) |
| **Organic Maps** (official mirror) | Mirrors Maps.me files; public CDN | `https://maps.organicmaps.app/download/2024-03-01/<region>.mwm` | Same as Maps.me | 5 – 150 MB (same as Maps.me) | Mirrors Maps.me daily release | ✅ Yes – documented on the Organic Maps wiki | [src](https://github.com/organicmaps/organicmaps/wiki/Offline-maps) |
| **Organic Maps** (alternative claim) | In‑app download; CDN not publicly exposed | `https://omaps.app/maps/251209/US_New York_New York.mwm` | ISO‑like but not strictly ISO (e.g., `US_New York_New York.mwm`) | US state ≈ 50‑500 MB; country ≈ 1‑10 GB | OSM data updated monthly; app updates more frequent | ⚠️ CONFLICT – Shard 1 says public URLs; Shard 2 says not officially supported | [src](https://github.com/organicmaps/organicmaps/issues/7210) |
| **CoMaps** (community fork) | Mirrors same files; public mirror | `https://comaps.org/downloads/<region>.mwm` | Same as Maps.me | 5 – 150 MB (same as Maps.me) | Mirrors Maps.me releases (usually within 24 h) | ✅ Yes – README states “All .mwm files are freely downloadable” | [src](https://github.com/comaps/comaps#offline-maps) |
| **CoMaps** (alternative claim) | Custom map server; same structure as Organic Maps | `/maps/251209/US_New York_New York.mwm` (relative) | Same as Organic Maps | Same as Organic Maps (50‑500 MB per US state) | OSM data updated monthly; app updates more frequent | ✅ Yes – self‑hosting documented | [src](https://www.comaps.app/support/how-can-i-host-a-custom-map-server-for-downloads/) |

> **⚠️ CONFLICT** rows indicate contradictory statements between the two shards. Both versions are retained with the conflict marker.

---

## 2. OSM extracts (Geofabrik & BBBike)

| Provider | Root URL | Example file (country/region) | Format | Update cadence | License | Source |
|----------|----------|------------------------------|--------|----------------|---------|--------|
| **Geofabrik** | <https://download.geofabrik.de/> | <https://download.geofabrik.de/europe/germany-latest.osm.pbf> | `.osm.pbf` (primary), also `.shp.zip`, `.poly` | Daily for “planet”; weekly for continent/country extracts (Shard 1) **or** daily for most regions, diffs kept 100 days (Shard 2) | ODbL (same as OSM) | [src](https://download.geofabrik.de/) |
| **BBBike** | <https://download.bbbike.org/osm/> | <https://download.bbbike.org/osm/planet/europe/germany-latest.osm.pbf> (Shard 1) <br> <https://download.bbbike.org/osm/extract/germany_berlin.osm.pbf> (Shard 2) | `.osm.pbf` (plus many other formats) | Weekly for country extracts (Shard 1) **or** daily for PBF, weekly for other formats (Shard 2) | ODbL | [src](https://download.bbbike.org/osm/) |

Both sites provide checksum files (`.md5`, `.sha256`) for verification.

---

## 3. Building offline routing engines

| Router | Minimal CLI steps (Linux) | Approx. RAM / Disk for a **small** country (≈ 2 M nodes) | Notes on larger regions | Source |
|--------|---------------------------|--------------------------------------------------------|--------------------------|--------|
| **OSRM** | ```bash\n# 1. Extract\nosrm-extract luxembourg-latest.osm.pbf -p profiles/car.lua\n# 2. Partition (MLD)\nosrm-partition luxembourg-latest.osrm\n# 3. Customize\nosrm-customize luxembourg-latest.osrm\n# 4. Run server\nosrm-routed luxembourg-latest.osrm\n``` | Shard 1: RAM ≈ 2 GB (partition); Disk ≈ 1 GB (pbf) + ~2 GB (osrm files) <br> **⚠️ CONFLICT** – Shard 2: RAM ≈ 4 GB; Disk ≈ 10 GB total | Medium country (e.g., Germany): ~16 GB RAM, ~50 GB disk (Shard 2) | [src](https://github.com/Project-OSRM/osrm-backend/wiki/Running-OSRM) |
| **Valhalla** | ```bash\n# 1. Build tiles\nvalhalla_build_tiles -c valhalla.json luxembourg-latest.osm.pbf\n# 2. Serve\nvalhalla_service valhalla.json\n``` | Shard 1: RAM ≈ 4 GB; Disk ≈ 1 GB (pbf) + ~3 GB (tiles) <br> **⚠️ CONFLICT** – Shard 2: RAM ≈ 8 GB; Disk ≈ 20 GB (small) | Small country: ~32 GB RAM, ~100 GB disk (medium) | [src](https://valhalla.readthedocs.io/en/latest/installation/) |
| **GraphHopper** | ```bash\n./graphhopper.sh import -i luxembourg-latest.osm.pbf -c config.yml\n# then start the server\n./graphhopper.sh web\n``` | Shard 1: RAM ≈ 4 GB (JVM `-Xmx4g`); Disk ≈ 1 GB (pbf) + ~2 GB (graph) <br> **⚠️ CONFLICT** – Shard 2: RAM ≈ 4 GB; Disk ≈ 10 GB (small) | Medium country: ~16 GB RAM, ~50 GB disk (Shard 2) | [src](https://github.com/graphhopper/graphhopper/blob/master/docs/core/README.md) |

> **⚠️ CONFLICT** rows show differing resource estimates; both are retained.

---

## 4. Offline map support in major navigation apps

| App | Offline map download? | Offline turn‑by‑turn routing | Offline POI / search | Offline traffic / live updates | Notes / Limitations | Source |
|-----|-----------------------|-----------------------------|----------------------|-------------------------------|----------------------|--------|
| **Google Maps** | ✅ – download “area” (up to 200 km²) via UI | ✅ – driving, walking, cycling within downloaded area (no live traffic) | ❌ – only previously saved places; no full POI search offline | ❌ – traffic & transit require online | – | [src](https://support.google.com/maps/answer/6291838) |
| **Apple Maps** | ✅ – maps cached automatically; no user‑controlled download (Shard 1) **or** ✅ – limited offline map viewing (Shard 2) | ❌ – routing requires online (Shard 1) **or** ✅ – all navigation types offline (Shard 2) | ❌ – search requires online (Shard 1) **or** ✅ – limited search offline (Shard 2) | ❌ – traffic requires online | **⚠️ CONFLICT** – differing statements on offline capability | [src](https://support.apple.com/en-us/HT207028) |
| **HERE WeGo** | ✅ – download whole‑country vector maps | ✅ – car, pedestrian, bike routing offline | ✅ – POI search works offline for downloaded regions | ✅ – limited offline traffic (premium) | – | [src](https://www.here.com/en-us/help/offline-maps) |
| **Sygic** | ✅ – full‑offline map packs | ✅ – routing, voice guidance, lane assistance offline | ✅ – POI database included | ✅ – optional offline traffic (subscription) | – | [src](https://support.sygic.com/hc/en-us/articles/360001232759-How-to-download-maps-for-offline-use) |
| **Waze** | ❌ – no explicit offline download; can cache recent routes for a few minutes (Shard 2) | ❌ – routing needs live data (Shard 1) **or** ❌ – same (Shard 2) | ❌ – POI search offline | ❌ – traffic core to Waze, online only | **⚠️ CONFLICT** – Shard 2 mentions “basic GPS, preloaded route” | [src](https://support.waze.com/en/article/offline-use) |

---

## 5. Offline tile packs / containers

| Format / Source | Download URL (example) | Typical size for a small country (e.g., Belgium) | How to serve (open‑source) | Notes | Source |
|-----------------|------------------------|---------------------------------------------------|----------------------------|-------|--------|
| **OpenMapTiles** (vector MBTiles) | <https://download.openmaptiles.org/tiles/2024-03-01/Belgium.mbtiles> | ≈ 250 MB (vector) | `tileserver-gl` Docker: `docker run -p 8080:80 -v $(pwd)/Belgium.mbtiles:/data/tiles.mbtiles maptiler/tileserver-gl` | Official download page | [src](https://openmaptiles.org/downloads/) |
| **Maptiler Cloud** (raster & vector) | <https://cloud.maptiler.com/tiles/> (requires free account) | Raster PNG for Belgium ≈ 1 GB (z0‑z14) | Same as above (`tileserver-gl` or `tileserver-php`) | Requires account | [src](https://docs.maptiler.com/tileserver/) |
| **PMTiles** (single‑file container) | <https://github.com/protomaps/PMTiles/releases/download/v2.0.0/pmtiles-example.zip> (example pack) | Belgium ≈ 180 MB (compressed) | `pmtiles serve ./belgium.pmtiles` (binary from GitHub) | Cloud‑optimized, works from static storage | [src](https://github.com/protomaps/PMTiles#cli) |
| **MBTiles** (generic) | Various sources (e.g., OSM QA Tiles, BBBike MBTiles) | Varies; typical country ≈ 300‑800 MB (vector) | `tileserver-gl`, MapLibre, or custom SQLite server | SQLite‑based; many tools (`gdal_translate`, `tippecanoe`) | [src](https://wiki.openstreetmap.org/wiki/MBTiles) |
| **Protomaps Basemaps (PMTiles)** | <https://source.coop/protomaps/openstreetmap/tiles/v3.pmtiles> (global 115 GB) | Global dataset; small country subset ≈ 200 MB | Same `pmtiles serve` binary | Cloud‑optimized, single‑file archive | [src](https://github.com/protomaps/basemaps) |

---

## 6. Deep‑link templates for programmatic map download

| Action | URL template | Required parameters | Source |
|--------|--------------|---------------------|--------|
| **Maps.me region download** | `https://maps.me/download/v5.0/{date}/planet/{date}-{region}.mwm` | `date` (YYYY‑MM‑DD), `region` (ISO‑2 or composite) | [src](https://support.maps.me/hc/en-us/articles/360018459311-How-to-download-maps) |
| **Organic Maps mirror** | `https://maps.organicmaps.app/download/{date}/{region}.mwm` | `date`, `region` | [src](https://github.com/organicmaps/organicmaps/wiki/Offline-maps) |
| **CoMaps mirror** | `https://comaps.org/downloads/{region}.mwm` | `region` | [src](https://github.com/comaps/comaps#offline-maps) |
| **Geofabrik extract** | `https://download.geofabrik.de/{continent}/{country}-latest.osm.pbf` | `continent`, `country` | [src](https://download.geofabrik.de/) |
| **BBBike extract (PBF)** | `https://download.bbbike.org/osm/{path}/{region}-latest.osm.pbf` | `path` (e.g., `planet/europe`), `region` | [src](https://download.bbbike.org/osm/) |
| **OpenMapTiles download** | `https://download.openmaptiles.org/tiles/{date}/{country}.mbtiles` | `date`, `country` | [src](https://openmaptiles.org/downloads/) |
| **PMTiles example** | `https://github.com/protomaps/PMTiles/releases/download/v{ver}/pmtiles-example.zip` | `ver` (release version) | [src](https://github.com/protomaps/PMTiles#cli) |

---

## Sources

- https://support.maps.me/hc/en-us/articles/360018459311-How-to-download-maps  
- https://maps.organicmaps.app/download/2024-03-01/<region> (example pattern)  
- https://github.com/organicmaps/organicmaps/wiki/Offline-maps  
- https://github.com/comaps/comaps#offline-maps  
- https://github.com/organicmaps/organicmaps/issues/7210  
- https://organicmaps.app/news/  
- https://github.com/organicmaps/organicmaps  
- https://wiki.openstreetmap.org/wiki/Organic_Maps  
- https://www.comaps.app/support/how-can-i-host-a-custom-map-server-for-downloads/  
- https://wiki.openstreetmap.org/wiki/CoMaps  
- https://codeberg.org/comaps/meta-php  
- https://maps.me/maps/  
- https://download.geofabrik.de/  
- https://download.geofabrik.de/technical.html  
- https://download.geofabrik.de/europe/germany-latest.osm.pbf  
- https://download.bbbike.org/osm/  
- https://download.bbbike.org/osm/planet/europe/germany-latest.osm.pbf  
- https://download.bbbike.org/osm/extract/germany_berlin.osm.pbf  
- https://extract.bbbike.org/ (custom extracts)  
- https://github.com/Project-OSRM/osrm-backend/wiki/Running-OSRM  
- https://github.com/Project-OSRM/osrm-backend/wiki/Disk-and-Memory-Requirements  
- https://valhalla.readthedocs.io/en/latest/installation/  
- https://github.com/valhalla/valhalla  
- https://github.com/graphhopper/graphhopper/blob/master/docs/core/README.md  
- https://support.google.com/maps/answer/6291838  
- https://support.apple.com/en-us/HT207028  
- https://www.here.com/en-us/help/offline-maps  
- https://support.sygic.com/hc/en-us/articles/360001232759-How-to-download-maps-for-offline-use  
- https://support.waze.com/en/article/offline-use  
- https://openmaptiles.org/downloads/  
- https://docs.maptiler.com/tileserver/  
- https://github.com/protomaps/PMTiles#cli  
- https://github.com/protomaps/PMTiles  
- https://wiki.openstreetmap.org/wiki/MBTiles  
- https://source.coop/protomaps/openstreetmap/tiles/v3.pmtiles  

*All URLs are presented exactly as cited in the source shards.*
