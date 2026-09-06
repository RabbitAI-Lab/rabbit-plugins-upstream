## Description:

Perkoon Transfer helps agents send and receive files through Perkoon using CLI, MCP, A2A, or browser automation interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-vy](https://clawhub.ai/user/alex-vy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to move files from agent to human, agent to agent, or agent to pipeline through Perkoon transfer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-transfer capability can expose sensitive files or overwrite received files.

Mitigation: Require explicit approval for each file sent, use passwords for sensitive transfers, and verify receive destinations before allowing overwrite behavior.

Risk: Some automation paths may bypass confirmations, run downloaded scripts, or dynamically fetch packages.

Mitigation: Prefer pinned package versions, avoid browser automation commands that skip confirmations or run downloaded scripts, and review generated commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alex-vy/skills/perkoon-transfer)
- [Perkoon homepage](https://perkoon.com)
- [Perkoon A2A agent card](https://perkoon.com/.well-known/agent.json)
- [Perkoon agent integration guide](https://perkoon.com/llms.txt)
- [Perkoon automation documentation](https://perkoon.com/automate)
- [Perkoon CLI package](https://www.npmjs.com/package/perkoon)
- [Perkoon MCP package](https://www.npmjs.com/package/@perkoon/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file-transfer links, session codes, status checks, and receive paths when the agent uses the described workflows.]

## Skill Version(s):

2.1.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
