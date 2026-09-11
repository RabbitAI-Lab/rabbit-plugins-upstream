## Description:

Audits Huawei Cloud skill directories for quality, security, and compliance using skillspector and gitleaks, then generates structured reports with issue details and fix strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scan one Huawei Cloud skill or a folder of skills before release, review security and credential findings, and apply the reported fix strategies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence reports automatic telemetry and local agent/session and Huawei credential probing that users are not fully told about.

Mitigation: Use the skill only in a constrained workspace with no ambient cloud credentials, set SKILL_QUALITY_DISABLE=1 when telemetry is not desired, and review outbound network policy before CI or private-repository use.

Risk: Partial scans created with --skip-checks can leave advertised audit coverage incomplete.

Mitigation: For release gates, run the full audit without skipped checks and review the generated gate verdict before relying on the result.

## Reference(s):

- [Security Audit Guide](artifact/references/security-audit-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [GitCode Security Scanner](artifact/references/gitcode-security-scanner.md)
- [Gitleaks Secret Remediation](https://gitleaks.io/docs/secrets)
- [Complementary GitCode Security Scanner](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text audit report with issue summaries, issue details, fix strategies, and a gate verdict; documentation also includes Markdown command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are saved as skill-gate-report-<timestamp>.txt in the selected output directory.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
