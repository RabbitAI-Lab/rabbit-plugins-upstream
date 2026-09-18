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

### Required Credentials (CI)

Real API functional verification requires Huawei Cloud AK/SK. Configure one of the
following environment variable pairs in the CI/agent runtime; when neither is set the
SDK tests are reported as `SKIP` (not FAIL):

- `HUAWEI_ACCESS_KEY` / `HUAWEI_SECRET_KEY`
- `HUAWEICLOUD_SDK_AK` / `HUAWEICLOUD_SDK_SK`

CLI mode relies on `hcloud configure set` (see `references/cli-installation-guide.md`).

## Manual Verification Checklist

| # | Check | Command |
|---|-------|---------|
| 1 | List all VPCEP endpoints | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=100` |
| 2 | Extract VPCEP endpoint names | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=100 | jq -r '.endpoints[].endpoint_service_name'` |
| 3 | Filter endpoints by name keyword | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --endpoint_service_name={name}` |
| 4 | List with pagination (limit/offset) | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=10 --offset=10` |
| 5 | Show summary with total count and core fields | `hcloud VPCEP ListEndpoints --cli-region=cn-north-4 --limit=100 | jq '{total_count, endpoints: [.endpoints[] | {name: .endpoint_service_name, id, status, vpc_id, ip, created_at}]}'` |

## Expected Results

- All query commands return HTTP 200 with valid JSON
- Empty results are valid (no endpoints matching the filter in the project) — should show friendly message
- The endpoint list response contains an `endpoints` array; each item's core fields:
  - `endpoint_service_name` — endpoint service name
  - `id` — endpoint ID
  - `status` — endpoint status
  - `vpc_id` — VPC ID
  - `ip` — private IP
  - `created_at` — creation time
- The response also contains a `total_count` field for the total number of matching endpoints
