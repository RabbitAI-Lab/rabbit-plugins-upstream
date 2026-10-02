## Description:

Researches short-form video niches, trends, creators, hashtags, sounds, and hooks across TikTok, YouTube Shorts, and Instagram Reels using the Virlo API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[virlo-ai](https://clawhub.ai/user/virlo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and research teams use this skill to identify effective short-form content, evaluate creators, and track market trends with Virlo's social-video data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid one-shot searches and creator lookups can consume Virlo credits.

Mitigation: Confirm the requested research and expected cost before paid calls; check the account balance.

Risk: Recurring monitors and tracking jobs can generate ongoing charges.

Mitigation: Confirm cadence and expected recurring cost before creation, and monitor the Virlo balance.

Risk: Deleting a monitor can permanently stop it and remove it from lists; webhook subscriptions send updates to external endpoints.

Mitigation: Confirm the target and destination before DELETE requests or webhook subscriptions; prefer pausing a monitor when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/virlo-ai/skills/short-form-market-research-brain)
- [Virlo API documentation](https://dev.virlo.ai/docs)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown research summaries and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source-post links, performance metrics, and trend snapshots.]

## Skill Version(s):

1.22.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
