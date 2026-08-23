## Description:

Audit Huawei Cloud skills for quality, security, and compliance using a two-check pipeline that runs SkillSpector for AI security review and gitleaks for credential leak detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release reviewers use this skill to scan Huawei Cloud skill directories before acceptance or release. It produces a gate report with scanned skills, issue summaries, issue details, fix strategies, and a PASS or FAIL verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default fallback path can install external tooling and write into a system binary path.

Mitigation: Use --no-install, prefer the bundled checks, and review any fallback tool installation before running in shared or privileged environments.

Risk: A PASS verdict can be misleading when check coverage is reduced.

Mitigation: Run the full audit without --checks or --skip-checks for release decisions, and document any intentionally reduced coverage.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Method](references/verification-method.md)
- [Security Audit Guide](references/security-audit-guide.md)
- [IAM Policies](references/iam-policies.md)
- [gitcode-security-scanner Usage](references/gitcode-security-scanner.md)
- [Gitleaks Secret Remediation Documentation](https://gitleaks.io/docs/secrets)
- [gitcode-security-scanner Source](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner)

## Skill Output:

**Output Type(s):** [Analysis, Files, Text, Shell commands, Guidance]

**Output Format:** [Plain text audit report with issue summaries, issue details, fix strategies, and a PASS or FAIL gate verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report files are written as skill-gate-report-<timestamp>.txt; scan coverage can change when --checks or --skip-checks is used.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
