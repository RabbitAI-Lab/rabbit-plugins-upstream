## Description:

Unofficial Go client for the Klavis AI API, generated with oapi-codegen. In package klavis (github.com/psyb0t/go-klavis), the client from klavis.NewClientWithResponses has a typed ...WithResponse method for every endpoint: MCP server discovery, listing and calling tools, MCP server instances and their auth, Strata, users and their integrations, OAuth, white labeling, sandboxes and universes. Auth is a Bearer API key added through a request editor, against the US or EU host. Use when Go code needs to call the Klavis AI API, manage Klavis MCP servers or tool calls, or already imports go-klavis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add and integrate the unofficial Klavis API client, including MCP server discovery and tool calls, instance and user management, OAuth, and sandbox endpoints. It provides setup, authentication, endpoint-selection, and response-handling guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys or downstream authentication data could be exposed, or credentials could be sent to the wrong regional host.

Mitigation: Read the key from KLAVIS_API_KEY, use the account's US or EU host, and never hardcode, commit, or log credentials or returned authentication data.

Risk: Tool calls and instance, authentication, user, or sandbox operations can change remote resources; new instances default to writable when IsReadOnly is omitted.

Mitigation: Make remote changes only when the user requested them, verify MCP server URLs and tool arguments, and explicitly enable read-only instances when appropriate.

Risk: The external Go dependency was not fully audited.

Mitigation: Review the dependency version before adding it.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-klavis)
- [Source repository](https://github.com/psyb0t/go-klavis)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
