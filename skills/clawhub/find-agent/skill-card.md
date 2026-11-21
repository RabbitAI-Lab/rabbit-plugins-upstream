## Description:

Find an agent, MCP server or tool for a task you cannot do well (a missing tool, a service you cannot reach, a specialist task). Asks ScBee for up to three verified agents that fit, with how to install each. Nothing is installed or run; the human chooses. Use when the user asks "is there an agent or MCP server for this?", "who can do X?", or when you are about to give up on a task for lack of a tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmakt99](https://clawhub.ai/user/hmakt99)

### License/Terms of Use:

MIT-0

## Use Case:

People who need a capability their current tools lack can ask for up to three matching agents or MCP servers and review their descriptions and install instructions. The user chooses whether to take any further action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The short description of the user's need is sent to ScBee to find matches.

Mitigation: Keep it under 200 characters and omit names, secrets, paths, and code, as the skill instructs.

## Reference(s):

- [ScBee agent directory](https://scbee.vercel.app/find)
- [ClawHub find-agent release](https://clawhub.ai/hmakt99/skills/find-agent)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown text with agent descriptions and install command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to three matches; install commands are presented for the human to review.]

## Skill Version(s):

1.1.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
