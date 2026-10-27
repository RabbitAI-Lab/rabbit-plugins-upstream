## Description:

Unofficial Go client for the Skyvern API, generated with oapi-codegen from the published OpenAPI document. Package skyvern (github.com/psyb0t/go-skyvern) provides typed REST methods for tasks, agents, runs, browser sessions and profiles, credentials, scripts, schedules, tags, artifacts and audit exports. Use when Go code needs Skyvern browser automation or already imports go-skyvern.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Skyvern browser automation into Go projects, including starting or inspecting runs and managing related API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or sensitive request data may be exposed to the selected Skyvern deployment.

Mitigation: Read SKYVERN_API_KEY from the environment, never hardcode or log credentials, and send only the data needed for the requested task.

Risk: Automation runs can interact with external websites and consume credits.

Mitigation: Review and pin the unofficial dependency, check which actions each automation needs, and run or change only resources the user requested.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-skyvern repository](https://github.com/psyb0t/go-skyvern)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go integration examples and API usage guidance; the library itself does not write files.]

## Skill Version(s):

0.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
