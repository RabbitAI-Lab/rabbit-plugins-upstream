## Description:

Short-form video market research via the Virlo API: viral niche research, trend tracking, creator vetting, hashtag and sound intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arod90](https://clawhub.ai/user/arod90)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research short-form social video markets, discover trending content and rising creators, analyze hashtags and sounds, and configure one-shot or recurring market monitors through Virlo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend funds from a Virlo prepaid account through paid API calls, recurring monitoring, tracking, and data intelligence add-ons.

Mitigation: Require the agent to show the estimated cost and get approval before any paid, recurring, tracking, autonomy, PATCH, PUT, DELETE, or webhook-related action.

Risk: The skill can make account or resource changes through monitoring, tracking, autonomy, and management endpoints.

Mitigation: Prefer read-only calls unless the user explicitly asks for a change, and require confirmation before applying proposals or changing resources.

Risk: The Virlo API key gives an agent access to the user's Virlo account and prepaid balance.

Mitigation: Keep the key in VIRLO_API_KEY, avoid pasting it into chat, and verify balance before paid requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/arod90/skills/short-form-market-research-brain)
- [Virlo API documentation](https://dev.virlo.ai/docs)
- [Virlo API reference for agents](https://dev.virlo.ai/llms-full.txt)
- [Virlo pricing](https://dev.virlo.ai/pricing)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON API payloads, and concise analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires VIRLO_API_KEY and curl; some workflows initiate paid Virlo API calls, recurring monitoring, tracking, or account/resource changes.]

## Skill Version(s):

1.11.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
