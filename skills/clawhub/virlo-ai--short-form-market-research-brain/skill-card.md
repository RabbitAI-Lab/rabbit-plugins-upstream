## Description:

Short-form video market research via the Virlo API for viral niche research, trend tracking, creator vetting, hashtag, sound, and hook intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[virlo-ai](https://clawhub.ai/user/virlo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, creators, agencies, and developers use this skill to research short-form video niches, discover trends and creators, analyze hashtags and hooks, and configure one-shot or recurring Virlo market-research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate paid Virlo API lookups using a prepaid account balance.

Mitigation: Require confirmation before paid lookups and check the free account balance endpoint before higher-cost or repeated operations.

Risk: Recurring monitors and tracking setups can continue spending credits after creation.

Mitigation: Require confirmation before creating recurring monitors or tracking jobs, and periodically review or pause active monitors.

Risk: The skill can change autonomy settings or modify and delete Virlo resources.

Mitigation: Require explicit approval before DELETE requests, autonomy changes, proposal application, or recurring workflow changes.

Risk: The required Virlo API key is tied to prepaid credits.

Mitigation: Store VIRLO_API_KEY only in the configured environment and avoid exposing it in chat, logs, prompts, or shared files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/virlo-ai/skills/short-form-market-research-brain)
- [Virlo API documentation](https://dev.virlo.ai/docs)
- [Virlo API full reference](https://dev.virlo.ai/llms-full.txt)
- [Virlo pricing](https://dev.virlo.ai/pricing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with curl commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires VIRLO_API_KEY and curl; some API calls consume prepaid Virlo credits or create recurring monitors.]

## Skill Version(s):

1.19.0 (source: server evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
