## Description:

Perkoon Transfer helps agents send and receive files through Perkoon using MCP tools, CLI commands, the A2A protocol, or browser automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-vy](https://clawhub.ai/user/alex-vy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to transfer files between agents, humans, and processing pipelines. It supports MCP tools, shell-based CLI workflows, A2A JSON-RPC calls, and browser automation paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-transfer workflows can expose unintended files or sensitive content if an agent sends the wrong path.

Mitigation: Confirm exact file paths before sending and require explicit approval before transferring sensitive files.

Risk: Share links without passwords may allow anyone with the link to download the transferred file.

Mitigation: Use password-protected transfers for sensitive files and share the password separately.

Risk: Browser automation instructions include curl-to-node execution and confirmation-skipping steps.

Mitigation: Prefer pinned MCP or CLI paths; use browser automation only after independently verifying scripts and obtaining explicit approval.

## Reference(s):

- [Perkoon Homepage](https://perkoon.com)
- [Perkoon A2A Agent Card](https://perkoon.com/.well-known/agent.json)
- [Perkoon Agent Integration Guide](https://perkoon.com/llms.txt)
- [Perkoon Automation Docs](https://perkoon.com/automate)
- [Perkoon MCP Package](https://www.npmjs.com/package/@perkoon/mcp)
- [Perkoon CLI Package](https://www.npmjs.com/package/perkoon)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, bash, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce file-transfer session links, JSON event parsing guidance, MCP configuration, A2A JSON-RPC payloads, and browser automation steps.]

## Skill Version(s):

2.1.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
