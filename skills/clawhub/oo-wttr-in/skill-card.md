## Description:

Provides current weather and forecast lookups from wttr.in through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the wttr_in connector schema and retrieve current conditions or forecasts as JSON through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote shell and PowerShell installer one-liners.

Mitigation: Review the oo CLI installer source and prefer a trusted, verifiable package or release before installing.

Risk: Weather requests, including locations, are routed through an OOMOL account-backed intermediary.

Mitigation: Confirm that sharing requested locations with OOMOL and wttr.in is acceptable for the use case before running the connector.

Risk: The connector may require OOMOL sign-in or billing before weather requests can complete.

Mitigation: Authenticate only after a command reports an auth failure, and resolve billing issues through the OOMOL console before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wttr-in)
- [wttr.in homepage](https://wttr.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
