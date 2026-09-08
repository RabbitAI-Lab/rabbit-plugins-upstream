---
name: huawei-cloud-vpc-list
description: |
  Query the list of Huawei Cloud Virtual Private Clouds (VPCs) belonging to the
  current tenant / project. Returns VPC id, name, CIDR block, status,
  description, enterprise project and other metadata. Supports filtering by
  VPC name, ID, CIDR block and enterprise project, pagination via limit/marker,
  and listing VPCs across all enterprise projects (all_granted_eps). Uses the
  huaweicloudsdkvpc Python SDK to query the VPC v3 API with full page aggregation
  — automatically loops through all paginated results to return the correct total
  VPC count. Read-only — never creates, modifies or deletes any resource.
  Use this skill whenever the user wants to list/inspect the VPCs of the tenant,
  e.g. for network inventory, VPC planning, or troubleshooting.
  Triggers include: "query VPC list", "list VPCs", "VPC list", "查询VPC列表",
  "查询vpc列表", "VPC列表", "租户VPC列表", "查询租户的VPC", "list my vpcs",
  "how many VPCs", "VPC inventory".
tags:
  - huawei-cloud
  - vpc
  - list
  - network
  - query
---

# Huawei Cloud VPC List Skill

## Overview

This skill queries the list of **VPCs (Virtual Private Clouds)** under the current
Huawei Cloud tenant / project and returns their key attributes (ID, name, CIDR,
status, description, enterprise project). It uses the `huaweicloudsdkvpc` Python
SDK to call the VPC v3 API (`ListVpcs`), and **automatically aggregates all
paginated results** to ensure the returned VPC count matches the actual total.

### Architecture

```
Agent → scripts/list_vpcs.py (Python SDK) → Huawei Cloud VPC v3 API
```

### API version

| Version | SDK Operation | API Path |
|---------|---------------|----------|
| v3      | `VpcClient.list_vpcs` | `GET /v3/{project_id}/vpc/vpcs` |

### Applicable Scenarios

- Network inventory: "list all VPCs of this tenant" — returns correct total count
- VPC planning: verify existing CIDR ranges before creating new subnets/VPCs
- Troubleshooting: locate a VPC by name/id and inspect its status
- Enterprise-project audit: list VPCs of one enterprise project or all projects

> **能力边界（Capability Boundary）：**
> 本 Skill **仅查询 VPC 列表**。不创建/删除/修改 VPC，也不查询子网、安全组、
> 路由表等其它资源（那些属于 VPC 的其它查询能力或专用 Skill）。
> 若用户询问"查询子网/安全组/路由表"等，请明确告知本 Skill 不提供该能力。

## Prerequisites

1. **Python 3.8+** with `huaweicloudsdkvpc` package installed:

   ```bash
   pip install huaweicloudsdkvpc
   ```
2. **IAM permissions** — `vpc:vpcs:list` (read-only) is required to list VPCs.
   See `references/iam-policies.md`.
3. **AK/SK credentials** — set via environment variables:
   - `HUAWEI_ACCESS_KEY` / `HUAWEI_SECRET_KEY`, or
   - `HW_AK` / `HW_SK`, or
   - other `HUAWEI*_AK` / `HUAWEI*_SK` pattern variables
4. **Region and Project ID** — specify via `--region` and `--project_id`.

## Workflow

1. **Confirm parameters** — ask the user for the target region (default
   `cn-north-4`), project ID, and any optional filters
2. **Verify prerequisites** — check `list_vpcs.py --help` for syntax validity,
   and confirm AK/SK environment variables are set
3. **Run the query** — execute `python3 scripts/list_vpcs.py --project_id=...`
   with the desired filters and pagination options
4. **Aggregate all pages** — the script **automatically loops through all**
   **paginated results** using the `next_marker` from each response, ensuring
   every VPC is counted
5. **Return results** — the script outputs the full VPC list (id, name, cidr,
   status, description, enterprise project id) along with the **correct total**
   **count** aggregated across all pages
6. **Handle errors** — on auth/region errors, verify credentials and region;
   on permission errors, report the missing IAM permission

## Core Commands

### Query All VPCs (with full page aggregation)

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region}
```

### Query with a Custom Limit Per Page

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --limit=100
```

### Filter by Enterprise Project

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --enterprise_project_id={id}
```

### Filter by VPC Name

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --name my-vpc
```

### Filter by VPC ID

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --id {vpc_id}
```

### Filter by CIDR

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --cidr 192.168.0.0/16
```

### Local Pagination (after full aggregation)

```bash
# Full aggregation returns all VPCs
python3 scripts/list_vpcs.py --project_id={project_id} --region={region}

# Use marker to start from a specific VPC
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --marker={vpc_id}
```

### Output as Text Table

```bash
python3 scripts/list_vpcs.py --project_id={project_id} --region={region} --output=text
```

## Parameter Confirmation

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `{project_id}` | Yes | Huawei Cloud project ID (from IAM) | `0a0...` |
| `{region}` | Yes | Huawei Cloud region | `cn-north-4` |
| `{limit}` | No | Max records to show (default: 2000, max: 2000) | `100` |
| `{marker}` | No | Start marker for continuation | VPC UUID from response |
| `{name}` | No | VPC name filter (multiple supported) | `production-vpc` |
| `{id}` | No | VPC ID filter (multiple supported) | `vpc-...` |
| `{cidr}` | No | CIDR filter (multiple supported) | `192.168.0.0/16` |
| `{description}` | No | Description filter (multiple supported) | `production` |
| `{enterprise_project_id}` | No | Enterprise project ID | `0` or `all_granted_eps` |

## Reference Documents

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)