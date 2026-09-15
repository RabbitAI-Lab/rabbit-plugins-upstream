## Description:

FlowiseAI (flowiseai.com). Use this skill for ANY FlowiseAI request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate FlowiseAI through an OOMOL-connected account, inspect action schemas, fetch the connected chatflow, and send JSON prediction requests after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run unpinned remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified, pinned, or checksum-checked method before using the skill.

Risk: The send_message action sends a JSON prediction request to the connected FlowiseAI chatflow.

Mitigation: Confirm the exact message payload and expected effect with the user before running write actions.

## Reference(s):

- [FlowiseAI homepage](https://flowiseai.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-flowiseai)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
