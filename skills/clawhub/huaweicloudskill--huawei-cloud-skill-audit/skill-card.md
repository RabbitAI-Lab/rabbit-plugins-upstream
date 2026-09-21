## Description:

Audits Huawei Cloud skill directories for quality, security, and compliance using built-in skillspector, gitleaks, and runtime security checks, then generates structured issue reports and fix strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit Huawei Cloud skills before release or acceptance, review security and quality findings, and follow generated remediation guidance before re-running the gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the default wrapper can collect local agent session content and command output and report it remotely with under-disclosed controls.

Mitigation: Review before installing in sensitive workspaces; prefer the direct Python audit command when telemetry is not desired, or set SKILL_QUALITY_DISABLE=1, verify endpoint settings, and avoid wrapping commands whose output or recent sessions may contain secrets or proprietary content.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [GitCode Security Scanner Usage](references/gitcode-security-scanner.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-skill-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text and Markdown reports with command examples and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include scanned skills, severity summaries, issue details, fix strategies, and a PASS or FAIL gate verdict.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
