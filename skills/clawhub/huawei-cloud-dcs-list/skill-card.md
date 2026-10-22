## Description:

Lists Huawei Cloud DCS (Redis and Memcached) instances in a selected region using read-only queries, with name-list, table, and JSON output modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to inspect Huawei Cloud DCS instance inventories in a tenant region, filter and review instances, and obtain instance IDs for follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exact-name searches can silently ignore requested tag filters and return inventory outside the selected scope.

Mitigation: Do not rely on combined exact-name and tag searches until the filtering defect is corrected; verify scope with separate searches.

Risk: Detailed inventory output can expose sensitive instance information, and credentials used for cloud access must be protected.

Mitigation: Use read-only cloud permissions, configure credentials outside chat, and keep detailed inventory private.

## Reference(s):

- [Huawei Cloud KooCLI installation and published checksums](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dcs-list)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [Plain-text instance-name list, full-field table, or raw JSON response array]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inventory results; fields can include instance IDs, addresses, status, and configuration details.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
