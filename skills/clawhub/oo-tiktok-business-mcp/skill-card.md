## Description:

TikTok for Business MCP lets agents inspect and run TikTok for Business connector actions through the OOMOL oo CLI using a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to list TikTok for Business MCP tools, inspect live action schemas, and run search, read, account, or advertising operations through an OOMOL-connected TikTok Business account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic call_tool action can reach tools that change ad accounts, spend, delivery, access, or assets.

Mitigation: Inspect the live schema before building a payload and require explicit user approval for every action that changes spend, delivery, access, assets, or account state.

Risk: The setup guidance includes remote installer commands that execute downloaded scripts in a shell.

Mitigation: Use only independently trusted and verified oo CLI installation sources, or follow a reviewed installation method before running connector commands.

Risk: The skill depends on an OOMOL-connected TikTok Business account with credential handling outside the local agent session.

Mitigation: Use a least-privilege TikTok Business/OOMOL connection and avoid granting broader account scopes than the task requires.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tiktok-business-mcp)
- [TikTok for Business](https://business.tiktok.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live connector schemas, tool lists, execution results, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
