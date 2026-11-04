## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that connects to an Intercom workspace. It provides setup and API guidance for reading and updating requested customer support data, conversations, messages, articles, tickets and related resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed bearer token could allow access to the connected Intercom workspace.

Mitigation: Use a minimally scoped token, read it from a protected environment variable, and keep it out of source code, logs, and printed authorization headers.

Risk: Messages, updates, or deletions can affect real customer and workspace data.

Mitigation: Perform these actions only when requested and only on the explicitly requested resources; use the API host for the workspace’s region.

Risk: The unofficial client implementation is not bundled in this review.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Project homepage](https://github.com/psyb0t/go-intercom)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-intercom)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Endpoint-specific setup and API usage guidance.]

## Skill Version(s):

0.8.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
