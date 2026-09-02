---
name: huawei-cloud-vpcep-name-list
description: >-
  Query Huawei Cloud VPCEP (VPC Endpoint) names by keyword, and list all
  VPC Endpoints across a region. Provides read-only name lookup, fuzzy
  name filtering, and paginated listing for daily inspection and resource
  management. Triggers include: VPCEP list, list VPCEP endpoints,
  query VPCEP names, VPCEP endpoint name, find VPCEP endpoint,
  VPCEP name lookup, VPCEP endpoint list, VPC endpoint names,
  endpoint name query, 查询VPCEP名称, VPCEP端点名称, VPC端点名称,
  VPCEP列表, VPCEP端点列表, 查询端点名称.
tags:
  - huawei-cloud
  - vpcep
  - list
  - endpoint
  - network
---

# Huawei Cloud VPCEP Name List Skill

## Overview

This skill provides read-only name-query capabilities for Huawei Cloud VPCEP (VPC Endpoint
Service). It lists all VPC Endpoints in a region, supports fuzzy name matching via the
`endpoint_service_name` parameter, and paginated queries with `limit`/`offset`. It is
designed for quick name lookups, inventory reporting, and daily endpoint inspection.

**Architecture:**

```
Agent → hcloud CLI (primary) → Huawei Cloud VPCEP API
       ↘ Python SDK (fallback) ↗
```

**Applicable Scenarios:**

- List all VPCEP endpoint names in a region for inventory
- Find VPCEP endpoints by name keyword (fuzzy match via endpoint_service_name)
- Paginated browsing of VPCEP endpoint list
- Check endpoint status, VPC, IP and creation time

## Prerequisites

1. **hcloud CLI** installed and authenticated — See `references/cli-installation-guide.md`
2. **Python 3.8+** with `huaweicloudsdkvpcep` package (SDK fallback)
3. **Huawei Cloud AK/SK** configured via environment variables or `hcloud configure set`
4. **IAM permissions** — `VPCEP ReadOnlyAccess` or finer-grained policy — See `references/iam-policies.md`

## Workflow

1. **Identify query scope** — Decide whether to list all VPCEP endpoints, filter by name keyword, or paginate
2. **Select execution mode** — Use the hcloud CLI by default; fall back to the Python SDK if the CLI is unavailable
3. **Execute the query** — Run the appropriate command and capture the response
4. **Present results** — Summarize endpoint names, IDs, statuses, VPC, IP and creation time in a readable form

> **Note on fuzzy matching:** The VPCEP `ListEndpoints` API supports fuzzy name matching via
> the `endpoint_service_name` parameter. This parameter matches endpoint names that contain
> the given keyword string, not an exact or prefix match.

## Core Commands

### Endpoint Name Queries

| Purpose | Command |
|---------|---------|
| List all VPCEP endpoints | `hcloud VPCEP ListEndpoints --cli-region={region} --limit={limit}` |
| List endpoints filtered by name (fuzzy) | `hcloud VPCEP ListEndpoints --cli-region={region} --endpoint_service_name={name} [--limit={limit}]` |
| List endpoints with pagination | `hcloud VPCEP ListEndpoints --cli-region={region} --limit={limit} --offset={offset}` |
| List endpoints filtered by name with pagination | `hcloud VPCEP ListEndpoints --cli-region={region} --endpoint_service_name={name} --limit={limit} --offset={offset}` |

### Name-Only Lookup (jq)

To extract just the endpoint names:

```bash
hcloud VPCEP ListEndpoints --cli-region={region} --limit={limit} | jq -r '.endpoints[].name'
```

To list endpoint names with status, VPC and IP:

```bash
hcloud VPCEP ListEndpoints --cli-region={region} --limit={limit} | jq -r '.endpoints[] | "\(.name)\t\(.status)\t\(.vpc_id)\t\(.endpoint_ip)"'
```

To show total count and paginated summary:

```bash
hcloud VPCEP ListEndpoints --cli-region={region} --limit={limit} | jq '{total_count, endpoints: [.endpoints[] | {name, id, status, vpc_id, endpoint_ip, created_at}]}'
```

### SDK Fallback Examples

When the CLI is unavailable, use the Python SDK:

```python
import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpcep.v1.region.vpcep_region import VpcepRegion
from huaweicloudsdkvpcep.v1 import vpcep_client
from huaweicloudsdkvpcep.v1.model import ListEndpointsRequest

credentials = BasicCredentials() \
    .with_ak(os.getenv("HUAWEI_ACCESS_KEY")) \
    .with_sk(os.getenv("HUAWEI_SECRET_KEY")) \
    .with_project_id("{project_id}")

client = vpcep_client.VpcepClient.new_builder() \
    .with_credentials(credentials) \
    .with_region(VpcepRegion.value_of("{region}")) \
    .build()

request = ListEndpointsRequest()
request.limit = 100
response = client.list_endpoints(request)
print(f"Total: {response.total_count}")
for ep in response.endpoints:
    print(ep.name, ep.status, ep.vpc_id, ep.endpoint_ip, ep.created_at)
```

## Parameter Confirmation

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `{region}` | Yes | Huawei Cloud region | `cn-north-4` |
| `{name}` | No | Endpoint name keyword (fuzzy match via endpoint_service_name) | `my-endpoint` |
| `{limit}` | No | Maximum records to return (1-500, default 10) | `100` |
| `{offset}` | No | Offset for pagination (default 0) | `0` |
| `{project_id}` | Conditional | Project ID (required for SDK/API) | `0a1234b56c78d9ef` |

## Reference Documents

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## KooCLI Command Format Standard

```bash
hcloud VPCEP <Operation> --cli-region=<region> [--key=value ...]
```

| Feature | Description | Example |
|---------|-------------|---------|
| Service name | `VPCEP` | `hcloud VPCEP ListEndpoints` |
| Operation name | PascalCase | `ListEndpoints` |
| Region parameter | `--cli-region=<value>` | `--cli-region=cn-north-4` |
| Simple parameter | `--key=value` | `--endpoint_service_name=my-endpoint` |
