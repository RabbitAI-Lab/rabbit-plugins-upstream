## Description:

Audits Huawei Cloud skill directories with local SkillSpector and gitleaks checks and produces a structured report with issue details, fix strategies, and a PASS/FAIL gate verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to scan Huawei Cloud skill directories before release, review reported security or credential findings, and follow remediation guidance. Treat the PASS result as a local two-check scanner result unless the documented five-check compliance gate is independently verified.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security-gate claims do not match the shipped checks, so a PASS result may be narrower than readers expect.

Mitigation: Treat output as a local SkillSpector and gitleaks scan result and verify full Huawei Cloud skill compliance separately before release decisions.

Risk: Automatic installation and PATH-provided scanner binaries can change what code is executed during an audit.

Mitigation: Run with `--no-install`, pin and review scanner binaries, and avoid elevated privileges when scanning untrusted skill directories.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [Verification Method](references/verification-method.md)
- [IAM Policies](references/iam-policies.md)
- [gitcode-security-scanner Usage](references/gitcode-security-scanner.md)
- [Gitleaks Secret Remediation Documentation](https://gitleaks.io/docs/secrets)
- [gitcode-security-scanner Source](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text audit report with Markdown guidance and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports scanned skills, severity summary, issue details, fix strategies, and a PASS/FAIL gate verdict.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
