## Description:

wttr.in lets agents retrieve current weather and forecast data from wttr.in through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the wttr.in connector schema and run the read-only get_weather action for current weather and forecast JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI being installed and authenticated before connector commands can run.

Mitigation: Use the documented first-time setup steps only after a command fails because the CLI is missing or unauthenticated.

Risk: Connector payloads can be malformed if the agent assumes input fields without checking the live action contract.

Mitigation: Inspect the action schema with oo connector schema before building and running a JSON payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wttr-in)
- [wttr.in homepage](https://wttr.in/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect the live connector schema before sending JSON payloads and to rely on server-side credential handling.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
