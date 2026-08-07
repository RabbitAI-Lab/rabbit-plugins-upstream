#!/usr/bin/env python3
"""
Urban Green Equity - Assess green space distribution fairness.

Evaluates quantity, quality, and walkable accessibility of urban green spaces
across populations and communities. Identifies service gaps and priority areas.

Exit codes:
    0 = success
    2 = argument error
    3 = dependency missing
    6 = validation error
    7 = processing failure
"""

import argparse
import csv
import heapq
import json
import math
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

EXIT_OK = 0
EXIT_ARG = 2
EXIT_DEP = 3
EXIT_VALIDATION = 6
EXIT_PROCESSING = 7

# Walk speed km/h per road type
WALK_SPEEDS = {
    "motorway": 0, "trunk": 0, "primary": 5, "secondary": 5,
    "tertiary": 5, "residential": 5, "service": 4, "unclassified": 5,
    "living_street": 5, "footway": 5, "path": 4, "pedestrian": 5,
    "cycleway": 4, "steps": 3, "default": 5,
}

# Green space quality weights by type
GREEN_QUALITY = {
    "park": 1.0, "garden": 0.9, "nature_reserve": 1.0,
    "recreation_ground": 0.85, "wood": 0.8, "forest": 0.8,
    "grass": 0.6, "heath": 0.5, "meadow": 0.6,
    "village_green": 0.7, "common": 0.7, "playground": 0.75,
    "dog_park": 0.7, "default": 0.6,
}

# Minimum green space area (m²) to be considered
MIN_GREEN_AREA_M2 = 100.0


# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------

