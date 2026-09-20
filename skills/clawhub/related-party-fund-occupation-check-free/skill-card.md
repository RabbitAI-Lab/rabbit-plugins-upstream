## Description:

关联方往来台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Group finance, corporate secretary or securities affairs, and internal audit teams use this skill before monthly related-party balance cleanup, annual audit, and disclosure workflows to check related-party ledger tables for arithmetic consistency, totals, duplicates, blanks, and cited findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake ledger consistency findings for legal, audit, tax, or disclosure advice.

Mitigation: Treat the output as a consistency aid and route legal, audit, tax, and disclosure decisions to qualified reviewers.

Risk: The free release explicitly omits several higher-level related-party fund occupation checks.

Mitigation: Review the omitted-checks list in the output and use a fuller review workflow when those scenarios matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/related-party-fund-occupation-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Console text or JSON result reports with cited findings and listed omitted checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on local related-party ledger text or JSON input; the free tier reports both executed checks and checks not included in this release.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
