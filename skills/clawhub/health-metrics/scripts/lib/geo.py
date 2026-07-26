"""Route geometry helpers: haversine distance, Douglas-Peucker simplification,
per-km split calculation. Pure stdlib, no dependencies."""
import math

EARTH_RADIUS_M = 6371000.0


def haversine_m(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlambda / 2) ** 2
    return 2 * EARTH_RADIUS_M * math.asin(math.sqrt(a))


def _to_local_meters(lat, lon, lat0, lon0):
    """Equirectangular projection to meters, accurate enough at route scale."""
    m_per_deg_lat = 111320.0
    m_per_deg_lon = 111320.0 * math.cos(math.radians(lat0))
    return (lon - lon0) * m_per_deg_lon, (lat - lat0) * m_per_deg_lat


def _perp_distance(pt, start, end):
    (lat0, lon0), (lat1, lon1) = start, end
    lat, lon = pt
    x, y = _to_local_meters(lat, lon, lat0, lon0)
    x1, y1 = _to_local_meters(lat1, lon1, lat0, lon0)
    denom = x1 * x1 + y1 * y1
    if denom < 1e-9:
        return math.hypot(x, y)
    t = max(0.0, min(1.0, (x * x1 + y * y1) / denom))
    px, py = x1 * t, y1 * t
    return math.hypot(x - px, y - py)


def douglas_peucker(points, epsilon_m=8.0):
    """points: list of (lat, lon). Returns a simplified subsequence preserving shape."""
    if len(points) < 3:
        return points
    start, end = points[0], points[-1]
    max_dist, max_idx = 0.0, 0
    for i in range(1, len(points) - 1):
        d = _perp_distance(points[i], start, end)
        if d > max_dist:
            max_dist, max_idx = d, i
    if max_dist > epsilon_m:
        left = douglas_peucker(points[:max_idx + 1], epsilon_m)
        right = douglas_peucker(points[max_idx:], epsilon_m)
        return left[:-1] + right
    return [start, end]


def km_splits(route):
    """route: list of dicts with lat, lon, timestamp (ISO string, sortable).
    Returns list of dicts: {km, split_seconds, pace_min_per_km}."""
    if len(route) < 2:
        return []
    splits = []
    cum_dist = 0.0
    last_km = 0
    split_start_ts = route[0]["ts"]
    for prev, cur in zip(route, route[1:]):
        cum_dist += haversine_m(prev["lat"], prev["lon"], cur["lat"], cur["lon"])
        km = int(cum_dist // 1000)
        if km > last_km:
            elapsed = cur["ts"] - split_start_ts
            splits.append({"km": km, "split_seconds": elapsed, "pace_min_per_km": elapsed / 60})
            split_start_ts = cur["ts"]
            last_km = km
    return splits
