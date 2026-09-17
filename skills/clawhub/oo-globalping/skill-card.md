## Description:

Globalping (globalping.io). Use this skill for ANY Globalping request - reading, creating, and updating data. Whenever a task involves Globalping, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Globalping through an OOMOL-connected account, including creating measurements, checking limits and credits, retrieving measurement results, and listing online probes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional installer commands fetch and execute remote shell or PowerShell scripts.

Mitigation: Run installer commands only after reviewing or verifying them, and avoid elevated shells.

Risk: The create_measurement action changes Globalping state.

Mitigation: Confirm the exact payload and expected effect before allowing the skill to create a measurement.

Risk: Connector payloads can drift from the live action contract.

Mitigation: Inspect the live action schema with the oo CLI before constructing payloads.

## Reference(s):

- [Globalping homepage](https://globalping.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-globalping)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Globalping connector results returned through the oo CLI as JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
