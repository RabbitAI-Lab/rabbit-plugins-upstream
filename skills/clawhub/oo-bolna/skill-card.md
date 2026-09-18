## Description:

Bolna lets agents inspect action schemas and read Bolna workspace, voice agent, execution, and log data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Bolna connector schemas and retrieve authenticated Bolna account data such as agents, executions, raw logs, user details, wallet status, and execution history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup guidance could execute unreviewed code.

Mitigation: Prefer a verified official installation method and avoid running pipe-to-shell installer commands directly.

Risk: The skill can access authenticated Bolna account data through the connected OOMOL account.

Mitigation: Use it only for explicit Bolna account-data tasks and review requested reads before execution.

Risk: Broad routing language may cause the skill to be selected for Bolna-related requests where direct account access is unnecessary.

Mitigation: Limit use to tasks that require inspecting Bolna schemas or reading Bolna account, agent, execution, log, user, wallet, or history data.

## Reference(s):

- [ClawHub Bolna Skill](https://clawhub.ai/oomol/skills/oo-bolna)
- [Bolna Homepage](https://www.bolna.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-oriented Bolna connector actions and should inspect live action schemas before constructing requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
