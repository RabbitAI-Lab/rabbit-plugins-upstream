## Description:

Plausible Analytics helps an agent operate Plausible Analytics through an OOMOL-connected account, including reading analytics, querying breakdowns and timeseries data, and recording events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and analytics users use this skill to let an agent query Plausible Analytics data and run approved event-recording actions through the OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may install the oo CLI through a remote shell installer without integrity checks.

Mitigation: Use official oo CLI installation documentation, review the installer before execution, and get explicit user approval before running installation commands.

Risk: The record_event action can write pageviews or custom events to Plausible Analytics.

Mitigation: Confirm the exact event payload and expected effect with the user before running write actions.

Risk: Using the skill requires OOMOL-mediated access to a connected Plausible Analytics account.

Mitigation: Install only when that access path is acceptable for the account owner and the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plausible-analytics)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Plausible Analytics homepage](https://plausible.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Plausible Analytics icon](https://static.oomol.com/logo/third-party/Plausible%20Analytics.svg)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI connector schema before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
