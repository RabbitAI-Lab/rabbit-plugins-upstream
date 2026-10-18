## Description:

Guides developers using an unofficial Go client to integrate Skyvern browser automation and manage its API resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Go applications use this skill to set up the Skyvern client, inspect typed API methods, and work with automation runs and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skyvern API keys or authenticated requests could expose credentials.

Mitigation: Read the key from SKYVERN_API_KEY; never hardcode, commit, or log credentials or authenticated requests.

Risk: Automation and resource changes can affect external websites, account resources, and service credits.

Mitigation: Review task, agent, script, credential, schedule, delete, and cancel operations; perform only user-requested actions on intended resources.

Risk: Requests may send sensitive task data to an unintended service deployment.

Mitigation: Use the official Skyvern Cloud URL or a deployment explicitly selected by the user, and send only necessary data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-skyvern)
- [Go client documentation linked by the skill](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Setup and API reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Skyvern API key for authenticated requests.]

## Skill Version(s):

0.2.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
