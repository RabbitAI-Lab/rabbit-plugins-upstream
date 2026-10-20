## Description:

Guides Go developers in using an unofficial typed Skyvern API client for browser automation and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on Go projects use this skill to integrate the unofficial Skyvern client, authenticate requests, and work with automation runs, browser sessions, and related API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skyvern API keys or sensitive request data could be exposed in source control, logs, or unintended requests.

Mitigation: Read the key from the environment, never commit or log credentials, and send only data needed for the requested task to the selected deployment.

Risk: Automation or resource changes could affect external websites or consume credits without the user's intent.

Mitigation: Review tasks, agents, scripts, deletions, and cancellations before execution; act only on user-requested resources.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-skyvern package documentation](https://pkg.go.dev/github.com/psyb0t/go-skyvern)
- [go-skyvern project homepage](https://github.com/psyb0t/go-skyvern)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Client examples require a Skyvern API key; callers handle HTTP errors, polling, and retries.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
