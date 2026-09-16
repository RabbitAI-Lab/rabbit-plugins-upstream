## Description:

Zammad lets an agent read, create, and update Zammad data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and agents use this skill to inspect Zammad action schemas, retrieve or search tickets and users, and create or update tickets through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask the agent to run remote oo CLI installer commands.

Mitigation: Review installation before execution; preferably install the oo CLI directly from a trusted, verified source before allowing the skill to proceed.

Risk: Write actions can create tickets, add ticket articles, or update existing tickets in Zammad.

Mitigation: Confirm the exact payload and intended Zammad effect with the user before running any action marked as write.

## Reference(s):

- [ClawHub Zammad skill page](https://clawhub.ai/oomol/skills/oo-zammad)
- [Zammad homepage](https://zammad.com/en)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
