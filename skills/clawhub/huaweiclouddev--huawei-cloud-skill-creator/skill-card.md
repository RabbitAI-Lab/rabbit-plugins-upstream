## Description:

Creates Huawei Cloud skill packages through a six-phase workflow covering requirements gathering, CLI/SDK/API research, Markdown generation, test preparation, detailed testing, cleanup, and compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to scaffold Huawei Cloud agent skills, research supported execution modes, prepare validation artifacts, and run credential-gated tests before release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-backed Huawei Cloud, API, and shell commands may run against live accounts during testing.

Mitigation: Use an isolated Huawei Cloud test project, least-privilege and preferably short-lived credentials, and avoid production accounts.

Risk: Generated test inputs or templates may trigger unintended operations if they are run without review.

Mitigation: Review templates/test-vars.json and generated commands before execution, and require explicit approval for any mutating cloud operation.

Risk: Scanner-ignore or gitleaks-ignore usage can hide security findings.

Mitigation: Treat any scanner-ignore or gitleaks-ignore entry as requiring explicit security approval before installation or release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-creator)
- [KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud SDK center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)
- [Huawei Cloud API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi)
- [KooCLI Installation & Configuration Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Related Commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline shell, Python, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates a complete skill directory structure with references, scripts, templates, phase summaries, and validation guidance.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter reports 2.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
