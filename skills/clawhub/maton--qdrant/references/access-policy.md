# Qdrant access policy

An access policy limits which endpoints Qdrant connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/qdrant#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Qdrant: its 34 read-only endpoints. Endpoints Maton has found to return credentials, start jobs, or spend credits are left out; a few reads that can change state or return a secret depending on their parameters stay in, and their descriptions say how. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create qdrant --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "aliases"},
    {"method": "GET", "path": "collections/{id}/aliases"},
    {"method": "GET", "path": "issues"},
    {"method": "GET", "path": "collections"},
    {"method": "GET", "path": "collections/{id}"},
    {"method": "GET", "path": "collections/{id}/exists"},
    {"method": "GET", "path": "collections/{id}/optimizations"},
    {"method": "GET", "path": "cluster"},
    {"method": "GET", "path": "cluster/telemetry"},
    {"method": "GET", "path": "collections/{id}/cluster"},
    {"method": "GET", "path": "collections/{id}/shards"},
    {"method": "POST", "path": "collections/{id}/facet"},
    {"method": "POST", "path": "collections/{id}/points"},
    {"method": "POST", "path": "collections/{id}/points/count"},
    {"method": "POST", "path": "collections/{id}/points/scroll"},
    {"method": "GET", "path": "collections/{id}/points/{id}"},
    {"method": "GET", "path": "quotas"},
    {"method": "POST", "path": "collections/{id}/points/query"},
    {"method": "POST", "path": "collections/{id}/points/query/batch"},
    {"method": "POST", "path": "collections/{id}/points/query/groups"},
    {"method": "POST", "path": "collections/{id}/points/search/matrix/offsets"},
    {"method": "POST", "path": "collections/{id}/points/search/matrix/pairs"},
    {"method": "GET", "path": "healthz"},
    {"method": "GET", "path": "livez"},
    {"method": "GET", "path": "metrics"},
    {"method": "GET", "path": "readyz"},
    {"method": "GET", "path": "telemetry"},
    {"method": "GET", "path": "collections/{id}/shards/{id}/snapshot"},
    {"method": "GET", "path": "collections/{id}/shards/{id}/snapshots"},
    {"method": "GET", "path": "collections/{id}/shards/{id}/snapshots/{id}"},
    {"method": "GET", "path": "collections/{id}/snapshots"},
    {"method": "GET", "path": "collections/{id}/snapshots/{id}"},
    {"method": "GET", "path": "snapshots"},
    {"method": "GET", "path": "snapshots/{id}"}
  ],
  "deny": []
}
```

## Endpoints

The Qdrant endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | aliases | read | aliases | List collections aliases. |
| POST | collections/aliases | write | aliases | Update aliases of the collections. |
| GET | collections/{id}/aliases | read | aliases | List aliases for collection. |
| DELETE | issues | write | beta | Clear issues. |
| GET | issues | read | beta | Get issues. |
| GET | collections | read | collections | List collections. |
| DELETE | collections/{id} | write | collections | Delete collection. |
| GET | collections/{id} | read | collections | Collection info. |
| PATCH | collections/{id} | write | collections | Update collection parameters. |
| PUT | collections/{id} | write | collections | Create collection. |
| GET | collections/{id}/exists | read | collections | Check the existence of a collection. |
| GET | collections/{id}/optimizations | read | collections | Get optimization progress. |
| DELETE | collections/{id}/vectors/{id} | write | collections | Delete named vector. |
| PUT | collections/{id}/vectors/{id} | write | collections | Create named vector. |
| GET | cluster | read | distributed | Get cluster status info. |
| DELETE | cluster/peer/{id} | write | distributed | Remove peer from the cluster. |
| POST | cluster/recover | write | distributed | Tries to recover current peer Raft state. |
| GET | cluster/telemetry | read | distributed | Collect cluster telemetry data. |
| GET | collections/{id}/cluster | read | distributed | Collection cluster info. |
| POST | collections/{id}/cluster | write | distributed | Update collection cluster setup. |
| GET | collections/{id}/shards | read | distributed | List shard keys. |
| PUT | collections/{id}/shards | write | distributed | Create shard key. |
| POST | collections/{id}/shards/delete | write | distributed | Delete shard key. |
| PUT | collections/{id}/index | write | indexes | Create index for field in collection. |
| DELETE | collections/{id}/index/{id} | write | indexes | Delete index for field in collection. |
| POST | collections/{id}/facet | read | points | Facet a payload key with a given filter. |
| POST | collections/{id}/points | read | points | Get points. |
| PUT | collections/{id}/points | write | points | Upsert points. |
| POST | collections/{id}/points/batch | write | points | Batch update points. |
| POST | collections/{id}/points/count | read | points | Count points. |
| POST | collections/{id}/points/delete | write | points | Delete points. |
| POST | collections/{id}/points/payload | write | points | Set payload. |
| PUT | collections/{id}/points/payload | write | points | Overwrite payload. |
| POST | collections/{id}/points/payload/clear | write | points | Clear payload. |
| POST | collections/{id}/points/payload/delete | write | points | Delete payload. |
| POST | collections/{id}/points/scroll | read | points | Scroll points. |
| PUT | collections/{id}/points/vectors | write | points | Update vectors. |
| POST | collections/{id}/points/vectors/delete | write | points | Delete vectors. |
| GET | collections/{id}/points/{id} | read | points | Get point. |
| GET | quotas | read | quotas | Get global quotas. |
| PUT | quotas | write | quotas | Set global quotas. |
| POST | collections/{id}/points/query | read | search | Query points. |
| POST | collections/{id}/points/query/batch | read | search | Query points in batch. |
| POST | collections/{id}/points/query/groups | read | search | Query points, grouped by a given payload field. |
| POST | collections/{id}/points/search/matrix/offsets | read | search | Search points matrix distance offsets. |
| POST | collections/{id}/points/search/matrix/pairs | read | search | Search points matrix distance pairs. |
| GET | healthz | read | service | Kubernetes healthz endpoint. |
| GET | livez | read | service | Kubernetes livez endpoint. |
| GET | metrics | read | service | Collect Prometheus metrics data. |
| GET | readyz | read | service | Kubernetes readyz endpoint. |
| GET | telemetry | read | service | Collect telemetry data. |
| GET | collections/{id}/shards/{id}/snapshot | read | snapshots | Download shard snapshot. |
| GET | collections/{id}/shards/{id}/snapshots | read | snapshots | List shards snapshots for a collection. |
| POST | collections/{id}/shards/{id}/snapshots | write | snapshots | Create shard snapshot. |
| PUT | collections/{id}/shards/{id}/snapshots/recover | write | snapshots | Recover from a snapshot. |
| POST | collections/{id}/shards/{id}/snapshots/upload | write | snapshots | Recover shard from an uploaded snapshot. |
| DELETE | collections/{id}/shards/{id}/snapshots/{id} | write | snapshots | Delete shard snapshot. |
| GET | collections/{id}/shards/{id}/snapshots/{id} | read | snapshots | Download collection snapshot. |
| GET | collections/{id}/snapshots | read | snapshots | List collection snapshots. |
| POST | collections/{id}/snapshots | write | snapshots | Create collection snapshot. |
| PUT | collections/{id}/snapshots/recover | write | snapshots | Recover from a snapshot. |
| POST | collections/{id}/snapshots/upload | write | snapshots | Recover from an uploaded snapshot. |
| DELETE | collections/{id}/snapshots/{id} | write | snapshots | Delete collection snapshot. |
| GET | collections/{id}/snapshots/{id} | read | snapshots | Download collection snapshot. |
| GET | snapshots | read | snapshots | List of storage snapshots. |
| POST | snapshots | write | snapshots | Create storage snapshot. |
| DELETE | snapshots/{id} | write | snapshots | Delete storage snapshot. |
| GET | snapshots/{id} | read | snapshots | Download storage snapshot. |
