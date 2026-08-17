## Description:

openFDA lets agents search and read openFDA data through an OOMOL-backed oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query public openFDA drug datasets through an OOMOL-connected account. It supports searching drug records and counting common field values while reminding users that results are informational and not medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: openFDA requests are routed through OOMOL as an intermediary.

Mitigation: Install only if users are comfortable using OOMOL for openFDA requests and review the oo CLI login and connection setup before first use.

Risk: Returned openFDA data may be mistaken for medical advice.

Mitigation: Treat results as informational public-data output and require qualified review before any medical, clinical, or regulatory decision.

Risk: CLI authentication, connector scope, connection expiry, or billing status can block execution.

Mitigation: Use the documented recovery paths for oo CLI installation, OOMOL login, openFDA connection refresh, and billing errors only when a command fails.

## Reference(s):

- [openFDA homepage](https://open.fda.gov/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openfda)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public-data queries through the OOMOL CLI; openFDA results are informational and not medical advice.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
