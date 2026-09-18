## Description:

Evenium lets an agent read, create, and update Evenium event and guest data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to retrieve Evenium events and guests, inspect live connector schemas, and run approved Evenium actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installers that execute immediately in a shell.

Mitigation: Prefer a verified package or inspect and verify the downloaded installer before execution.

Risk: Write actions can change sensitive Evenium guest or event data.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged [write].

## Reference(s):

- [Evenium ClawHub release](https://clawhub.ai/oomol/skills/oo-evenium)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Evenium homepage](https://corp.evenium.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
