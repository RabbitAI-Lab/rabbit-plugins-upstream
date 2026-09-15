## Description:

This skill helps an agent operate ClickHelp through the OOMOL-connected oo CLI to read, create, and update projects, publications, topics, and portal content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to interact with ClickHelp content from an agent session, including listing and searching projects, retrieving topics, and preparing confirmed topic create or update actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote install scripts executed directly by a local shell.

Mitigation: Use official, versioned, verified oo CLI installation steps and avoid pipe-to-shell setup commands.

Risk: The skill can create or update ClickHelp topics.

Mitigation: Confirm the target project or topic, exact payload, and expected effect with the user before running any write action.

Risk: The skill depends on OOMOL-mediated ClickHelp access.

Mitigation: Install only in environments where OOMOL-mediated ClickHelp access is acceptable, and confirm the connected account and scopes before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-clickhelp)
- [ClickHelp Homepage](https://clickhelp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live ClickHelp connector schemas; write actions require confirmation of the exact payload and effect before execution.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
