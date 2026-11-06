## Description:

Audits Huawei Cloud skills for quality, security, and compliance, then generates structured reports with findings and fix strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to audit one or more Huawei Cloud skills for quality, credential leaks, and risky runtime behavior, then review a structured report before accepting or releasing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit tool may send private conversation data, source excerpts, and an existing AI-provider key to external services without clearly explaining those transfers.

Mitigation: Before installation, establish explicit control over remote processing, conversation collection, credentials, and CLI updates. For evaluation, use the direct scanner in an isolated offline environment with AI arbitration disabled and without personal session stores or cloud credentials.

Risk: Downloaded CLI executables are not reviewed, and a passing result can be misleading if required checks did not complete.

Mitigation: Review downloaded executables before use and do not rely on PASS unless every required check completed successfully.

## Reference(s):

- [Security audit guide](references/security-audit-guide.md)
- [Verification method](references/verification-method.md)
- [CLI installation and telemetry guide](references/cli-installation-guide.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [gitleaks documentation](https://gitleaks.io/docs/secrets)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/cli/index.html)
- [GitCode security scanner](https://gitcode.com/developer-skill/DTSE-SKILL/tree/main/gitcode-security-scanner)
- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-skill-audit)

## Skill Output:

**Output Type(s):** [Analysis, Text, Files]

**Output Format:** [Structured plain-text audit report with check summaries, issue details, and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a report for a scanned skill or collection of skills.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
