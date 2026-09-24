## Description:

Short-form video market research via the Virlo API, including viral niche research, trend tracking, creator vetting, hashtag, sound, and hook intelligence across TikTok, YouTube Shorts, and Instagram Reels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arod90](https://clawhub.ai/user/arod90)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to direct an agent through paid Virlo API workflows for short-form video market research, including niche analysis, trend discovery, creator analysis, hashtag and sound research, and recurring monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate paid Virlo API calls using the user's prepaid balance.

Mitigation: Ask the agent to confirm the cost and target before paid calls, and check the Virlo account balance when cost matters.

Risk: Recurring monitors, tracking, and autopilot-style changes can continue producing billed runs or modify monitoring scope.

Mitigation: Confirm cadence, monitored resources, autonomy settings, and reversibility before creating or changing recurring workflows.

Risk: Webhook setup, delete, stop-tracking, apply, dismiss, and revert actions can alter external Virlo resources.

Mitigation: Require explicit confirmation of the resource id and intended action before executing state-changing or destructive API calls.

## Reference(s):

- [Virlo API Documentation](https://dev.virlo.ai/docs)
- [Virlo Full API Reference](https://dev.virlo.ai/llms-full.txt)
- [Virlo Pricing](https://dev.virlo.ai/pricing)
- [ClawHub Skill Page](https://clawhub.ai/arod90/skills/short-form-market-research-brain)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl examples, configuration snippets, and concise analysis summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs often include paid-call cost notes, polling cadence guidance, and API result interpretation.]

## Skill Version(s):

1.19.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
