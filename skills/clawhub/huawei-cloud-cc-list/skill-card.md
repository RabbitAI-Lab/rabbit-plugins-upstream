## Description:

Lists Huawei Cloud Cloud Connect instances with optional filters and table, JSON, or names-only output through KooCLI or the Huawei Cloud SDK fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud network operators use this skill to inspect Huawei Cloud Cloud Connect inventory, filter instances, and retrieve connection details for operational workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation guide downloads and runs an installer whose publisher provenance is unclear.

Mitigation: Use Huawei's official installation instructions, verify the installer source before running it, and keep executable overrides under your control.

Risk: Cloud credentials used for listing can expose account access if mishandled or over-privileged.

Mitigation: Configure credentials outside chat, keep them secret, and grant only the cloud-connection list permission needed for this skill.

## Reference(s):

- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM Policies (least privilege, read-only)](references/iam-policies.md)
- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Human-readable table, JSON array, or plain-text instance names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inventory results with optional filters and marker-based pagination.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
