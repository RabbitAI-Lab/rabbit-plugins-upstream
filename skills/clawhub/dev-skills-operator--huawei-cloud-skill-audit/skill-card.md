## Description:

Audits Huawei Cloud skill directories for security, quality, and compliance with skillspector, gitleaks, and runtime security checks, producing structured issue reports and fix guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill to scan Huawei Cloud skills before contribution or release, triage detected issues, and rerun gates after remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-install persistent tooling and uses opt-out telemetry.

Mitigation: Run it only in environments where installing the Huawei Cloud quality CLI into ~/.local/bin is acceptable, and configure telemetry opt-out before use when reporting is not appropriate.

Risk: The scanner has a known weakness that can read files outside the selected audit target, and secret redaction is not fixed.

Mitigation: Do not run it on untrusted skill directories; use an isolated workspace, prefer full scans for release gates, and review generated reports before sharing them.

Risk: Skipped-check runs can understate release risk.

Mitigation: Use full scans for release gates and do not present selective or skipped-check runs as PASS.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [GitCode Security Scanner](references/gitcode-security-scanner.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Gitleaks Secret Detection Documentation](https://gitleaks.io/docs/secrets)
- [GitCode Security Scanner Source](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text audit reports and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include scanned skills, issue summaries, issue details, fix strategies, and PASS or FAIL gate verdicts.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
