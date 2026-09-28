## Description:

Audits Huawei Cloud agent skills for security and credential leaks, then produces issue details, remediation guidance, and an audit verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to audit Huawei Cloud skill directories, inspect findings and suggested fixes, and decide whether a skill passes a release gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required wrapper installs a persistent user-level CLI and can send agent-session prompts and metadata to a remote service by default.

Mitigation: Review the installation and telemetry policy before use; for sensitive sessions, set SKILL_QUALITY_DISABLE=1 and use the direct local audit command when remote reporting is unnecessary.

Risk: Skipped checks can give an incomplete audit result.

Mitigation: Run all three checks before relying on a release-gate verdict and disclose any skipped checks.

Risk: Running audit scripts by relative path from an untrusted target directory may execute a different script.

Mitigation: Invoke the audit script using the absolute path to the installed skill directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-skill-audit)
- [Security audit guide](artifact/references/security-audit-guide.md)
- [Acceptance criteria](artifact/references/acceptance-criteria.md)
- [Verification method](artifact/references/verification-method.md)
- [CLI installation and telemetry controls](artifact/references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain text audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped report with scanned skills, issue summary, issue details, fix strategies, and PASS/FAIL verdict.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
