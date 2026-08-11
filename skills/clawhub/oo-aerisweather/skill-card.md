## Description:

Xweather lets an agent retrieve forecasts, current observations, and place data through an OOMOL-connected Xweather account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Xweather forecasts, latest observations, and place resolution while relying on OOMOL for account connection and credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require one-time installation of the oo CLI and an account connection before it can retrieve weather data.

Mitigation: Install and connect the oo CLI only when needed, and review setup commands before running them.

Risk: Using the connected Xweather account may involve paid API usage or insufficient-credit failures.

Mitigation: Confirm billing expectations before retrying requests that report payment or credit errors.

## Reference(s):

- [ClawHub Xweather skill page](https://clawhub.ai/oomol/skills/oo-aerisweather)
- [Xweather homepage](https://www.xweather.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId when run through the oo CLI.]

## Skill Version(s):

1.0.0 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
