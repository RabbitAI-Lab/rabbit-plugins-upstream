## Description:

Audits articles and reports by checking factual claims against primary or reliable secondary sources and producing structured findings, cross-version comparisons, and regression checks without editing the source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and research teams use the skill to verify high-risk factual claims, source quality, incident attribution, and consistency across article versions. It returns audit findings while leaving the source material unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is incomplete because a local path-like reference could not be resolved.

Mitigation: Review the unresolved reference and inspect the skill's behavior before relying on its audit output.

Risk: The skill uses fixed claim statuses and severity levels, and some classifications require judgment.

Mitigation: Have a reviewer check the source quality, status assignments, and judgment calls before acting on the report.

## Reference(s):

- [Claim-to-Source Auditor on ClawHub](https://clawhub.ai/haiyangchenbj/skills/claim-to-source-auditor-skill)

## Skill Output:

**Output Type(s):** [Markdown, CSV, Text]

**Output Format:** [Structured Markdown audit report and CSV claim records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports claim statuses and P0–P2 severity; can include cross-platform comparisons and an optional regression gold-set CSV.]

## Skill Version(s):

1.0.8 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