def _haversine_distance(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """Compute haversine distance in km between two (lon, lat) points."""
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def _line_length_km(coords: List[List[float]]) -> float:
    """Compute total length of a line in km from coordinate list."""
    total = 0.0
    for i in range(1, len(coords)):
        total += _haversine_distance(coords[i - 1][0], coords[i - 1][1], coords[i][0], coords[i][1])
    return total


def _polygon_area_approx(coords: List[List[float]]) -> float:
    """Approximate polygon area in m² using cos(lat) correction for EPSG:4326."""
    if len(coords) < 4:
        return 0.0
    # Use centroid latitude for correction
    lats = [c[1] for c in coords]
    lat_center = sum(lats) / len(lats)
    cos_lat = math.cos(math.radians(lat_center))

    # Shoelace formula
    area = 0.0
    n = len(coords) - 1  # Last point == first
    for i in range(n):
        x1 = coords[i][0] * cos_lat * 111320.0
        y1 = coords[i][1] * 111320.0
        x2 = coords[i + 1][0] * cos_lat * 111320.0
        y2 = coords[i + 1][1] * 111320.0
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def create_polygon(x: float, y: float, w: float, h: float) -> Dict:
    """Create a rectangular polygon geometry dict."""
    return {
        "type": "Polygon",
        "coordinates": [[
            [x, y],
            [x + w, y],
            [x + w, y + h],
            [x, y + h],
            [x, y],
        ]],
    }


def _convex_hull(points: List[Tuple[float, float]]) -> List[List[float]]:
    """Compute convex hull of 2D points using Andrew's monotone chain."""
    if len(points) < 3:
        return []
    pts = sorted(set((round(p[0], 7), round(p[1], 7)) for p in points))
    if len(pts) < 3:
        return []

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    return [[p[0], p[1]] for p in hull]


# ---------------------------------------------------------------------------
# Graph abstraction
# ---------------------------------------------------------------------------

class WalkGraph:
    """Lightweight weighted directed graph for walkable network analysis."""

    def __init__(self):
        self.nodes: Dict[int, Tuple[float, float]] = {}
        self.edges: Dict[int, List[Tuple[int, float]]] = {}
        self._next_node: int = 0
        self._node_map: Dict[Tuple[float, float], int] = {}

    def add_node(self, lon: float, lat: float) -> int:
        key = (round(lon, 7), round(lat, 7))
        if key in self._node_map:
            return self._node_map[key]
        nid = self._next_node
        self._next_node += 1
        self.nodes[nid] = (lon, lat)
        self.edges[nid] = []
        self._node_map[key] = nid
        return nid

    def add_edge(self, n1: int, n2: int, weight: float, bidirectional: bool = True):
        self.edges[n1].append((n2, weight))
        if bidirectional:
            self.edges[n2].append((n1, weight))

    def remove_edge(self, n1: int, n2: int):
        self.edges[n1] = [(t, w) for t, w in self.edges[n1] if t != n2]
        self.edges[n2] = [(t, w) for t, w in self.edges[n2] if t != n1]

    def dijkstra(self, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
        """Dijkstra shortest path from source. Returns (distances, predecessors)."""
        dist: Dict[int, float] = {source: 0.0}
        prev: Dict[int, Optional[int]] = {source: None}
        pq: List[Tuple[float, int]] = [(0.0, source)]
        visited = set()

        while pq:
            d, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            for v, w in self.edges.get(u, []):
                if v in visited:
                    continue
                nd = d + w
                if nd < dist.get(v, float('inf')):
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        return dist, prev

    def reachable_within(self, source: int, max_cost: float) -> Dict[int, float]:
        """Return all nodes reachable from source within max_cost."""
        dist, _ = self.dijkstra(source)
        return {n: d for n, d in dist.items() if d <= max_cost}

    def nearest_node(self, lon: float, lat: float) -> int:
        """Find the nearest graph node to a (lon, lat) point."""
        best_id = -1
        best_dist = float('inf')
        for nid, (nlon, nlat) in self.nodes.items():
            d = _haversine_distance(lon, lat, nlon, nlat)
            if d < best_dist:
                best_dist = d
                best_id = nid
        return best_id


# ---------------------------------------------------------------------------
# Network building
# ---------------------------------------------------------------------------

def build_walk_graph(network_path: Path,
                     barriers_path: Optional[Path] = None) -> WalkGraph:
    """Build a WalkGraph from a GeoJSON road network file."""
    with open(network_path, encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    if not features:
        raise ValueError(f"No features found in {network_path}")

    # Collect barrier segments
    barrier_segments = set()
    if barriers_path and barriers_path.exists():
        with open(barriers_path, encoding="utf-8") as f:
            barrier_data = json.load(f)
        for feat in barrier_data.get("features", []):
            geom = feat.get("geometry", {})
            if geom.get("type") == "LineString":
                coords = geom.get("coordinates", [])
                for i in range(1, len(coords)):
                    c1 = (round(coords[i - 1][0], 7), round(coords[i - 1][1], 7))
                    c2 = (round(coords[i][0], 7), round(coords[i][1], 7))
                    barrier_segments.add((c1, c2))
                    barrier_segments.add((c2, c1))

    graph = WalkGraph()
    edge_count = 0
    skipped = 0

    for feat in features:
        geom = feat.get("geometry", {})
        if geom.get("type") != "LineString":
            skipped += 1
            continue
        coords = geom.get("coordinates", [])
        if len(coords) < 2:
            skipped += 1
            continue

        props = feat.get("properties", {})
        highway = props.get("highway", "default")
        if isinstance(highway, list):
            highway = highway[0]
        speed = WALK_SPEEDS.get(highway, WALK_SPEEDS.get("default", 5))

        if speed <= 0:
            skipped += 1
            continue

        prev_nid = None
        for i in range(len(coords)):
            lon, lat = coords[i][0], coords[i][1]
            nid = graph.add_node(lon, lat)
            if prev_nid is not None:
                c1_key = (round(coords[i - 1][0], 7), round(coords[i - 1][1], 7))
                c2_key = (round(lon, 7), round(lat, 7))
                if (c1_key, c2_key) in barrier_segments:
                    prev_nid = nid
                    continue

                seg_len = _haversine_distance(coords[i - 1][0], coords[i - 1][1], lon, lat)
                cost = (seg_len / speed) * 60.0  # minutes
                graph.add_edge(prev_nid, nid, cost, bidirectional=True)
                edge_count += 1
            prev_nid = nid

    if edge_count == 0:
        raise ValueError("No valid edges built from network file")

    return graph


# ---------------------------------------------------------------------------
# Green space loading and validation
# ---------------------------------------------------------------------------

def load_green_spaces(green_sources_path: Path,
                      entrances_path: Optional[Path] = None) -> Dict[str, Any]:
    """Load green spaces from GeoJSON and validate entrances."""
    with open(green_sources_path, encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    if not features:
        raise ValueError(f"No green space features in {green_sources_path}")

    # Load entrances if provided
    entrance_points = []
    if entrances_path and entrances_path.exists():
        with open(entrances_path, encoding="utf-8") as f:
            ent_data = json.load(f)
        for feat in ent_data.get("features", []):
            geom = feat.get("geometry", {})
            if geom.get("type") == "Point":
                entrance_points.append((geom["coordinates"][0], geom["coordinates"][1]))

    green_spaces = []
    for feat in features:
        geom = feat.get("geometry", {})
        props = feat.get("properties", {})
        gtype = geom.get("type", "")

        if gtype == "Polygon":
            coords = geom.get("coordinates", [[]])[0]
        elif gtype == "MultiPolygon":
            coords = geom.get("coordinates", [[[]]])[0][0]
        else:
            continue

        if len(coords) < 4:
            continue

        area_m2 = _polygon_area_approx(coords)
        green_type = props.get("leisure", props.get("landuse", "default"))
        if isinstance(green_type, list):
            green_type = green_type[0]
        quality = GREEN_QUALITY.get(green_type, GREEN_QUALITY["default"])

        # Check for valid entrances if we have entrance data
        has_entrance = True
        if entrance_points:
            has_entrance = any(
                _point_near_polygon(ex, ey, coords, threshold_km=0.05)
                for ex, ey in entrance_points
            )

        centroid = _polygon_centroid(coords)
        green_spaces.append({
            "id": props.get("id", props.get("osm_id", len(green_spaces))),
            "type": green_type,
            "area_m2": round(area_m2, 2),
            "quality": quality,
            "centroid": centroid,
            "geometry": geom,
            "has_entrance": has_entrance,
        })

    if not green_spaces:
        raise ValueError("No valid green space polygons found")

    total_area = sum(g["area_m2"] for g in green_spaces)
    return {
        "green_spaces": green_spaces,
        "total": len(green_spaces),
        "total_area_m2": total_area,
    }


def _polygon_centroid(coords: List[List[float]]) -> List[float]:
    """Compute centroid of polygon ring."""
    n = len(coords) - 1  # Last == first
    if n < 1:
        return [0.0, 0.0]
    cx = sum(c[0] for c in coords[:n]) / n
    cy = sum(c[1] for c in coords[:n]) / n
    return [round(cx, 7), round(cy, 7)]


def _point_near_polygon(px: float, py: float, poly_coords: List[List[float]],
                        threshold_km: float = 0.05) -> bool:
    """Check if a point is within threshold distance of any polygon edge or inside it."""
    # First check if point is inside polygon (ray casting)
    if _point_in_polygon(px, py, poly_coords):
        return True
    # Then check distance to vertices
    for i in range(len(poly_coords) - 1):
        ex, ey = poly_coords[i]
        d = _haversine_distance(px, py, ex, ey)
        if d <= threshold_km:
            return True
    return False


def _point_in_polygon(px: float, py: float, poly_coords: List[List[float]]) -> bool:
    """Ray casting algorithm to check if point is inside polygon."""
    n = len(poly_coords) - 1  # Last point == first
    if n < 3:
        return False
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = poly_coords[i]
        xj, yj = poly_coords[j]
        if ((yi > py) != (yj > py)) and (px < (xj - xi) * (py - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside


# ---------------------------------------------------------------------------
# Population raster overlay
# ---------------------------------------------------------------------------

def load_population_raster(pop_raster_path: Path) -> Dict[str, Any]:
    """Load population raster and return metadata + data."""
    try:
        import rasterio
    except ImportError:
        return {"error": "rasterio not available"}

    with rasterio.open(pop_raster_path) as ds:
        pop_data = ds.read(1)
        transform = ds.transform
        nodata = ds.nodata
        crs = str(ds.crs)
        bounds = ds.bounds
        shape = pop_data.shape

    pop_valid = pop_data.astype(np.float64)
    if nodata is not None:
        pop_valid[pop_data == nodata] = 0
    pop_valid[pop_valid < 0] = 0

    return {
        "data": pop_valid,
        "transform": transform,
        "nodata": nodata,
        "crs": crs,
        "bounds": bounds,
        "shape": shape,
        "total_population": float(np.nansum(pop_valid)),
    }


def compute_population_in_service_area(graph: WalkGraph, covered_nodes: set,
                                       pop_info: Dict[str, Any]) -> Dict[str, Any]:
    """Compute population served by covered graph nodes."""
    if "error" in pop_info:
        return pop_info

    pop_data = pop_info["data"]
    transform = pop_info["transform"]
    shape = pop_info["shape"]

    try:
        import rasterio
    except ImportError:
        return {"error": "rasterio not available"}

    covered_mask = np.zeros(shape, dtype=bool)
    for nid in covered_nodes:
        lon, lat = graph.nodes[nid]
        try:
            row, col = rasterio.transform.rowcol(transform, lon, lat)
            if 0 <= row < shape[0] and 0 <= col < shape[1]:
                covered_mask[row, col] = True
        except Exception:
            continue

    pop_valid = pop_data.copy()
    total_pop = float(np.nansum(pop_valid))
    served_pop = float(np.nansum(pop_valid[covered_mask]))
    unserved_pop = total_pop - served_pop

    return {
        "total_population": round(total_pop, 2),
        "served_population": round(served_pop, 2),
        "unserved_population": round(unserved_pop, 2),
        "served_fraction": round(served_pop / total_pop, 4) if total_pop > 0 else 0,
    }


# ---------------------------------------------------------------------------
# Community metrics
# ---------------------------------------------------------------------------

def load_communities(communities_path: Path) -> Dict[str, Any]:
    """Load community boundaries from GeoJSON."""
    with open(communities_path, encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    if not features:
        raise ValueError(f"No features in {communities_path}")

    communities = []
    for feat in features:
        geom = feat.get("geometry", {})
        props = feat.get("properties", {})
        communities.append({
            "id": props.get("id", props.get("name", len(communities))),
            "name": props.get("name", props.get("id", f"community_{len(communities)}")),
            "geometry": geom,
            "population": props.get("population"),
            "properties": props,
        })

    return {"communities": communities, "total": len(communities)}


def compute_community_metrics(graph: WalkGraph, green_data: Dict,
                              communities_data: Dict,
                              walk_minutes: float,
                              pop_info: Optional[Dict] = None) -> Dict[str, Any]:
    """Compute per-community green space metrics."""
    green_spaces = green_data["green_spaces"]
    communities = communities_data["communities"]

    # For each community, find green spaces within walk_minutes
    community_metrics = []
    for comm in communities:
        comm_geom = comm["geometry"]
        if comm_geom.get("type") == "Polygon":
            coords = comm_geom.get("coordinates", [[]])[0]
        elif comm_geom.get("type") == "MultiPolygon":
            coords = comm_geom.get("coordinates", [[[]]])[0][0]
        else:
            continue

        centroid = _polygon_centroid(coords)
        comm_area_m2 = _polygon_area_approx(coords)

        # Population: use provided value or estimate from raster
        comm_pop = comm.get("population")
        if comm_pop is None and pop_info and "error" not in pop_info:
            comm_pop = _estimate_population_in_polygon(centroid, pop_info)

        # Find green spaces accessible within walk_minutes
        accessible_green = []
        total_green_area = 0.0
        weighted_quality_area = 0.0

        src = graph.nearest_node(centroid[0], centroid[1])
        dist, _ = graph.dijkstra(src)

        for gs in green_spaces:
            if not gs["has_entrance"]:
                continue
            gs_centroid = gs["centroid"]
            gs_node = graph.nearest_node(gs_centroid[0], gs_centroid[1])
            walk_time = dist.get(gs_node, float('inf'))
            if walk_time <= walk_minutes:
                accessible_green.append({
                    "id": gs["id"],
                    "area_m2": gs["area_m2"],
                    "quality": gs["quality"],
                    "walk_minutes": round(walk_time, 2),
                })
                total_green_area += gs["area_m2"]
                weighted_quality_area += gs["area_m2"] * gs["quality"]

        # Metrics
        green_per_capita = (total_green_area / comm_pop) if comm_pop and comm_pop > 0 else None
        green_coverage = (total_green_area / comm_area_m2) if comm_area_m2 > 0 else 0
        avg_quality = (weighted_quality_area / total_green_area) if total_green_area > 0 else 0

        community_metrics.append({
            "community_id": comm["id"],
            "name": comm["name"],
            "population": comm_pop,
            "area_m2": round(comm_area_m2, 2),
            "accessible_green_count": len(accessible_green),
            "total_green_area_m2": round(total_green_area, 2),
            "green_per_capita_m2": round(green_per_capita, 2) if green_per_capita is not None else None,
            "green_coverage_ratio": round(min(green_coverage, 1.0), 4),
            "avg_quality": round(avg_quality, 4),
            "green_spaces": accessible_green,
        })

    return {
        "community_metrics": community_metrics,
        "total_communities": len(community_metrics),
        "walk_minutes": walk_minutes,
    }


def _estimate_population_in_polygon(centroid: List[float],
                                    pop_info: Dict) -> Optional[float]:
    """Estimate population near a centroid point from raster."""
    try:
        import rasterio
    except ImportError:
        return None

    pop_data = pop_info["data"]
    transform = pop_info["transform"]
    shape = pop_info["shape"]

    try:
        row, col = rasterio.transform.rowcol(transform, centroid[0], centroid[1])
        if 0 <= row < shape[0] and 0 <= col < shape[1]:
            return float(pop_data[row, col])
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Equity metrics
# ---------------------------------------------------------------------------

def compute_equity_metrics(community_metrics: List[Dict],
                           metrics_list: List[str]) -> Dict[str, Any]:
    """Compute equity/summary metrics across communities."""
    results = {}

    # Extract values
    green_per_capita = [m["green_per_capita_m2"] for m in community_metrics
                        if m["green_per_capita_m2"] is not None]
    green_coverage = [m["green_coverage_ratio"] for m in community_metrics]
    populations = [m["population"] for m in community_metrics if m["population"] is not None]

    if "gini" in metrics_list and green_per_capita:
        results["gini_coefficient"] = round(_gini(green_per_capita), 4)

    if "coverage_rate" in metrics_list:
        covered = sum(1 for m in community_metrics if m["accessible_green_count"] > 0)
        results["coverage_rate"] = round(covered / len(community_metrics), 4) if community_metrics else 0

    if "per_capita_stats" in metrics_list and green_per_capita:
        results["per_capita_stats"] = {
            "mean": round(sum(green_per_capita) / len(green_per_capita), 2),
            "min": round(min(green_per_capita), 2),
            "max": round(max(green_per_capita), 2),
            "median": round(_median(green_per_capita), 2),
        }

    if "coverage_stats" in metrics_list and green_coverage:
        results["coverage_stats"] = {
            "mean": round(sum(green_coverage) / len(green_coverage), 4),
            "min": round(min(green_coverage), 4),
            "max": round(max(green_coverage), 4),
            "median": round(_median(green_coverage), 4),
        }

    if "disparity_ratio" in metrics_list and green_per_capita:
        sorted_vals = sorted(green_per_capita)
        n = len(sorted_vals)
        if n >= 4:
            q25 = sorted_vals[n // 4]
            q75 = sorted_vals[3 * n // 4]
            results["disparity_ratio"] = round(q75 / max(q25, 0.01), 4) if q75 > 0 else 0.0

    if "population_weighted_coverage" in metrics_list and populations and green_coverage:
        total_pop = sum(populations)
        if total_pop > 0:
            weighted = sum(m["green_coverage_ratio"] * (m["population"] or 0)
                           for m in community_metrics)
            results["population_weighted_coverage"] = round(weighted / total_pop, 4)

    if "total_green_area" in metrics_list:
        results["total_green_area_m2"] = round(
            sum(m["total_green_area_m2"] for m in community_metrics), 2)

    if "total_served_population" in metrics_list and populations:
        served_pop = sum(m["population"] or 0 for m in community_metrics
                         if m["accessible_green_count"] > 0)
        results["total_served_population"] = round(served_pop, 2)

    results["metrics_computed"] = metrics_list
    return results


def _gini(values: List[float]) -> float:
    """Compute Gini coefficient."""
    if not values or len(values) < 2:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    total = sum(sorted_vals)
    if total == 0:
        return 0.0
    numerator = sum((2 * (i + 1) - n - 1) * v for i, v in enumerate(sorted_vals))
    return numerator / (n * total)


def _median(values: List[float]) -> float:
    """Compute median of a list."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


# ---------------------------------------------------------------------------
# Service area computation
# ---------------------------------------------------------------------------

def compute_green_service_areas(graph: WalkGraph, green_data: Dict,
                                walk_minutes: float) -> Dict[str, Any]:
    """Compute service areas (isochrones) from green space entrances."""
    green_spaces = green_data["green_spaces"]
    service_areas = []
    # Max distance from green space centroid to nearest network node (km)
    MAX_CONNECT_DISTANCE_KM = 0.5

    for gs in green_spaces:
        if not gs["has_entrance"]:
            continue
        centroid = gs["centroid"]
        src = graph.nearest_node(centroid[0], centroid[1])
        # Skip if green space is too far from any network node
        src_lon, src_lat = graph.nodes[src]
        connect_dist = _haversine_distance(centroid[0], centroid[1], src_lon, src_lat)
        if connect_dist > MAX_CONNECT_DISTANCE_KM:
            continue
        reachable = graph.reachable_within(src, walk_minutes)

        if not reachable:
            continue

        # Build convex hull of reachable nodes + green space centroid
        points = [(centroid[0], centroid[1])]
        for nid in reachable:
            nlon, nlat = graph.nodes[nid]
            points.append((nlon, nlat))

        hull = _convex_hull(points)
        if hull and len(hull) >= 3:
            service_areas.append({
                "green_space_id": gs["id"],
                "green_type": gs["type"],
                "walk_minutes": walk_minutes,
                "node_count": len(reachable),
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [hull],
                },
            })

    return {
        "service_areas": service_areas,
        "total": len(service_areas),
        "walk_minutes": walk_minutes,
    }


# ---------------------------------------------------------------------------
# Priority communities
# ---------------------------------------------------------------------------

def identify_priority_communities(community_metrics: List[Dict],
                                  green_data: Dict) -> Dict[str, Any]:
    """Identify communities with lowest green access (highest priority)."""
    # Sort by green_per_capita (ascending), then by population (descending)
    scored = []
    for m in community_metrics:
        gpc = m["green_per_capita_m2"] if m["green_per_capita_m2"] is not None else 0
        pop = m["population"] or 0
        # Priority score: higher = more priority (low green, high population)
        priority_score = (1.0 / max(gpc, 0.01)) * math.log1p(pop)
        scored.append({**m, "priority_score": round(priority_score, 4)})

    scored.sort(key=lambda x: x["priority_score"], reverse=True)

    # Top 30% are priority
    n_priority = max(1, len(scored) // 3)
    priority = scored[:n_priority]

    return {
        "priority_communities": priority,
        "total_priority": len(priority),
        "threshold_score": priority[-1]["priority_score"] if priority else 0,
    }


# ---------------------------------------------------------------------------
# Candidate site evaluation
# ---------------------------------------------------------------------------

def evaluate_candidate_sites(graph: WalkGraph, candidates_path: Path,
                             green_data: Dict, communities_data: Dict,
                             walk_minutes: float) -> Dict[str, Any]:
    """Evaluate potential new green space sites for impact."""
    with open(candidates_path, encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    if not features:
        raise ValueError(f"No candidate features in {candidates_path}")

    green_spaces = green_data["green_spaces"]
    communities = communities_data["communities"]
    evaluations = []

    for feat in features:
        geom = feat.get("geometry", {})
        props = feat.get("properties", {})

        if geom.get("type") == "Point":
            cx, cy = geom["coordinates"][0], geom["coordinates"][1]
        elif geom.get("type") == "Polygon":
            coords = geom.get("coordinates", [[]])[0]
            centroid = _polygon_centroid(coords)
            cx, cy = centroid[0], centroid[1]
        else:
            continue

        candidate_area = props.get("area_m2", 1000.0)

        # Count newly served communities
        newly_served = 0
        additional_population = 0.0

        src = graph.nearest_node(cx, cy)
        dist, _ = graph.dijkstra(src)

        for comm in communities:
            comm_geom = comm["geometry"]
            if comm_geom.get("type") == "Polygon":
                coords = comm_geom.get("coordinates", [[]])[0]
            elif comm_geom.get("type") == "MultiPolygon":
                coords = comm_geom.get("coordinates", [[[]]])[0][0]
            else:
                continue
            comm_centroid = _polygon_centroid(coords)
            comm_node = graph.nearest_node(comm_centroid[0], comm_centroid[1])
            walk_time = dist.get(comm_node, float('inf'))

            if walk_time <= walk_minutes:
                # Check if this community currently has NO green access
                comm_pop = comm.get("population") or 0
                has_access = any(
                    _haversine_distance(gs["centroid"][0], gs["centroid"][1],
                                        comm_centroid[0], comm_centroid[1]) < 0.5
                    for gs in green_spaces
                )
                if not has_access:
                    newly_served += 1
                    additional_population += comm_pop

        evaluations.append({
            "candidate_id": props.get("id", len(evaluations)),
            "area_m2": candidate_area,
            "newly_served_communities": newly_served,
            "additional_population_served": round(additional_population, 2),
            "coordinates": [cx, cy],
        })

    evaluations.sort(key=lambda x: x["additional_population_served"], reverse=True)

    return {
        "evaluations": evaluations,
        "total_evaluated": len(evaluations),
    }


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------

def write_service_areas_geojson(service_areas: List[Dict], output_path: Path) -> None:
    """Write green service areas as GeoJSON."""
    features = []
    for sa in service_areas:
        features.append({
            "type": "Feature",
            "geometry": sa["geometry"],
            "properties": {
                "green_space_id": sa["green_space_id"],
                "green_type": sa["green_type"],
                "walk_minutes": sa["walk_minutes"],
                "node_count": sa["node_count"],
            },
        })
    geojson = {"type": "FeatureCollection", "features": features}
    output_path.write_text(json.dumps(geojson, default=str), encoding="utf-8")


def write_community_metrics_csv(community_metrics: List[Dict], output_path: Path) -> None:
    """Write community metrics as CSV."""
    if not community_metrics:
        return
    headers = ["community_id", "name", "population", "area_m2",
               "accessible_green_count", "total_green_area_m2",
               "green_per_capita_m2", "green_coverage_ratio", "avg_quality"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for m in community_metrics:
            writer.writerow([
                m["community_id"], m["name"], m["population"], m["area_m2"],
                m["accessible_green_count"], m["total_green_area_m2"],
                m["green_per_capita_m2"], m["green_coverage_ratio"], m["avg_quality"],
            ])


def write_priority_communities_geojson(priority: List[Dict], output_path: Path) -> None:
    """Write priority communities as GeoJSON."""
    features = []
    for p in priority:
        # Reconstruct simple point geometry from centroid
        gs = p.get("green_spaces", [])
        # Use community centroid approximation
        features.append({
            "type": "Feature",
            "geometry": create_polygon(0, 0, 0.001, 0.001),  # Placeholder
            "properties": {
                "community_id": p["community_id"],
                "name": p["name"],
                "population": p["population"],
                "green_per_capita_m2": p["green_per_capita_m2"],
                "green_coverage_ratio": p["green_coverage_ratio"],
                "priority_score": p["priority_score"],
            },
        })
    geojson = {"type": "FeatureCollection", "features": features}
    output_path.write_text(json.dumps(geojson, default=str), encoding="utf-8")


def write_equity_summary(equity: Dict, output_path: Path) -> None:
    """Write equity summary as JSON."""
    output_path.write_text(json.dumps(equity, default=str, ensure_ascii=False, indent=2),
                          encoding="utf-8")


def write_scenario_report(report: Dict, output_path: Path) -> None:
    """Write scenario report as JSON (placeholder for PDF)."""
    output_path.with_suffix(".json").write_text(
        json.dumps(report, default=str, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Manifest and QA
# ---------------------------------------------------------------------------

def write_request_manifest(args: argparse.Namespace, output_dir: Path) -> None:
    """Write request manifest."""
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "place": args.place,
        "bbox": args.bbox,
        "aoi_file": args.aoi_file,
        "green_sources": args.green_sources,
        "population": args.population,
        "walk_minutes": args.walk_minutes,
        "network_mode": args.network_mode,
        "equity_metrics": args.equity_metrics.split(",") if args.equity_metrics else ["gini", "coverage_rate"],
        "candidate_sites": args.candidate_sites,
    }
    (output_dir / "request.json").write_text(
        json.dumps(manifest, default=str, ensure_ascii=False, indent=2), encoding="utf-8")


def write_dataset_manifest(green_data: Dict, communities_data: Dict,
                           pop_info: Optional[Dict], output_dir: Path) -> None:
    """Write dataset manifest."""
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "green_spaces": {
            "total": green_data["total"],
            "total_area_m2": green_data["total_area_m2"],
            "types": list(set(gs["type"] for gs in green_data["green_spaces"])),
        },
        "communities": {
            "total": communities_data["total"],
        },
        "population": {
            "total": pop_info.get("total_population") if pop_info and "error" not in pop_info else None,
            "crs": pop_info.get("crs") if pop_info else None,
        },
    }
    (output_dir / "dataset-manifest.json").write_text(
        json.dumps(manifest, default=str, ensure_ascii=False, indent=2), encoding="utf-8")


def write_output_manifest(results: Dict, output_dir: Path) -> None:
    """Write output manifest."""
    manifest = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "results": results,
        "outputs": [
            "green_service_areas.geojson",
            "community_metrics.csv",
            "equity_summary.json",
            "priority_communities.geojson",
            "scenario_report.pdf",
        ],
    }
    (output_dir / "output-manifest.json").write_text(
        json.dumps(manifest, default=str, ensure_ascii=False, indent=2), encoding="utf-8")


def write_qa_report(qa: Dict, output_dir: Path) -> None:
    """Write QA report."""
    (output_dir / "qa.json").write_text(
        json.dumps(qa, default=str, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main workflow
# ---------------------------------------------------------------------------

def run_analysis(args: argparse.Namespace) -> int:
    """Main analysis workflow."""
    output_dir = Path(args.output_dir) if args.output_dir else Path("uge-output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parse walk minutes
    walk_minutes = float(args.walk_minutes) if args.walk_minutes else 10.0

    # Parse equity metrics
    equity_metrics = args.equity_metrics.split(",") if args.equity_metrics else [
        "gini", "coverage_rate", "per_capita_stats", "coverage_stats",
    ]

    # Resolve input paths
    green_sources_path = Path(args.green_sources) if args.green_sources else None
    network_path = Path(args.network) if args.network else None
    population_path = Path(args.population) if args.population else None
    communities_path = Path(args.communities) if args.communities else None
    entrances_path = Path(args.entrances) if args.entrances else None
    barriers_path = Path(args.barriers) if args.barriers else None
    candidates_path = Path(args.candidate_sites) if args.candidate_sites else None

    # Validate required inputs
    if not green_sources_path or not green_sources_path.exists():
        print("ERROR: Green sources file not found", file=sys.stderr)
        return EXIT_ARG
    if not network_path or not network_path.exists():
        print("ERROR: Network file not found", file=sys.stderr)
        return EXIT_ARG
    if not communities_path or not communities_path.exists():
        print("ERROR: Communities file not found", file=sys.stderr)
        return EXIT_ARG

    results = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "walk_minutes": walk_minutes,
        "equity_metrics": equity_metrics,
    }
    qa = {
        "checks": [],
        "warnings": [],
        "status": "pass",
    }

    # Write request manifest
    write_request_manifest(args, output_dir)

    # Build walk graph
    print("Building walk network graph...")
    try:
        graph = build_walk_graph(network_path, barriers_path)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return EXIT_VALIDATION
    print(f"  Nodes: {len(graph.nodes)}")
    results["network_nodes"] = len(graph.nodes)

    # Load green spaces
    print("Loading green spaces...")
    try:
        green_data = load_green_spaces(green_sources_path, entrances_path)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return EXIT_VALIDATION
    print(f"  Green spaces: {green_data['total']}, "
          f"Total area: {green_data['total_area_m2']:.0f} m²")
    results["green_spaces"] = green_data["total"]
    results["total_green_area_m2"] = green_data["total_area_m2"]

    # QA: check green spaces without entrances
    no_entrance = [gs for gs in green_data["green_spaces"] if not gs["has_entrance"]]
    if no_entrance:
        qa["warnings"].append(
            f"{len(no_entrance)} green spaces lack verified entrances")

    # Load communities
    print("Loading communities...")
    try:
        communities_data = load_communities(communities_path)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return EXIT_VALIDATION
    print(f"  Communities: {communities_data['total']}")
    results["communities"] = communities_data["total"]

    # Load population raster (optional)
    pop_info = None
    if population_path and population_path.exists():
        pop_info = load_population_raster(population_path)
        if "error" not in pop_info:
            print(f"  Population raster: {pop_info['total_population']:,.0f} total")
            results["total_population"] = pop_info["total_population"]
        else:
            qa["warnings"].append("Population raster could not be loaded")
    else:
        qa["warnings"].append("No population raster provided")

    # Write dataset manifest
    write_dataset_manifest(green_data, communities_data, pop_info, output_dir)

    # Compute service areas
    print("Computing green service areas...")
    service_areas = compute_green_service_areas(graph, green_data, walk_minutes)
    results["service_areas"] = service_areas["total"]
    write_service_areas_geojson(service_areas["service_areas"],
                                output_dir / "green_service_areas.geojson")
    print(f"  Service areas: {service_areas['total']}")

    # Compute community metrics
    print("Computing community metrics...")
    comm_metrics = compute_community_metrics(
        graph, green_data, communities_data, walk_minutes, pop_info
    )
    results["community_metrics"] = comm_metrics["total_communities"]
    write_community_metrics_csv(comm_metrics["community_metrics"],
                                output_dir / "community_metrics.csv")
    print(f"  Communities analyzed: {comm_metrics['total_communities']}")

    # Compute equity metrics
    print("Computing equity metrics...")
    equity = compute_equity_metrics(comm_metrics["community_metrics"], equity_metrics)
    results["equity"] = equity
    write_equity_summary(equity, output_dir / "equity_summary.json")
    if "gini_coefficient" in equity:
        print(f"  Gini coefficient: {equity['gini_coefficient']}")
    if "coverage_rate" in equity:
        print(f"  Coverage rate: {equity['coverage_rate']:.1%}")

    # Identify priority communities
    print("Identifying priority communities...")
    priority = identify_priority_communities(comm_metrics["community_metrics"], green_data)
    results["priority_communities"] = priority["total_priority"]
    write_priority_communities_geojson(priority["priority_communities"],
                                       output_dir / "priority_communities.geojson")
    print(f"  Priority communities: {priority['total_priority']}")

    # Evaluate candidate sites
    if candidates_path and candidates_path.exists():
        print("Evaluating candidate sites...")
        try:
            candidates_result = evaluate_candidate_sites(
                graph, candidates_path, green_data, communities_data, walk_minutes
            )
            results["candidate_evaluations"] = candidates_result["total_evaluated"]
            write_scenario_report(candidates_result, output_dir / "scenario_report.pdf")
            print(f"  Candidates evaluated: {candidates_result['total_evaluated']}")
        except ValueError as e:
            qa["warnings"].append(f"Candidate evaluation failed: {e}")

    # Population coverage
    if pop_info and "error" not in pop_info:
        all_covered = set()
        for gs in green_data["green_spaces"]:
            if not gs["has_entrance"]:
                continue
            src = graph.nearest_node(gs["centroid"][0], gs["centroid"][1])
            reachable = graph.reachable_within(src, walk_minutes)
            all_covered.update(reachable.keys())

        pop_coverage = compute_population_in_service_area(graph, all_covered, pop_info)
        results["population_coverage"] = pop_coverage
        if "error" not in pop_coverage:
            print(f"  Population served: {pop_coverage['served_fraction']:.1%}")

    # Final QA
    qa["checks"].append("green_spaces_loaded")
    qa["checks"].append("network_built")
    qa["checks"].append("service_areas_computed")
    qa["checks"].append("community_metrics_computed")
    qa["checks"].append("equity_metrics_computed")
    if qa["warnings"]:
        qa["status"] = "pass_with_warnings"

    # Write manifests and QA
    write_output_manifest(results, output_dir)
    write_qa_report(qa, output_dir)

    print(f"\nOutput: {output_dir}")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(description="Urban Green Equity Analysis")
    parser.add_argument("--place", help="Place name for area of interest")
    parser.add_argument("--bbox", nargs=4, type=float, metavar=("XMIN", "YMIN", "XMAX", "YMAX"),
                        help="Bounding box (EPSG:4326)")
    parser.add_argument("--aoi-file", help="AOI polygon file (GeoJSON)")
    parser.add_argument("--green-sources", required=True,
                        help="Green spaces GeoJSON file")
    parser.add_argument("--network", required=True,
                        help="Walkable road network GeoJSON file")
    parser.add_argument("--communities", required=True,
                        help="Community boundaries GeoJSON file")
    parser.add_argument("--population", help="Population raster (GeoTIFF)")
    parser.add_argument("--entrances", help="Green space entrances GeoJSON file")
    parser.add_argument("--barriers", help="Walk barriers GeoJSON file")
    parser.add_argument("--walk-minutes", default="10",
                        help="Walk time threshold in minutes (default: 10)")
    parser.add_argument("--network-mode", default="walk",
                        choices=["walk"], help="Network mode (default: walk)")
    parser.add_argument("--equity-metrics",
                        help="Comma-separated equity metrics (gini,coverage_rate,per_capita_stats,coverage_stats,disparity_ratio,population_weighted_coverage,total_green_area,total_served_population)")
    parser.add_argument("--candidate-sites", help="Candidate new green space sites GeoJSON")
    parser.add_argument("--output-dir", "-o", default="uge-output",
                        help="Output directory")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    args = parser.parse_args()

    try:
        sys.exit(run_analysis(args))
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(EXIT_PROCESSING)


if __name__ == "__main__":
    main()
