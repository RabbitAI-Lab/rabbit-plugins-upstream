## Description:

Perkoon Transfer lets agents send and receive files through Perkoon using MCP tools, CLI commands, JSON-RPC A2A calls, or browser automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-vy](https://clawhub.ai/user/alex-vy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to transfer files between an agent and a human, another agent, or a pipeline through Perkoon. It covers setup and operation through MCP, CLI, A2A JSON-RPC, and browser automation interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags instructions that can run unverified website code.

Mitigation: Use pinned CLI or MCP package versions where possible, and review browser automation scripts before downloading and running them.

Risk: The skill can transfer selected local files and may expose data through a share link if the wrong file or recipient is used.

Mitigation: Confirm the exact file path, recipient, and session before sending, and use a password for sensitive files.

Risk: Receiving files with overwrite behavior can replace existing local files.

Mitigation: Receive into a new empty directory unless overwriting existing files is explicitly intended.

Risk: Browser automation guidance can bypass confirmation prompts.

Mitigation: Avoid prompt-bypass automation unless the operator has reviewed the flow and trusts the script source.

## Reference(s):

- [Perkoon homepage](https://perkoon.com)
- [Perkoon A2A agent card](https://perkoon.com/.well-known/agent.json)
- [Perkoon agent integration guide](https://perkoon.com/llms.txt)
- [Perkoon automation documentation](https://perkoon.com/automate)
- [Perkoon MCP server package](https://www.npmjs.com/package/@perkoon/mcp)
- [Perkoon CLI package](https://www.npmjs.com/package/perkoon)
- [ClawHub skill page](https://clawhub.ai/alex-vy/skills/perkoon-transfer)
- [Publisher profile](https://clawhub.ai/user/alex-vy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file-transfer session URLs, status events, save paths, and operational guidance.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
