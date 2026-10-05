# Source-derived implementation for this package; see source-map.json.
from __future__ import annotations

import json
import math
import re
from typing import Any, Callable, Dict, List, Mapping, Sequence
CONTRACTS = {'cap_12_route_to_dispatch': {'upstream': {'input_schema': {'type': 'object', 'required': ['type', 'features', 'route_id'], 'properties': {'type': {'type': 'string', 'minLength': 1}, 'features': {'type': 'array', 'items': {'type': 'object'}}, 'route_id': {'type': 'string', 'minLength': 1}}, 'additionalProperties': True}, 'output_schema': {'type': 'object', 'required': ['route_id', 'ordered_stops', 'leg_km', 'total_km'], 'properties': {'route_id': {'type': 'string', 'minLength': 1}, 'ordered_stops': {'type': 'array', 'items': {'type': 'string'}}, 'leg_km': {'type': 'array', 'items': {'type': 'number'}}, 'total_km': {'type': 'number'}}, 'additionalProperties': True}, 'sample_input': {'type': 'FeatureCollection', 'route_id': 'ROUTE-LIMA-3957', 'depot': [121.47, 31.23], 'features': [{'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [121.48, 31.24]}, 'properties': {'stop_id': 'stop-a'}}, {'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [121.5, 31.25]}, 'properties': {'stop_id': 'stop-b'}}]}}}}

def _require_text(value: Any, label: str='value') -> str:
    if isinstance(value, bytes):
        text = value.decode('utf-8')
    elif isinstance(value, str):
        text = value
    else:
        raise TypeError('{} must be text'.format(label))
    if not text.strip():
        raise ValueError('{} must not be empty'.format(label))
    return text

def _as_mapping(value: Any, label: str='value') -> Dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    text = _require_text(value, label)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError('{} must be a JSON object'.format(label)) from exc
    if not isinstance(parsed, dict):
        raise ValueError('{} must decode to an object'.format(label))
    return parsed

def _extract_prefixed(text: str, prefix: str) -> str:
    pattern = '(?<![A-Z0-9])(' + re.escape(prefix) + '-[A-Z0-9]+(?:-[A-Z0-9]+)+)(?![A-Z0-9])'
    match = re.search(pattern, text.upper())
    if not match:
        raise ValueError('no {} reference found'.format(prefix))
    return match.group(1)

def _haversine_km(left: Sequence[float], right: Sequence[float]) -> float:
    lon1, lat1 = (math.radians(float(left[0])), math.radians(float(left[1])))
    lon2, lat2 = (math.radians(float(right[0])), math.radians(float(right[1])))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
    return 6371.0088 * 2.0 * math.asin(min(1.0, math.sqrt(a)))

def _plan_geojson_route(value: Any) -> Dict[str, Any]:
    data = _as_mapping(value, 'GeoJSON route')
    if data.get('type') != 'FeatureCollection' or not isinstance(data.get('features'), list):
        raise ValueError('route input must be a GeoJSON FeatureCollection')
    route_id = _extract_prefixed(str(data.get('route_id', '')), 'ROUTE')
    stops: List[Dict[str, Any]] = []
    for index, feature in enumerate(data['features']):
        if not isinstance(feature, Mapping):
            raise ValueError('route feature must be an object')
        geometry = feature.get('geometry', {})
        properties = feature.get('properties', {})
        if not isinstance(geometry, Mapping) or geometry.get('type') != 'Point':
            raise ValueError('route features must use Point geometry')
        coords = geometry.get('coordinates')
        if not isinstance(coords, list) or len(coords) < 2:
            raise ValueError('route Point requires longitude and latitude')
        lon, lat = (float(coords[0]), float(coords[1]))
        if not -180.0 <= lon <= 180.0 or not -90.0 <= lat <= 90.0:
            raise ValueError('route coordinate is outside longitude/latitude bounds')
        stop_id = str(properties.get('stop_id', 'stop-{}'.format(index + 1)))
        stops.append({'stop_id': stop_id, 'coordinates': [lon, lat]})
    if not stops:
        raise ValueError('route requires at least one stop')
    depot = data.get('depot', stops[0]['coordinates'])
    if not isinstance(depot, list) or len(depot) < 2:
        raise ValueError('depot must contain longitude and latitude')
    current = [float(depot[0]), float(depot[1])]
    remaining = list(stops)
    ordered: List[Dict[str, Any]] = []
    legs: List[float] = []
    while remaining:
        next_stop = min(remaining, key=lambda item: (_haversine_km(current, item['coordinates']), item['stop_id']))
        distance = _haversine_km(current, next_stop['coordinates'])
        legs.append(round(distance, 3))
        ordered.append(next_stop)
        current = next_stop['coordinates']
        remaining.remove(next_stop)
    return {'route_id': route_id, 'ordered_stops': [item['stop_id'] for item in ordered], 'leg_km': legs, 'total_km': round(sum(legs), 3)}

def _up_cap12(value: Any) -> Dict[str, Any]:
    return _plan_geojson_route(value)
_UPSTREAM_EXECUTORS: Dict[str, Callable[[Any], Any]] = {'cap_12_route_to_dispatch': _up_cap12}

def execute(variant_id: str, role: str, supplied_value: Any) -> Any:
    """Run one pure transformation for a capability-splitting role."""
    if variant_id not in CONTRACTS:
        raise KeyError('unknown capability variant: {}'.format(variant_id))
    executor = _UPSTREAM_EXECUTORS[variant_id]
    result = executor(supplied_value)
    if role == 'downstream' and result == supplied_value:
        raise RuntimeError('downstream transformation returned its input unchanged')
    return result
