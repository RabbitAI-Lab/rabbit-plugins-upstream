## Description:

Creates product video ad hooks as coordinated visuals, spoken lines, and text overlays, checks claims against platform rules, and can produce short hook clips when footage is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams and creators use the skill to draft and vary the first seconds of TikTok, Reels, and Meta product videos from buyer language, with claims checked against platform rules. Selected hooks can also be turned into short vertical clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation command is unpinned.

Mitigation: Review the installation source and pin the CLI and skill revision where possible.

Risk: Optional media generation sends images to external AI services, and the available scan is incomplete.

Mitigation: Before generation, confirm which media will be sent to which services and that sharing is allowed; review unresolved references and the incomplete scan.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vargai/skills/product-video-hooks)
- [Varg.ai](https://varg.ai)
- [Varg MCP service](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Video files]

**Output Format:** [Markdown hook list; optional MP4 (9:16) hook clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hook sets align the visual, spoken line, and text overlay; clip generation is optional.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
