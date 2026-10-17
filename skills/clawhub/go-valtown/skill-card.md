## Description:

Guides Go developers in using a typed client to access the Val Town API for vals, files, storage, SQLite, email, and account resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Val Town API access into projects, including managing vals and account resources with a bearer token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Val Town API token could be exposed in code or request logs.

Mitigation: Read the token from VALTOWN_API_TOKEN; never commit it or log Authorization headers.

Risk: Delete, SQL, and email operations can change account data or send messages.

Mitigation: Obtain user approval for these operations and limit them to resources the task owns.

## Reference(s):

- [go-valtown ClawHub release](https://clawhub.ai/psyb0t/skills/go-valtown)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and a Val Town API token for the examples.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
