## Description:

Guides Go developers in using an unofficial typed client for the Roark voice AI testing and monitoring API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the unofficial Roark client and work with agents, calls, transcripts, simulations, metrics, and other Roark API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Roark bearer credentials may be exposed in code, logs, or shared requests.

Mitigation: Read ROARK_API_KEY from the environment, prefer project-scoped credentials, and never commit or log keys or authorization headers.

Risk: Create, delete, promote, and job-start operations can change a Roark project.

Mitigation: Review those code paths and execute them only when the user explicitly requests the action.

Risk: Calls, transcripts, and recordings may contain private information.

Mitigation: Return only the information needed for the task.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Go client repository](https://github.com/psyb0t/go-roark)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for integrating the client; live API calls require the user's request.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
