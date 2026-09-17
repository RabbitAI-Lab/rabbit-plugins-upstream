## Description:

Happy Scribe lets agents manage Happy Scribe transcription, subtitling, translation, order, and export workflows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Happy Scribe via the OOMOL oo CLI, including listing organizations and transcriptions, creating orders and exports, checking order status, updating transcriptions, and deleting transcriptions when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that run downloaded scripts directly in a shell.

Mitigation: Verify the OOMOL CLI installer and source through a trusted channel before running installer commands, or install the CLI through an approved package-management path.

Risk: Write and destructive actions can change or delete Happy Scribe account data.

Mitigation: Confirm the exact action, payload, and affected transcription or order with the user before running write or destructive commands.

## Reference(s):

- [Happy Scribe homepage](https://www.happyscribe.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-happy-scribe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or summarize JSON responses returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
