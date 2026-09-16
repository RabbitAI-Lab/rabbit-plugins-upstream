## Description:

KlickTipp helps agents operate KlickTipp subscriber workflows through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run KlickTipp subscriber sign-in, sign-off, and sign-out workflows through an OOMOL-connected account. The skill is intended for agents that need to inspect the live connector schema before constructing payloads and confirm account-changing actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The listed KlickTipp actions can change account or subscriber state even when the skill text frames untagged actions as safe reads.

Mitigation: Treat every listed action as account-changing and confirm the email address, payload, and expected effect before running it.

Risk: The setup instructions include remote installer commands that execute downloaded scripts.

Mitigation: Avoid pipe-to-shell installation unless the OOMOL CLI installer source has been independently trusted and verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-klicktipp)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [KlickTipp homepage](https://www.klicktipp.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON and may include data plus meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
