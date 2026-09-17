## Description:

Bazhuayu helps agents read, create, and update Bazhuayu task data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with connected OOMOL and Bazhuayu accounts use this skill to inspect live action schemas and run Bazhuayu connector actions for task management, execution data, analytics, and export workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes commands that download an installer and execute it directly in a shell.

Mitigation: Use an official, versioned, verifiable oo CLI installation method and review the installer before execution.

Risk: Several Bazhuayu actions can change task state or exported-data acknowledgements.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bazhuayu)
- [Bazhuayu Homepage](https://www.bazhuayu.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce JSON payloads for Bazhuayu connector actions; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
