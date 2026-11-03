## Description:

Guides Go developers in using an unofficial typed client to call the Vercel REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and work with a typed Vercel API client, including authentication, team selection, request parameters, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vercel API operations can change or delete live projects, deployments, domains, DNS records, environment variables, and teams.

Mitigation: Confirm the intended account or team and resource, and make live changes only when the user requested them.

Risk: The client uses a Vercel access token and depends on an external Go module that is not bundled with the skill.

Mitigation: Use a token limited to the needed resources, keep it out of logs and source control, and review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-vercel project](https://github.com/psyb0t/go-vercel)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-vercel)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-vercel)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup and usage guidance with code examples]

## Skill Version(s):

0.17.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
