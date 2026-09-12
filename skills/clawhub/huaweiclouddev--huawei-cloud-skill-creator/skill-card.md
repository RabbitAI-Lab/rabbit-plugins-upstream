## Description:

Creates Huawei Cloud agent skill packages through a six-phase workflow covering requirements gathering, CLI/SDK/API research, document generation, test preparation, detailed testing, cleanup, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create Huawei Cloud skills with structured requirements, researched execution modes, generated documentation, test assets, IAM guidance, and final validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires cloud credentials and can run broad shell-based tests.

Mitigation: Use an isolated workspace with short-lived, least-privilege Huawei Cloud test credentials.

Risk: Generated skills or test commands may be unsafe or inappropriate for the target account.

Mitigation: Review generated skills, commands, IAM policies, and test cases before execution.

Risk: Telemetry is delegated to external reporter code.

Mitigation: Avoid the telemetry step unless the reporter implementation and endpoint are trusted.

Risk: The workflow may install or depend on local CLI, SDK, Node.js, Python, and scanning tools.

Mitigation: Pin or sandbox dependency installs before running the workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-creator)
- [KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Related Commands](references/related-commands.md)
- [Security Audit Guide](references/security-audit-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, shell, Python, and curl snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce skill package files and phase summary JSON during guided creation.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
