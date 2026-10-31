## Description:

Local-first TikTok Growth OS for strategy, hooks, scripts, retention design, and analytics feedback that generates execution-ready outputs and stores assets locally without TikTok API access, posting, or platform automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticio](https://clawhub.ai/user/agenticio)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, social media operators, and content strategists use this skill to plan TikTok positioning, content pillars, hooks, short-form scripts, captions, retention improvements, and performance reviews. It can optionally save profile details, content assets, manually entered analytics, and pattern reports to local JSON files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local JSON storage may retain TikTok profile details, unpublished content ideas, scripts, captions, notes, and manually entered performance metrics.

Mitigation: Avoid saving sensitive private business plans unless local retention is acceptable, and review or delete files under ~/.openclaw/workspace/memory/tiktok/ when they are no longer needed.

Risk: Strategic content recommendations can be incorrect, misleading, or misaligned with platform rules or brand requirements.

Mitigation: Review generated hooks, scripts, captions, and analytics interpretations before use, and ensure final posts comply with applicable platform and brand policies.

## Reference(s):

- [Hooks](references/hooks.md)
- [Retention](references/retention.md)
- [ClawHub Skill Page](https://clawhub.ai/agenticio/skills/tiktok)
- [Publisher Profile](https://clawhub.ai/user/agenticio)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and local JSON-backed records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores optional TikTok profile details, content assets, analytics, and pattern reports as local JSON files under ~/.openclaw/workspace/memory/tiktok/.]

## Skill Version(s):

3.0.0 (source: release evidence and skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
