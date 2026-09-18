## Description:

Searches and reads Loop Returns return and destination data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Loop Returns records, return details, and configured destinations without handling raw API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI from a verified package source or inspect the installer before running it.

Risk: Loop Returns requests and responses are routed through OOMOL.

Mitigation: Confirm this routing is acceptable for sensitive or compliance-bound business data before installing or using the skill.

Risk: Connector inputs depend on live action schemas.

Mitigation: Fetch the action schema before constructing payloads and run only the read actions needed for the user request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-loop-returns)
- [Loop Returns homepage](https://www.loopreturns.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Loop Returns connection page](https://console.oomol.com/app-connections?provider=loop_returns)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing request payloads; read-only actions return Loop Returns data with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
