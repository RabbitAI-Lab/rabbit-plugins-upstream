## Description:

Beamer helps agents read, create, and update Beamer data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Beamer connector schemas, retrieve Beamer data, and create changelog posts after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer scripts that could be run directly in a shell.

Mitigation: Install the oo CLI only from a trusted, versioned source after inspecting or verifying the installer; do not let an agent run the remote installer automatically.

Risk: The create_post action changes Beamer content.

Mitigation: Confirm the exact payload and expected effect with the user before running Beamer write actions.

## Reference(s):

- [ClawHub Beamer skill](https://clawhub.ai/oomol/skills/oo-beamer)
- [Beamer homepage](https://www.getbeamer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live connector schema inspection and JSON command payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
