## Description:

Guides developers using an unofficial Go client to integrate Skyvern browser automation and manage Skyvern resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to configure the Skyvern client, start and inspect browser automation runs, and manage related API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed Skyvern API key could allow unauthorized API access.

Mitigation: Read SKYVERN_API_KEY from the environment; do not hardcode, commit, or log credentials or authenticated requests.

Risk: Automation runs and resource changes may affect external websites, stored account data, and credits.

Mitigation: Review code that starts agents, handles credentials or schedules, or changes resources; act only on explicitly requested tasks and resources.

Risk: Requests may send sensitive browser instructions or data to an unintended endpoint.

Mitigation: Choose the Skyvern endpoint deliberately and include only data needed for the requested task.

## Reference(s):

- [go-skyvern skill listing](https://clawhub.ai/psyb0t/skills/go-skyvern)
- [go-skyvern setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Go toolchain and a Skyvern API key for authenticated use.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
