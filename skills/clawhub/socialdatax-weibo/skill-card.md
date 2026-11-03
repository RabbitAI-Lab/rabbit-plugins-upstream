## Description:

A SocialDataX-powered assistant for Weibo hot searches, post and comment research, engagement review, and creator profile and post lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and content teams can use the skill to monitor Weibo hot searches and examine posts, comments, engagement, creator profiles, and creator timelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and target identifiers are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Review queries and target identifiers before submitting, monitor credit use, and keep the API key out of chat and version control.

Risk: The external CLI implementation and future package releases were not verified by the security review.

Mitigation: Use a reviewed, fixed package version and limit its access to unrelated files and secrets.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured Weibo data with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; requests may consume paid credits.]

## Skill Version(s):

0.1.22 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
