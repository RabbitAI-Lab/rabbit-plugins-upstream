## Description:

Short-form video market research via the Virlo API for viral niche research, trend tracking, creator vetting, hashtag, sound, and hook intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arod90](https://clawhub.ai/user/arod90)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, creators, and analysts use this skill to research short-form video markets, discover trends and creators, analyze hashtags, inspect hooks, and set up recurring niche or creator monitoring through the Virlo API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics, creator handles, video URLs, hashtags, and related social-media data are sent to Virlo under the user's API key.

Mitigation: Install and use the skill only when this external data sharing is acceptable for the user's workflow and data policies.

Risk: Recurring monitors, tracking jobs, and optional add-ons can create ongoing paid activity.

Mitigation: Confirm cadence, selected add-ons, and expected costs before creating recurring or tracking resources.

Risk: The required VIRLO_API_KEY grants access to paid Virlo API usage.

Mitigation: Store VIRLO_API_KEY only as a configured secret or environment variable and do not paste it into chat history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arod90/skills/short-form-market-research-brain)
- [ClawHub publisher profile](https://clawhub.ai/user/arod90)
- [Virlo API documentation](https://dev.virlo.ai/docs)
- [Virlo full API reference](https://dev.virlo.ai/llms-full.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Virlo API responses to produce market research summaries, trend analysis, creator recommendations, monitoring setup guidance, and API call examples.]

## Skill Version(s):

1.13.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
