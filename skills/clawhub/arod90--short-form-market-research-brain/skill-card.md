## Description:

Short-form video market research via the Virlo API for viral niche research, trend tracking, creator vetting, hashtag, sound, and hook intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arod90](https://clawhub.ai/user/arod90)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creators, agencies, and product researchers use this skill to research short-form video markets, find rising creators, analyze trends and hashtags, inspect sounds and hooks, and set up recurring social intelligence monitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unexpected prepaid credit spend from paid API calls, recurring monitors, tracking jobs, or data-intelligence and depth add-ons.

Mitigation: Confirm request cost, cadence, platforms, and add-ons before creating monitors or tracking jobs; check balance before paid calls and periodically pause or delete recurring agents that are no longer needed.

Risk: Virlo API key exposure or misuse.

Mitigation: Store VIRLO_API_KEY in the agent environment configuration and avoid asking users to paste the key into chat history.

## Reference(s):

- [Virlo API Documentation](https://dev.virlo.ai/docs)
- [Virlo Full API Reference for Agents](https://dev.virlo.ai/llms-full.txt)
- [Virlo Pricing](https://dev.virlo.ai/pricing)
- [Virlo Agent Playbook](https://dev.virlo.ai/agent-playbook.txt)
- [ClawHub Skill Page](https://clawhub.ai/arod90/skills/short-form-market-research-brain)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Virlo API calls, polling steps, cost notes, trend or creator analysis, recurring monitor setup guidance, and environment-variable configuration.]

## Skill Version(s):

1.14.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
