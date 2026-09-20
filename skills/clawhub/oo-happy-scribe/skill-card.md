## Description:

Operate Happy Scribe through an OOMOL-connected account for transcription, subtitling, translation, export, listing, update, and delete workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to perform Happy Scribe account actions through the OOMOL connector, including creating orders, checking status, exporting results, and managing transcriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts for the OOMOL CLI.

Mitigation: Use a verified installation method or review the installer source before setup.

Risk: The connector can create orders, update transcriptions, and delete Happy Scribe data.

Mitigation: Require explicit user confirmation before write or destructive actions and confirm the exact payload and target.

## Reference(s):

- [Happy Scribe homepage](https://www.happyscribe.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-happy-scribe)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
