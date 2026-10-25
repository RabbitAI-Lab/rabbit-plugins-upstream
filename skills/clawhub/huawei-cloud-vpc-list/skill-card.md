## Description:

Lists Huawei Cloud VPCs in a selected region and presents results as a full-field table, a JSON array, or a names-only list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Inspect tenant VPC inventory and retrieve identifiers, names, CIDRs, states, and other returned fields before follow-up operations.

### Deployment Geography for Use:

Huawei Cloud tenant regions selected for each query; service availability depends on the selected region.

## Known Risks and Mitigations:

Risk: The documented installation flow requires an automatically installed telemetry wrapper without disclosing its reported fields or destinations.

Mitigation: Before installation, request an optional telemetry workflow and disclosure of reported fields and destinations; review and pin the wrapper release, and use narrowly scoped read-only cloud credentials.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-vpc-list)
- [Huawei Cloud KooCLI installation guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [A full-field table by default, a raw JSON array with --json, or a compact VPC name list with --names-only.]

**Output Parameters:** [Supports region selection, VPC ID and enterprise-project filters, and project ID for the SDK fallback; results are paginated automatically.]

**Other Properties Related to Output:** [Read-only inventory operation; mutating intents are blocked. Uses configured Huawei Cloud credentials and does not require credentials in chat.]

## Skill Version(s):

1.0.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
