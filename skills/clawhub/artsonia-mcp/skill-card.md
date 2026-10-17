## Description:

Connects an agent to Artsonia student-art portfolios, artwork, comments, fans, and notification settings through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and other authorized Artsonia account holders can ask an agent to browse student artwork and activity, download images, manage fans and comments, and change notification preferences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artsonia credentials and student artwork, comments, and fan information are sensitive.

Mitigation: Use a private environment file or scoped MCP configuration for credentials, and limit access to authorized accounts and exported files.

Risk: Bulk downloads can export private artwork and comments without a confirmation step.

Mitigation: Review download destinations and metadata options, exclude private pieces when appropriate, and restrict or disable session caching.

Risk: Notification changes and feedback-read actions can take effect without explicit confirmation; auto confirmation can bypass user approval for other writes.

Mitigation: Avoid auto confirmation mode and review requested account changes before invoking tools.

## Reference(s):

- [Artsonia MCP on ClawHub](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Text or Markdown responses with optional MCP configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return artwork details and comments, download images and metadata to local storage, and report changes to comments, fan invitations, or notification settings.]

## Skill Version(s):

1.3.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
