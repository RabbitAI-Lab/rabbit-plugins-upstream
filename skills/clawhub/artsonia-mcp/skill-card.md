## Description:

Access Artsonia student-art portfolios, comments, fans, notifications, and artwork downloads through an MCP server registered with the agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to an authorized Artsonia account for viewing student artwork, managing portfolio-related social actions, and downloading artwork records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server exposes sensitive student and account actions that may not be fully disclosed in the skill description.

Mitigation: Review the MCP tool list before installing, use only Artsonia accounts and students the user is authorized to manage, and carefully confirm comment, invite, notification, and feedback-read actions.

Risk: The skill requires Artsonia credentials and can maintain a session cache.

Mitigation: Keep credentials in protected environment or secret storage, and disable the session cache on shared machines.

Risk: Artwork downloads may save private student artwork or metadata to local storage.

Mitigation: Choose a private download destination and set include_private:false when private artwork should not be saved locally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/artsonia-mcp)
- [artsonia-mcp npm package](https://www.npmjs.com/package/artsonia-mcp)
- [artsonia-mcp repository link from skill artifact](https://github.com/chrischall/artsonia-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP setup and propose Artsonia MCP tool use; downloads can write artwork files and metadata when the installed server is used.]

## Skill Version(s):

0.11.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
