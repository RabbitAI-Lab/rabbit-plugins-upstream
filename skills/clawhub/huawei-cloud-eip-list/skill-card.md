## Description:

Lists Huawei Cloud Elastic IP instances through KooCLI, with an SDK fallback and table, JSON, or compact output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud EIP inventory by region, review returned fields, and filter results by EIP ID, status, or public IP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment settings can bypass the skill's read-only safeguards.

Mitigation: Clear EIP_LIST_HCLOUD_BIN and EIP_LIST_HCLOUD_ARGS in the launch environment.

Risk: The installation guide executes a downloaded installer without verification steps shown in the guide.

Mitigation: Install KooCLI through Huawei's documented download and verification process.

## Reference(s):

- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [KooCLI Installation and Credential Guide](artifact/references/cli-installation-guide.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [Least-Privilege IAM Policies](artifact/references/iam-policies.md)
- [Verification Method and API Reference](artifact/references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Console table, JSON array, or compact EIP alias and public-IP list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inventory output with optional region and EIP filters; results are automatically paginated.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
