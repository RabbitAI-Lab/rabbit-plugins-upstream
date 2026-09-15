## Description:

Attention connects agents to an OOMOL-managed Attention account to search, read, and analyze conversations, deals, teams, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to retrieve Attention conversations and organization records, then ask Attention to analyze selected conversations or deals through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review and verify the installer source before running setup commands, and prefer a trusted installation path for the oo CLI.

Risk: The skill can read Attention conversations and organization records through the connected account.

Mitigation: Use an account with appropriate scopes and avoid requesting data beyond the user's authorized Attention workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-attention)
- [Attention homepage](https://attention.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected Attention account.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
