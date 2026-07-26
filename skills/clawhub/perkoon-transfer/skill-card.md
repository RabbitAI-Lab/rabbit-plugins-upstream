## Description: <br>
Perkoon Transfer helps agents send, receive, and monitor encrypted P2P file transfers through MCP, CLI, A2A, or browser automation interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alex-vy](https://clawhub.ai/user/alex-vy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to move files between an agent and a human, another agent, or a processing pipeline. It provides guidance for MCP tools, pinned CLI commands, JSON-RPC A2A requests, and browser automation flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables agents to send or receive local files through a third-party file-transfer provider. <br>
Mitigation: Install and use it only when the user trusts Perkoon for the transfer, and confirm every file path before sending. <br>
Risk: Sensitive files may be accessible to anyone who obtains an unprotected share link. <br>
Mitigation: Use password-protected transfers for sensitive files and avoid sending files from sensitive directories without explicit user approval. <br>
Risk: Optional browser automation examples run remote JavaScript locally. <br>
Mitigation: Prefer the pinned CLI or MCP paths, and inspect or verify remote browser scripts before running them. <br>
Risk: Browser automation steps can suppress sender confirmation prompts. <br>
Mitigation: Keep explicit user confirmation for file paths and recipients before starting a transfer. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/alex-vy/skills/perkoon-transfer) <br>
- [Perkoon homepage](https://perkoon.com) <br>
- [Perkoon A2A agent card](https://perkoon.com/.well-known/agent.json) <br>
- [Perkoon integration guide](https://perkoon.com/llms.txt) <br>
- [Perkoon automation docs](https://perkoon.com/automate) <br>
- [Perkoon CLI package](https://www.npmjs.com/package/perkoon) <br>
- [Perkoon MCP package](https://www.npmjs.com/package/@perkoon/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes pinned package versions, JSON event parsing guidance, session status handling, and transfer outcome reporting.] <br>

## Skill Version(s): <br>
2.0.3 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
