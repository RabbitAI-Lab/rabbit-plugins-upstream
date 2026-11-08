## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this typed client to connect applications to Intercom workspaces and read or manage customer support data, including contacts, companies, conversations, messages, articles, and tickets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Intercom access tokens can expose workspace data if logged or sent to an untrusted host.

Mitigation: Read the token from INTERCOM_ACCESS_TOKEN, keep it out of source code and logs, use the HTTPS host for the workspace region, and do not forward it to an untrusted pagination host.

Risk: Client operations can change customer data or delete workspace resources, including contacts.

Mitigation: Perform only the actions requested by the user and limit changes or deletions to the requested resources.

Risk: The security review is partial because two local references were unresolved, leaving the evidence incomplete.

Mitigation: Review the complete skill and its references before installation or use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Project homepage](https://github.com/psyb0t/go-intercom)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
