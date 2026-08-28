## Description:

Analyzes pet food-bowl videos or video URLs to estimate feeding start and end times and eating speed, then returns non-diagnostic slow-feed intervention guidance when eating appears too fast.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in smart slow-feeder bowl and pet-care workflows to analyze food-bowl videos, review structured feeding-speed results, and retrieve prior cloud reports. The skill is intended for behavior and feeding-speed reference only, not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet feeding videos or video URLs may be sent to the configured remote backend for analysis.

Mitigation: Use non-sensitive footage, confirm the configured endpoint, and avoid household footage that should not leave the local environment.

Risk: The workflow can silently create or reuse a backend identity and fetch cloud report history.

Mitigation: Run in an isolated workspace and verify account, retention, and report-access behavior with the publisher before deployment.

Risk: Backend tokens may be stored in the workspace database.

Mitigation: Limit access to the workspace, rotate credentials after testing, and review token storage and cleanup expectations before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface document](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured report text, Markdown tables for report history, or JSON output when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feeding timestamps, eating-speed estimates, threshold comparison, intervention advice, and cloud report links when available.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
