## Description:

Refiner (refiner.io) helps agents read, create, update, and delete Refiner data through the OOMOL oo connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Refiner contacts, forms, segments, survey responses, reporting, and account information from an OOMOL-connected Refiner account. The skill emphasizes schema-first action execution before building connector payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer channel before use; prefer a verified, pinned, or manually inspected oo CLI installation path.

Risk: Write and destructive Refiner actions can change contact, segment, response, or event data.

Mitigation: Confirm the exact payload and expected effect with the user before writes, and require explicit approval before destructive actions.

Risk: Connector action schemas can change over time.

Mitigation: Fetch the live schema with oo connector schema before building each connector payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-refiner)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Refiner homepage](https://refiner.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
