## Description:

Diagnoses Huawei Cloud CDN domain DNS resolution issues by checking domain details, probing A-record resolution, verifying resolved IP attribution, and producing a read-only diagnosis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, CDN operators, and support engineers use this skill to diagnose why a domain is not resolving to Huawei Cloud CDN, whether a CNAME has taken effect, or whether resolved IPs belong to Huawei Cloud CDN. It is limited to read-only DNS diagnosis and hands off certificate, origin, ownership, and configuration-change requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses local Huawei Cloud hcloud credentials.

Mitigation: Use a least-privilege IAM user and do not paste AK/SK values into chat or tickets.

Risk: Diagnosis results may lead to DNS or CDN configuration changes outside the skill.

Mitigation: Treat the report as diagnostic guidance only and make any DNS or CDN changes manually after review.

Risk: DNS observations may be incomplete because the probe uses the host resolver, checks A records, and limits IP attribution to the first 20 IPs.

Mitigation: Review timeout, resolver, and IP-limit notes in the report and rerun verification from another resolver or region when partial resolution is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cdn-dns-resolution-diagnosis)
- [Permission check workflow](references/task-permission-check.md)
- [DNS resolution probe workflow](references/task-dns-resolve.md)
- [IP attribution workflow](references/task-ip-attribution.md)
- [Diagnosis report workflow](references/task-report-generation.md)
- [Prohibited operations](references/prohibited-operations.md)
- [API and CLI command reference](references/related-apis.md)
- [IAM permission policies](references/iam-policies.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Structured text diagnosis report with inline shell commands and parsed JSON probe results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; DNS probe has a 10-second default timeout and IP attribution is limited to 20 IPs per query.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
