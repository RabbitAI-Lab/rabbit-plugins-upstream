## Description:

Typebot helps agents search and read Typebot workspaces, bots, bot definitions, and collected results through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Typebot workspaces, bots, bot definitions, and collected results from an OOMOL-connected account without handling raw Typebot tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review the setup path before installation, prefer a pinned or verified official oo CLI release or package manager, and avoid curl-to-bash or Invoke-Expression installation unless the supply-chain risk is accepted.

Risk: Typebot access depends on an OOMOL-connected account and server-side credentials.

Mitigation: Use an account with appropriate read scopes, inspect the live connector schema before each action, and treat the documented operations as read-only get/list workflows once the CLI is installed and connected.

## Reference(s):

- [Typebot homepage](https://typebot.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Typebot skill page](https://clawhub.ai/oomol/skills/oo-typebot)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect each live connector schema before sending a Typebot action payload.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
