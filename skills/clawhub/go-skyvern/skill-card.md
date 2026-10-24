## Description:

An unofficial Go client for Skyvern API interactions, providing typed REST methods for browser automation and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Go engineers use this skill to integrate the unofficial go-skyvern client for Skyvern browser automation and API resource management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and request bodies may expose credentials or sensitive data.

Mitigation: Read the API key from the environment, never hardcode or log it, and send only data needed for the requested task.

Risk: Automation can interact with external websites, consume credits, or change resources.

Mitigation: Run automation only when explicitly requested and limit resource changes to resources owned by that task.

Risk: The Go client is unofficial.

Mitigation: Review and pin the dependency before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-skyvern)
- [Project repository (documented homepage)](https://github.com/psyb0t/go-skyvern)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Setup and reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, API calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
