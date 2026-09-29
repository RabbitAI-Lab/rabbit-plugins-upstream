## Description:

Pulsetic (pulsetic.com). Use this skill for Pulsetic requests that search and read monitor data through the OOMOL Pulsetic connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Pulsetic connector schemas and run read-only Pulsetic monitor lookups, listings, uptime, downtime, response-time, check history, event history, and snapshot queries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into shell interpreters.

Mitigation: Review the OOMOL installer source and official install path before allowing an agent to run the installer commands.

Risk: The security verdict is suspicious because setup behavior requires user review even though connector behavior is purpose-aligned.

Mitigation: Install and authenticate the oo CLI manually or under explicit user approval before running Pulsetic connector actions.

## Reference(s):

- [Pulsetic homepage](https://pulsetic.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pulsetic)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
