## Description:

Unofficial Go client for the Intercom REST API, generated with oapi-codegen. Package `intercom` (`github.com/psyb0t/go-intercom`) provides typed methods for admins, contacts, companies, conversations, messages, articles, tickets, tags, teams and exports. Use when Go code needs Intercom customer support or workspace data, must perform a requested Intercom action, or already imports go-intercom.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the unofficial go-intercom client and work with Intercom workspace data. It supports requested actions such as sending messages, updating customer records, and deleting contacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Intercom bearer token grants access to workspace data, and API calls can send messages or change and delete records.

Mitigation: Keep the token in INTERCOM_ACCESS_TOKEN, grant only needed scopes, and confirm the requested resources before sending messages or making changes or deletions.

Risk: Credentials could be exposed if sent to an incorrect API host or an untrusted pagination URL.

Mitigation: Use the HTTPS API host for the workspace region and never attach the bearer token to an untrusted pagination host.

Risk: The benign security verdict has medium confidence and scan coverage was partial because two local references could not be resolved.

Mitigation: Review the unresolved references and assess the skill for the intended workspace before use; treat the verdict as benign, not risk-free.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-intercom)
- [Source repository](https://github.com/psyb0t/go-intercom)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-intercom)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks, shell commands, and API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.10.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
