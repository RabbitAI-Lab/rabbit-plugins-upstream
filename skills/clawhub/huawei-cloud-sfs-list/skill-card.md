## Description:

Lists Huawei Cloud SFS file systems in a selected region through KooCLI, with an SDK fallback and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inventory SFS file systems in a Huawei Cloud region and retrieve file-system identifiers for follow-up tasks. It is limited to listing and filtering resources.

### Deployment Geography for Use:

Huawei Cloud regions (default: cn-north-4)

## Known Risks and Mitigations:

Risk: The supplied KooCLI installation command uses a download source that the security review says is unverified.

Mitigation: Install KooCLI using Huawei's official instructions and verify the downloaded package instead of running the supplied installer command.

Risk: The SDK fallback reads credentials from environment variables, contrary to assurances in the skill documentation.

Mitigation: Use a dedicated read-only cloud identity, review which environment credentials are available to the process, and confirm the target region before running.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-sfs-list)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM policy guidance](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Aligned text table, JSON array, or names-and-IDs text inventory]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inventory results with optional region, paging, and client-side filters.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
