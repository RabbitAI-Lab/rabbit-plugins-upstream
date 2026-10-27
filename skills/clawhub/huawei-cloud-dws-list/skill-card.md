## Description:

Lists Huawei Cloud DWS clusters in a tenant region through KooCLI, with an SDK fallback and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and platform operators use the skill to inspect regional DWS cluster inventory, filter and page through results, and retrieve cluster IDs for follow-up work.

### Deployment Geography for Use:

The Huawei Cloud tenant region selected by the user; service availability depends on that region.

## Known Risks and Mitigations:

Risk: Unchecked settings can change the program the skill runs or the destination configured for its fallback connection.

Mitigation: Use only trusted region values and leave DWS_LIST_HCLOUD_BIN and DWS_LIST_HCLOUD_ARGS unset.

Risk: The skill uses credentials configured for Huawei Cloud access.

Mitigation: Use narrowly scoped read-only credentials, such as access limited to listing DWS clusters.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dws-list)
- [Publisher profile](https://clawhub.ai/user/wlc-dev)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [text, json]

**Output Format:** [A full-field cluster table by default, a raw JSON array with --json, or a compact cluster-name list with --names-only.]

**Output Parameters:** [['Region', 'Enterprise project ID', 'Name, status, or cluster ID filters', 'Local limit and offset']]

**Other Properties Related to Output:** [Read-only cluster inventory results; filters and pagination are applied locally.]

## Skill Version(s):

1.0.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
