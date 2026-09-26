## Description:

Enables an agent to read Peec AI reports and project lists through an OOMOL-connected Peec account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to retrieve Peec AI brand visibility, sentiment, position, share-of-voice, source-domain, source-URL, and project-list data from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running a remote installer script directly in a shell.

Mitigation: Review or manually install the oo CLI from official documentation before allowing an agent to run installer commands.

Risk: The skill accesses Peec AI through an OOMOL-connected account.

Mitigation: Confirm authentication and connection steps yourself, and only install the skill if you trust OOMOL and the Peec AI connector.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-peec)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Peec AI Homepage](https://peec.ai/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and execution metadata.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
