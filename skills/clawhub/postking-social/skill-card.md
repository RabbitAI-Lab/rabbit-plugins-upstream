## Description:

Generate, approve, and schedule social posts on PostKing across LinkedIn, X, Instagram, Threads, and Facebook — plus content weeks and repurposing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsandtea](https://clawhub.ai/user/bitsandtea)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams and operators use this skill to generate, save, approve, schedule, and repurpose social posts across PostKing-supported platforms while managing visuals, assets, account connections, cadence schedules, and platform rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or schedule public social posts, so incorrect copy, platform selection, timezone, or timing can become public-facing.

Mitigation: Review post content, target platform, timezone, and scheduledAt values before approving or scheduling posts.

Risk: The skill can disconnect social accounts and delete posts, assets, templates, or schedules.

Mitigation: Confirm the specific account IDs, post IDs, asset IDs, template IDs, schedule IDs, and irreversible delete or disconnect intent before using destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bitsandtea/skills/postking-social)
- [PostKing MCP endpoint](https://mcp.postking.app/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured tool-call parameters and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include future ISO 8601 scheduling times, platform selections, brand or account IDs, post IDs, and asset identifiers.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
