## Description:

This skill lets an agent operate Wachete through an OOMOL-connected account for reading, creating, updating, and deleting Wachete data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Wachete monitors, folders, history, and notifications through the oo CLI while relying on live connector schemas for action payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes live internet installer commands that could execute unreviewed code if run automatically.

Mitigation: Review the setup path before installation, prefer a verified and versioned oo CLI source with checksum or signature verification, and do not let an agent run the pipe-to-shell installer automatically.

Risk: Write and destructive actions can create, replace, or delete Wachete monitors.

Mitigation: Confirm exact payloads, targets, and expected effects with the user before creating, replacing, or deleting Wachete monitors.

## Reference(s):

- [Wachete homepage](https://www.wachete.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wachete)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Wachete connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
