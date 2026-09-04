# Dataflow Diagram

```mermaid
sequenceDiagram
    participant User as User/Agent
    participant Skill as list_vpcs.py
    participant SDK as huaweicloudsdkvpc
    participant API as VPC v3 API
    participant VPC as VPC Service

    User->>Skill: Request: List VPCs with filters
    Skill->>Skill: Parse params (project_id, region, filters)

    loop Pagination (marker loop)
        Skill->>SDK: VpcClient.list_vpcs(limit=2000, marker=...)
        SDK->>API: GET /v3/{project_id}/vpc/vpcs?limit=2000
        API->>VPC: Query VPC list page
        VPC-->>API: Return VPC page
        API-->>SDK: HTTP 200 + VPC list + page_info.next_marker
        SDK-->>Skill: Vpcs response object
        alt next_marker exists
            Skill->>Skill: Set marker = next_marker, continue loop
        else no more pages
            Skill->>Skill: Break pagination loop
        end
    end

    Skill->>Skill: Aggregate all VPCs, compute total_count
    Skill-->>User: JSON { total_count: N, vpcs: [...] }
```

## Flow Description

1. User/agent invokes `scripts/list_vpcs.py` with region, project ID, and optional filters
2. The script loads AK/SK from environment variables (using dynamic scanning)
3. The script uses huaweicloudsdkvpc SDK to call VPC v3 API (`ListVpcs`)
4. **Critical pagination fix**: the script loops through ALL pages using the
   `next_marker` from each response, aggregating VPCs until no more pages exist
5. A safety limit of 50 pages prevents infinite loops
6. Duplicate detection (first-item check) prevents marker failure from causing duplicates
7. `total_count` reflects the actual total VPC count across all pages, not just
   the first page
8. This skill performs **read-only** queries — no VPC is created, modified, or deleted