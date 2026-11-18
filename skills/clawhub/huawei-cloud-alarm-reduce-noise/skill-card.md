## Description:

Analyzes Huawei Cloud CES and AOM alarm data to identify noise patterns and produce optimization recommendations and an HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to review Huawei Cloud CES and AOM alarms, identify recurring or unresolved issues, and plan noise reduction. It produces analysis and operational recommendations for the selected regions and core resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags an unpinned remote installer and a root-level troubleshooting command as installation and privilege risks.

Mitigation: Avoid the reported “latest” installer and root-level troubleshooting command; review installation steps before running them.

Risk: The security guidance says generated report markup could execute when viewed.

Mitigation: Review generated reports before opening them, and use a restricted viewing environment when their contents are untrusted.

Risk: The security scan is incomplete because it excluded executable content in a spreadsheet and its tool-misuse analyzer was degraded.

Mitigation: Treat the scan as partial and review the bundled files, including embedded spreadsheet content, before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-alarm-reduce-noise)
- [Alarm analysis methodology](references/alarm-analysis.md)
- [IAM policies](references/iam-policies.md)
- [KooCLI installation guide](references/cli-installation-guide.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, HTML report, JSON alarm data]

**Output Format:** [HTML optimization report with alarm summaries, trends, and recommendations; JSON alarm data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multi-region selection, 1-, 7-, and 30-day or custom date ranges, and core-resource filtering.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
