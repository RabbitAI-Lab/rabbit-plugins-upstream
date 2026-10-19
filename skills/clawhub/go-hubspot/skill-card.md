## Description:

Guides Go developers in using an unofficial typed HubSpot API client to read and update HubSpot data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this guidance to add the Go HubSpot client to a project, locate typed API methods, and handle authenticated CRM and other HubSpot requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot access tokens or sensitive request details may be exposed in code or logs.

Mitigation: Use least-privilege scopes, keep tokens in environment variables or a secrets manager, and avoid logging headers or full URLs.

Risk: Create, update, delete, archive, merge, or purge calls can alter live HubSpot data.

Mitigation: Confirm the intended records and review any data-changing operation before running it against a live account.

## Reference(s):

- [Skill setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-hubspot)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for typed API requests and response handling]

## Skill Version(s):

0.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
