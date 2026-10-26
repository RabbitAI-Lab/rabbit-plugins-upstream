## Description:

Lists Huawei Cloud ECS instances in a tenant region through KooCLI, with an automatic fallback to the Huawei Cloud ECS SDK when KooCLI is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use the skill to inventory ECS instances in a Huawei Cloud region, filter results by status or name, and obtain instance identifiers for follow-on workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SDK fallback can construct a server endpoint from an unchecked region value, potentially directing credentialed requests outside Huawei Cloud.

Mitigation: Before enabling the fallback, validate region identifiers and Huawei endpoint hostnames; use read-only cloud credentials.

Risk: Inventory results can expose internal network details, including private IP addresses.

Mitigation: Limit access to inventory output and handle it according to the organization's sensitive infrastructure-data practices.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-ecs-list)
- [KooCLI installation guide](references/cli-installation-guide.md)
- [IAM permissions](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable table, compact instance-name and ID list, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, filterable and paginated inventory output; printed to stdout and may include private and public IP addresses.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
