## Description:

Short-form video market research via the Virlo API: viral niche research, trend tracking, creator vetting, hashtag, sound, and hook intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[virlo-ai](https://clawhub.ai/user/virlo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to research short-form video markets, compare platform trends, find creators and content formats, and set up ongoing monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to Virlo, which retains research results.

Mitigation: Avoid including confidential or personal information in research queries, and review Virlo's data handling terms before using sensitive topics.

Risk: One-time requests and recurring monitoring can incur prepaid charges, including charges for background runs and checks.

Mitigation: Check the balance and set a budget and cadence before starting; pause monitors when they are no longer needed.

Risk: Autopilot can change monitoring keywords by default.

Mitigation: Review keyword changes and disable autopilot when automatic adjustments are not wanted.

Risk: The skill requires a Virlo API key.

Mitigation: Configure VIRLO_API_KEY in the agent's environment or secret settings, not in chat messages.

## Reference(s):

- [Virlo API Documentation](https://dev.virlo.ai/docs)
- [Virlo Agent Playbook](https://dev.virlo.ai/agent-playbook.txt)
- [Virlo Intent Cookbook](https://dev.virlo.ai/intent-cookbook.txt)
- [Virlo Pricing](https://dev.virlo.ai/pricing)
- [ClawHub Skill Release](https://clawhub.ai/virlo-ai/skills/short-form-market-research-brain)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Market research summaries, comparisons, and recommendations in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include trend, creator, hashtag, sound, hook, and video performance insights.]

## Skill Version(s):

1.31.5 (source: SKILL.md frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
