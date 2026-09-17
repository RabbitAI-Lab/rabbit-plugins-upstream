## Description:

Avochato (avochato.com). Use this skill for reading, creating, and updating Avochato data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to list and retrieve Avochato contacts and messages, send text messages, and upsert contacts through the OOMOL `oo` CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Review the setup instructions before installing, prefer a verified package or checksum/signature-checked installer, and only run installation commands when setup actually fails.

Risk: Write actions can send messages or change Avochato contacts.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions such as `send_message` or `upsert_contact`.

## Reference(s):

- [Avochato homepage](https://www.avochato.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Avochato skill page](https://clawhub.ai/oomol/skills/oo-avochato)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON from the `oo connector run` command, including `data` and `meta.executionId`.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
