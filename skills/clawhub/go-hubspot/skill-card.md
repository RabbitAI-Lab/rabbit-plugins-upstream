## Description:

Provides Go developers with typed methods for reading and managing HubSpot API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill when writing Go code that integrates with HubSpot. It provides setup guidance, typed API examples, and endpoint lookup instructions for reading or changing HubSpot data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HubSpot access tokens could expose account data if committed or written to logs.

Mitigation: Read tokens from environment variables, use the minimum required scopes, and never print or log authorization headers.

Risk: Create, update, archive, delete, merge, and purge operations can change live HubSpot records.

Mitigation: Identify the intended records and make changes only when the user requested them and the task owns those records.

Risk: The integration depends on an unofficial Go library whose downloaded code is outside this documentation review.

Mitigation: Pin the dependency version and review its code before production use.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-hubspot package documentation](https://pkg.go.dev/github.com/psyb0t/go-hubspot)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.4.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
