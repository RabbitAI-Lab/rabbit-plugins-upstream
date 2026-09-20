---
name: huawei-cloud-resource-inventory
version: 1.0.0
description: |
  Query all Huawei Cloud resources under a tenant across all regions and display
  their inter-resource relationships in grouped tables. Aggregates ECS / BMS / RDS /
  EVS / DCS / CCE / VPC / Subnet / EIP / ELB / NAT / DNS resources in a single run,
  builds an in-memory relationship index (network topology, storage mount, dependency),
  and outputs results as plain-text tables grouped by resource type. Read-only — never
  creates, modifies, or deletes any resource.
  Use this skill when the user needs a full resource inventory, resource relationship
  audit, network topology overview, or cross-region resource census.
  Triggers include: "查询租户资源", "资源清单", "资源关联", "资源盘点",
  "resource inventory", "cloud resource list", "全量资源查询", "资源拓扑",
  "tenant resources", "资源关联关系", "cross-region resource audit".
triggers:
  - 查询租户云资源
  - 租户资源清单
  - 资源关联关系
  - 资源盘点
  - 全量资源查询
  - cloud resource inventory
  - resource topology
  - cross-region resource audit
tags:
  - huawei-cloud
  - resource-inventory
  - aggregation
  - query
  - multi-service
---

# Huawei Cloud Resource Inventory Skill

## Overview

This skill aggregates all Huawei Cloud resources under a tenant across multiple
services and regions, builds inter-resource relationship indexes, and outputs
results as plain-text tables grouped by resource type.

### Architecture

```text
Agent → Python SDK (huaweicloudsdk{ecs,bms,rds,evs,dcs,cce,vpc,eip,elb,nat,dns,iam})
        → Cross-region parallel query
        → In-memory relationship index (VPC↔Subnet↔ECS, EIP↔ECS, EVS↔ECS, CCE↔VPC)
        → Grouped table output
```

### Supported Resource Types

| Resource Type | Service | Key Relationship Fields |
|---------------|---------|------------------------|
| VPC | VPC v3 | id, name, cidr |
| Subnet | VPC v2 | vpc_id (→VPC), az |
| ECS | ECS v2 | vpc_id, subnet_id, eip_port_ids, volume_ids |
| BMS | BMS v1 | az |
| EIP | EIP v2 | port_id (→ECS), associated_server |
| ELB | ELB v3 | vpc_id, subnet_id |
| NAT | NAT v2 | vpc_id (router_id), internal_network_id |
| RDS | RDS v3 | vpc_id, subnet_id |
| EVS | EVS v2 | attached_to (→ECS server_id) |
| DCS | DCS v2 | vpc_id, subnet_id |
| CCE | CCE v3 | vpc_id, subnet_id, node_count |
| DNS | DNS v2 | zone_type (public/private) |

### Relationship Coverage

- **Network topology**: VPC → Subnet → ECS NIC, EIP → ECS (via port_id), ELB → VPC/Subnet, NAT → VPC
- **Storage mount**: EVS → ECS (via attachment server_id)
- **Dependency**: CCE → VPC/Subnet, RDS → VPC/Subnet, DCS → VPC/Subnet

### Applicable Scenarios

- Resource inventory: "list all resources of this tenant across all regions"
- Relationship audit: "which resources are connected to which VPC"
- Network topology overview: "show me the network topology"
- Cross-region census: "how many resources do I have in each region"
- Cost review preparation: enumerate all resources before billing analysis

> **Capability Boundary:** This skill only queries resources. It does not create,
> modify, or delete any resource. It does not query billing, monitoring, or alarm data.

## Prerequisites

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| AK (any of) | Yes | HUAWEICLOUD_SDK_AK / HW_ACCESS_KEY / OBS_ACCESS_KEY |
| SK (any of) | Yes | HUAWEICLOUD_SDK_SK / HW_SECRET_KEY / OBS_SECRET_KEY |
| HTTPS_PROXY | No | Proxy URL if behind a proxy |

### Dependencies

- Python 3.8+
- huaweicloudsdkcore >= 3.1.0
- huaweicloudsdkecs >= 3.1.0
- huaweicloudsdkbms >= 3.1.0
- huaweicloudsdkrds >= 3.1.0
- huaweicloudsdkevs >= 3.1.0
- huaweicloudsdkdcs >= 3.1.0
- huaweicloudsdkcce >= 3.1.0
- huaweicloudsdkvpc >= 3.1.0
- huaweicloudsdkeip >= 3.1.0
- huaweicloudsdkelb >= 3.1.0
- huaweicloudsdknat >= 3.1.0
- huaweicloudsdkdns >= 3.1.0
- huaweicloudsdkiam >= 3.1.0

### IAM Permissions

See `references/iam-policies.md` for the minimum IAM permissions required.

## Workflow

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Set Credentials

```bash
export HUAWEICLOUD_SDK_AK="your-ak"
export HUAWEICLOUD_SDK_SK="your-sk"
```

### Step 3: Execute Query

```bash
# Query all resources across all regions
python3 scripts/resource_inventory.py

# Query a specific region
python3 scripts/resource_inventory.py --region cn-north-4

# Query specific resource types
python3 scripts/resource_inventory.py --resource-type ecs,vpc,eip

# Output as JSON
python3 scripts/resource_inventory.py --format json

# List supported capabilities
python3 scripts/resource_inventory.py --capability-list
```

## Core Commands

| Command | Description |
|---------|-------------|
| `python3 scripts/resource_inventory.py` | Query all resources in all regions (table output) |
| `python3 scripts/resource_inventory.py --region cn-north-4` | Query all resources in a specific region |
| `python3 scripts/resource_inventory.py --resource-type ecs,vpc,eip` | Query specific resource types |
| `python3 scripts/resource_inventory.py --format json` | Output as JSON |
| `python3 scripts/resource_inventory.py --capability-list` | List supported resource types |

## Parameter Confirmation

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--region` | all regions | Specific region to query |
| `--resource-type` | all types | Comma-separated resource types |
| `--format` | table | Output format: table or json |
| `--capability-list` | - | List capabilities and exit |

## 安全硬约束

- AK/SK are read from environment variables dynamically — never hardcoded
- All API calls have 30s timeout — no hanging
- 403/429 errors are caught and reported, not retried indefinitely
- Read-only — no write operations of any kind
- No sensitive data (AK/SK) is written to output, logs, or files
- curl / SDK 调用设 30s 超时——超时判定失败，不 hang
- API 返回 403/无权限时：立即停止该操作并提示用户
- token 不得写入任何文件/日志/评论

## KooCLI Command Format Standard

This skill uses **SDK mode** (huaweicloudsdk Python packages), not hcloud CLI.
No KooCLI commands are used. All API calls are made via Python SDK clients.

If CLI mode is needed in the future, the standard format would be:
`hcloud <Service> <Operation> --cli-region={region} [--params]`

## Reference Documents

- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
