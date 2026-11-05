## Description:

Provides access to Artsonia student-art portfolios, teacher feedback, comments, fans, and notification settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and fans can use the skill to review a child's artwork and teacher feedback, download portfolio images, and manage comments, fan invitations, and notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and cached sessions can expose access to student-art portfolios.

Mitigation: Use an authorized parent or fan account and protect configuration files and cached session data containing account access.

Risk: Comments and fan invitations affect other people, and some account actions may run without a confirmation step.

Mitigation: Keep MCP_CONFIRM_MODE=ask-user or set it to refuse; review the write preview before approving comments or invitations.

Risk: Artwork downloads may include private pieces, and the external server implementation and its dependencies were not audited in this review.

Mitigation: Set include_private=false when private artwork is not needed, and review and pin the external server version before providing credentials.

## Reference(s):

- [Artsonia MCP package on npm](https://www.npmjs.com/package/artsonia-mcp)
- [Project repository listed in the skill documentation](https://github.com/chrischall/artsonia-mcp)
- [Artsonia MCP on ClawHub](https://clawhub.ai/chrischall/skills/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Images, Files, JSON]

**Output Format:** [Text summaries and structured results, downloaded image files, and optional JSON indexes or metadata sidecars]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected tool and the authenticated Artsonia account; downloads may omit private artwork when include_private is false.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
