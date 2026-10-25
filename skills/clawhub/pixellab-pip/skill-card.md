## Description:

Helps users set up PixelLab, choose supported generation routes, create and edit pixel-art assets, animate scenes, and troubleshoot PixelLab workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shilo](https://clawhub.ai/user/shilo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, artists, and other PixelLab users can ask an assistant for setup and API guidance or have it generate, edit, and animate game-ready pixel-art assets through PixelLab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live generation can spend PixelLab credits; auto mode skips future cost-approval prompts.

Mitigation: Review projected costs before enabling auto mode and set a budget or attempt limit for paid work.

Risk: Setup or removal can change local configuration, and remote asset changes can delete or overwrite work.

Mitigation: Review configuration changes and require explicit confirmation of the exact scope before uninstalling or changing existing remote assets.

Risk: Exposing the PixelLab bearer token in chat could compromise the account.

Mitigation: Keep PIXELLAB_SECRET out of chat and configure it only in the approved client or environment.

## Reference(s):

- [PixelLab Pip release](https://clawhub.ai/shilo/skills/pixellab-pip)
- [PixelLab REST v2 documentation](https://api.pixellab.ai/v2/docs)
- [PixelLab MCP documentation](https://api.pixellab.ai/mcp/docs)
- [PixelLab setup guidance](references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance, Image files, JSON blueprints]

**Output Format:** [Conversational guidance and code snippets; generated assets and JSON files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live generation may require PixelLab credentials and consume credits.]

## Skill Version(s):

2.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
