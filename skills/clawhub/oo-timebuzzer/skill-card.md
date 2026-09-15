## Description:

timeBuzzer (timebuzzer.com). Use this skill for ANY timeBuzzer request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage timeBuzzer data from an agent through the OOMOL oo CLI, including activities, users, layers, and tiles. It supports read actions directly and requires user confirmation before write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include executing remote installer scripts directly in a shell.

Mitigation: Prefer a signed, versioned, checksum-verified installer or package-manager install before using the oo CLI.

Risk: The skill routes timeBuzzer actions through OOMOL as an intermediary.

Mitigation: Install only when users are comfortable with OOMOL-connected account mediation for timeBuzzer operations.

Risk: Create, update, and delete actions can change or remove timeBuzzer data.

Mitigation: Keep the skill's requirement to confirm exact payloads and effects before write or destructive actions.

## Reference(s):

- [timeBuzzer homepage](https://timebuzzer.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
