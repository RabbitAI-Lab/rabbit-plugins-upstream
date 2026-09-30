## Description:

Research short-form video niches, trends, creators, hashtags, sounds, and hooks across TikTok, YouTube Shorts, and Instagram Reels using the Virlo API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[virlo-ai](https://clawhub.ai/user/virlo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and research teams use this skill to discover winning short-form video formats, assess creators, and monitor emerging topics for content strategy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent sends research terms, creator handles, hashtags, and video URLs to Virlo using a Virlo API key.

Mitigation: Share only intended research data and provide the API key through configured credentials, not chat.

Risk: Paid lookups, recurring monitors, tracking, resumes, and cadence changes can create ongoing charges.

Mitigation: Require confirmation before each paid request or change to recurring activity; review balance and pause unneeded monitoring.

Risk: Remote DELETE calls can permanently remove research or monitoring resources.

Mitigation: Require explicit confirmation before deletion and prefer pausing when possible.

Risk: Webhook setup can send research updates to an external endpoint.

Mitigation: Confirm the destination before setup and secure the webhook endpoint with a secret header.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/virlo-ai/skills/short-form-market-research-brain)
- [Virlo API documentation](https://dev.virlo.ai/docs)
- [Virlo agent playbook](https://dev.virlo.ai/agent-playbook.txt)
- [Virlo intent cookbook](https://dev.virlo.ai/intent-cookbook.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research summaries with video and creator metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Virlo API results; paid lookups and recurring monitoring may incur charges.]

## Skill Version(s):

1.22.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
