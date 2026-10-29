## Description:

Lists Huawei Cloud Cloud Connect instances by region, with optional filters and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect Huawei Cloud Cloud Connect inventory and locate connection IDs for follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SDK fallback directly reads cloud secrets, so credential handling needs review.

Mitigation: Use a dedicated identity limited to cc:cloudConnections:list, configure credentials outside chat, and prefer the KooCLI profile path when suitable.

Risk: Read-only guarantees and credential-handling claims exceed what the code enforces.

Mitigation: Keep executable overrides unset and enforce read-only access through IAM; do not rely on the skill's guard as the permission boundary.

## Reference(s):

- [KooCLI installation documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text table, JSON array, or instance-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region and instance filters; results may be marker-paged.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
