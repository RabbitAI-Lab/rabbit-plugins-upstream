## Description:

Perkoon Transfer helps agents move files to humans, other agents, or pipelines using CLI, MCP, A2A, or browser automation, with cloud relay for small files and WebRTC P2P streaming for larger files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-vy](https://clawhub.ai/user/alex-vy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to send and receive files across agent-to-human, agent-to-agent, and agent-to-pipeline workflows. It supports shell, MCP, HTTP A2A, and browser automation runtimes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser automation examples can execute live remote JavaScript without pinning or checksum verification.

Mitigation: Prefer the pinned MCP or CLI paths, or inspect the downloaded browser automation script and use an integrity or trust mechanism for the exact content before running it.

Risk: File-transfer workflows can expose unintended or sensitive files if the selected path or link handling is careless.

Mitigation: Confirm the exact file path before sending and use password protection for sensitive transfers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alex-vy/skills/perkoon-transfer)
- [Perkoon homepage](https://perkoon.com)
- [Perkoon A2A agent card](https://perkoon.com/.well-known/agent.json)
- [Perkoon agent integration guide](https://perkoon.com/llms.txt)
- [Perkoon automation docs](https://perkoon.com/automate)
- [perkoon npm package](https://www.npmjs.com/package/perkoon)
- [@perkoon/mcp npm package](https://www.npmjs.com/package/@perkoon/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pinned CLI and MCP package versions plus JSON event-stream examples for automation.]

## Skill Version(s):

2.1.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
