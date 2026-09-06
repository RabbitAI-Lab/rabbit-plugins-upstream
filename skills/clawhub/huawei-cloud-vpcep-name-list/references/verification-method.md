# Verification Method

## Specification Compliance Verification

```bash
bash scripts/validate-skill.sh skills/network/vpcep/huawei-cloud-vpcep-name-list
```

This checks all items in the Huawei Cloud Skill Specification.

## Functional Testing

### CLI Mode

```bash
bash scripts/test-cli-commands.sh skills/network/vpcep/huawei-cloud-vpcep-name-list cli
```

Test parameters are read from `templates/test-vars.json` (region). Environment variables
`VPCEP_REGION` overrides them. Placeholder values such as `{name}` in the JSON
are treated as unset.

The JSON also documents all test cases used by `test-cli-commands.sh`.

### SDK Mode (Fallback)

```bash
bash scripts/test-cli-commands.sh skills/network/vpcep/huawei-cloud-vpcep-name-list sdk
```

## Manual Verification Checklist

| # | Check | Command |
|---|-------|---------|
| 1 | List all VPCEP endpoints | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=100` |
| 2 | Extract VPCEP endpoint names | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=100 | jq -r '.endpoints[].name'` |
| 3 | Filter endpoints by name keyword | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --endpoint_service_name={name}` |
| 4 | List with pagination (limit/offset) | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=10 --offset=10` |
| 5 | Show summary with total count and core fields | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=100 | jq '{total_count, endpoints: [.endpoints[] | {name, id, status, vpc_id, endpoint_ip, created_at}]}'` |

## Expected Results

- All query commands return HTTP 200 with valid JSON
- Empty results are valid (no endpoints matching the filter in the project) — should show friendly message
- The endpoint list response contains an `endpoints` array; each item's `name` is the endpoint name, `id` is the endpoint ID, `status` is the endpoint status, `vpc_id` is the VPC ID, `endpoint_ip` is the private IP, and `created_at` is the creation time
- The response also contains a `total_count` field for the total number of matching endpoints
