## Description:

The unofficial go-skyvern Go client provides typed REST methods for Skyvern browser automation and related API resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate the unofficial go-skyvern client into a project, configure API authentication, call Skyvern endpoints, and handle responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial Go dependency may change or introduce issues.

Mitigation: Review and pin the dependency version before production use.

Risk: API keys and request bodies may contain credentials or sensitive data.

Mitigation: Keep the API key private and send only the data needed for the requested task.

Risk: Automation actions can affect external websites and consume credits.

Mitigation: Authorize website actions carefully and run, cancel, delete, or change only resources the user requested and owns.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [Project homepage](https://github.com/psyb0t/go-skyvern)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.6.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
