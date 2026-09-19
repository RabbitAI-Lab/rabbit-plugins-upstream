# Data Flow Diagram

## VPCEP Name List Skill Data Flow

```mermaid
graph TD
    A[Agent / User] --> B{Execution Mode}
    B -->|Primary| C[hcloud CLI]
    B -->|Fallback| D[Python SDK]
    C --> E[Huawei Cloud VPCEP API]
    D --> E
    E --> F[VPCEP Service]

    F --> G[Endpoint List Data]

    G --> O[Query Results]

    O --> P[Analysis & Report]
```

## Query Categories

All API paths below are read from the `huaweicloudsdkvpcep` v1 SDK definitions.

| Category | API Path | Methods |
|----------|----------|---------|
| Endpoint List | `/v1/{project_id}/vpc-endpoints` | ListEndpoints |
