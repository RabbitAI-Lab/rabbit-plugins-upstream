## Description: <br>
Audits Huawei Cloud skills for quality, security, and compliance, then generates structured issue reports with fix strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers use this skill to scan Huawei Cloud skill directories before release, identify security, quality, style, and specification issues, and get remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release may under-run its advertised five-check security gate. <br>
Mitigation: Review before installing, confirm which checks are actually enabled, and do not rely on it as a five-check release gate until registry, documentation, and skip-check behavior are aligned. <br>
Risk: Fallback installation behavior can modify the host environment. <br>
Mitigation: Run in an isolated workspace, use --no-install, preinstall trusted tools when needed, and set an explicit --output-dir. <br>
Risk: Generated reports may include credential snippets from scanned files. <br>
Mitigation: Treat audit reports as sensitive, store them in a protected location, and redact findings before sharing outside the review team. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-skill-audit) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Security Audit Guide](references/security-audit-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [GitCode Security Scanner](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner) <br>
- [Gitleaks Secrets Documentation](https://gitleaks.io/docs/secrets) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and plain-text audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces timestamped skill-gate-report files with issue summaries, issue details, fix strategies, and PASS/FAIL verdicts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
