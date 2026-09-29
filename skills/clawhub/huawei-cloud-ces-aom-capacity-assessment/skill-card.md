## Description:

Assesses Huawei Cloud instance capacity using CES and AOM monitoring data, then reports projected demand and scale-out recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operations engineers use this skill to compare historical or recent monitoring peaks and valleys across Huawei Cloud instances, forecast event demand, and decide whether to scale out.

### Deployment Geography for Use:

Global, where the selected Huawei Cloud region supports the required CES/AOM metrics.

## Known Risks and Mitigations:

Risk: Credentialed cloud requests may be exposed by the documented TLS-bypass or direct-IP networking workaround.

Mitigation: Avoid the workaround; use an approved network or DNS fix and promptly remove temporary hosts-file changes.

Risk: Broad cloud permissions increase the impact of credential misuse.

Mitigation: Use a Huawei Cloud account restricted to read-only CES/AOM access.

Risk: Assessment writes replace workbook contents without retaining a backup.

Mitigation: Run assessments on a copy of any important Excel workbook.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ces-aom-capacity-assessment)
- [Metric registry](references/metrics.json)
- [Region mapping](references/region-map.md)
- [IAM permission notes](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [DNS troubleshooting](references/troubleshooting-dns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown assessment summary and updated Excel workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes capacity and scale-out recommendations, workbook location, and collection or skipped-row details.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
