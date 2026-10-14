## Description:

Connects an agent to Artsonia to browse student artwork and activity, manage comments and fans, and update notification preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, fans, and other authorized users can ask an agent to view linked students' artwork, check comments and fans, download images, or manage Artsonia account interactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia account access exposes children's portfolios and potentially private artwork.

Mitigation: Use only an account intended for this connection; exclude private pieces from downloads when they are not needed.

Risk: Artwork downloads and notification changes run without a confirmation step; downloaded metadata may contain comments or teacher feedback.

Mitigation: Review requests before these actions and avoid downloading private artwork or writing metadata sidecars unless necessary.

Risk: Automatic confirmation mode may permit account writes without explicit user approval.

Mitigation: Keep confirmation mode at ask-user or refuse, not auto, and approve comment posts or fan invitations only after reviewing their preview.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [MCP tool responses and optional downloaded artwork images and metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads may include private artwork by default; optional metadata files may include comments and teacher feedback.]

## Skill Version(s):

1.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
