## Description:

An unofficial typed Go client for reading and managing HubSpot data through the HubSpot API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to make typed HubSpot API requests for CRM and related data. It helps applications read or change HubSpot records without assembling raw HTTP requests by hand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A HubSpot access token can expose account data or permit changes through the API.

Mitigation: Use an environment variable for the token, grant only the scopes required, and never log or print request headers.

Risk: Create, update, archive, delete, merge, or purge requests can change live HubSpot records.

Mitigation: Make these changes only when the user requests them and only on records the task owns.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)
- [Source repository](https://github.com/psyb0t/go-hubspot)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and shell commands with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include calls that read or change live HubSpot data.]

## Skill Version(s):

0.5.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
