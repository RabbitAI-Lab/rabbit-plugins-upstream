## Description:

Audits Huawei Cloud skills for security, credential leaks, and risky runtime patterns, producing findings and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit Huawei Cloud skill directories, review security findings and fix strategies, and check a PASS/FAIL quality gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic audit reporting may send local agent session data to an external service.

Mitigation: For private or sensitive work, disable reporting with SKILL_QUALITY_DISABLE=1 and review reporting endpoints before running.

Risk: LLM arbitration may send scanned source context to a remote model service.

Mitigation: Disable arbitration with SKILL_AUDIT_LLM_ARBITER=0 for sensitive source and review the configured model endpoint and keys.

Risk: Skipping checks can leave the audit incomplete.

Mitigation: Run the full set of checks before relying on the gate verdict; treat runs with --skip-checks as incomplete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-skill-audit)
- [Security audit guide](artifact/references/security-audit-guide.md)
- [Audit acceptance criteria](artifact/references/acceptance-criteria.md)
- [CLI installation and telemetry controls](artifact/references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Plain-text audit report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped report with issue details, fix strategies, and a PASS/FAIL gate verdict.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
