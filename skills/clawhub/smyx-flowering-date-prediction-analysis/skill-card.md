## Description:

Uses cloud media analysis to provide flowering-date predictions and historical reports from plant images or videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse growers, cut-flower producers, and botanical garden staff can submit flower-bud images or videos to inform flowering schedules and retrieve cloud-hosted analysis reports. Predictions should be checked against field observations before production planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or submitted URLs are sent to a cloud service for analysis.

Mitigation: Confirm the destination and obtain permission before submitting sensitive media or URLs.

Risk: The skill silently creates or reuses an identity and caches tokens in the workspace data directory.

Mitigation: Disclose identity and token retention, restrict access to cached credentials, and review retention before use.

Risk: Cloud report history can be retrieved without an explicit confirmation step, and the skill's flowering-date description may not match its underlying analysis behavior.

Mitigation: Require user confirmation before history access and verify reported predictions against observations before acting on them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Bundled API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text report with structured analysis content and Markdown links or tables for cloud reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report text to a file; the skill describes a 3–7-day forecast and warns that dates may vary by 1–2 days.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release; bundled SKILL.md frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
