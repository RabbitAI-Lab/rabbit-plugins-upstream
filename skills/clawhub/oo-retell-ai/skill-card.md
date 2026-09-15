## Description:

Retell AI lets agents inspect Retell AI data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve and list Retell AI calls, phone numbers, voices, and voice agents through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes internet installer commands that pipe downloaded content directly into a shell.

Mitigation: Install the oo CLI from a verified official package or downloaded installer and validate checksum or signature information before running it.

Risk: The skill reads Retell AI workspace data through OOMOL as an intermediary.

Mitigation: Connect Retell AI deliberately, review the workspace data exposed to the connector, and use an account with only the access needed for the task.

## Reference(s):

- [Retell AI homepage](https://www.retellai.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Retell AI skill](https://clawhub.ai/oomol/skills/oo-retell-ai)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions return JSON data with execution metadata when run through the connector.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
