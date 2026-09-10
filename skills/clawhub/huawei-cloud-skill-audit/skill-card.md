## Description:

Audits Huawei Cloud skills for quality, security, and compliance using skillspector AI-security checks and gitleaks credential-leak detection, producing structured reports with issue details and fix strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to scan Huawei Cloud skill directories before release or in CI/CD, review security and credential findings, and follow generated remediation guidance before re-running the audit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audit execution can send quality reporting metadata to a remote endpoint unless disabled.

Mitigation: Run with SKILL_QUALITY_DISABLE=1 when remote reporting is not intended, and use a clean environment without broad Huawei Cloud credentials.

Risk: Fallback tool installation may occur when built-in scanner resources are unavailable.

Mitigation: Run with --no-install and pre-review or pin any scanner tools used in the execution environment.

Risk: Static scanning may miss obfuscated or runtime-generated behavior.

Mitigation: Treat PASS as a gate result rather than a complete assurance claim, review warnings and report details, and use complementary scanning where needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-audit)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [IAM Policies](references/iam-policies.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [Verification Method](references/verification-method.md)
- [gitcode-security-scanner Usage](references/gitcode-security-scanner.md)
- [gitleaks secrets documentation](https://gitleaks.io/docs/secrets)
- [gitcode-security-scanner source](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance, files]

**Output Format:** [Plain text report with command examples and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates skill-gate-report-<timestamp>.txt with scanned skills, issue summary, issue details, fix strategies, and PASS/FAIL gate verdict.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
