## Description:

Analyzes pet feeding-area videos or video URLs through server-side APIs to estimate feeding duration and eating speed, flag fast-eating risk, and provide slow-feed intervention guidance without disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet food-bowl videos, produce structured eating-speed reports, and decide whether slow-feed reminders or device-side interventions are appropriate. It is intended for pet health management and smart slow-feeder workflows, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, URLs, account identifiers, and report history may be sent to LifeEmergence cloud APIs.

Mitigation: Review data-sharing acceptability before installation and avoid submitting sensitive media or identifiers unless that transfer is approved.

Risk: The skill can silently create or reuse an identity, read local identity material, and persist returned tokens in a shared workspace SQLite database.

Mitigation: Run it in a controlled workspace, limit filesystem access, and clear stored identity or token state between users.

Risk: Cloud report history can be queried with limited user control.

Mitigation: Restrict use to authorized accounts and review whether historical report access is appropriate for the deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [Pet eating speed API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown and JSON analysis reports with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feeding start/end times, eating-speed estimates, risk labels, slow-feed recommendations, and historical report tables.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
