# Acceptance Criteria

## Functional Criteria

| # | Criterion | Verification |
|---|-----------|-------------|
| 1 | ListEndpoints returns valid response | `hcloud VPCEP ListEndpoints --cli-region={region}` succeeds and returns endpoint list |
| 2 | Endpoint names are present in the response | Each item's `name` field is returned in the `endpoints` array |
| 3 | Name keyword filter works | `hcloud VPCEP ListEndpoints --cli-region={region} --endpoint_service_name={name}` returns matching endpoints |
| 4 | Pagination with limit works | `hcloud VPCEP ListEndpoints --cli-region={region} --limit=10` returns at most 10 items |
| 5 | Pagination with offset works | `hcloud VPCEP ListEndpoints --cli-region={region} --limit=10 --offset=10` returns items from page 2 |
| 6 | total_count is returned | Response includes `total_count` field |
| 7 | Core fields are present | Endpoints include name, id, status, vpc_id, endpoint_ip, created_at |

## Non-Functional Criteria

| # | Criterion | Threshold |
|---|-----------|-----------|
| 1 | All commands are read-only | No create/update/delete operations |
| 2 | CLI command response time | < 10s for list operations |
| 3 | SDK fallback works when CLI unavailable | Query methods available via SDK |
| 4 | No credential hardcoding | AK/SK from environment variables only |
| 5 | IAM least privilege | ReadOnlyAccess only |
| 6 | Empty result friendly message | "No endpoint matched" message when no results |

## Compliance Criteria

| # | Criterion | Check |
|---|-----------|-------|
| 1 | SKILL.md frontmatter valid | name + description + tags present |
| 2 | All required sections present | Overview, Prerequisites, Workflow, Core Commands, Parameter Confirmation, Reference Documents |
| 3 | No version field in frontmatter | `version` key absent |
| 4 | File count <= 30 | Count all files in skill directory |
| 5 | SKILL.md line count <= 500 | Line count check |
