## Description:

Query Credit Karma transactions from a shell with fpx and curl by capturing signed-in session cookies once, then calling the GraphQL transactions endpoint directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation users can use this skill to retrieve Credit Karma transaction data from shell scripts without running the creditkarma-mcp server. It is intended for workflows where the user already has an authenticated Credit Karma browser session and needs command-oriented guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow extracts live Credit Karma session cookies and reusable access or refresh tokens for a sensitive financial account.

Mitigation: Use it only on trusted local machines, keep tokens in shell variables when possible, and do not expose ACCESS, REFRESH, CKAT, or CKTRKID in logs, screenshots, shell history, or shared files.

Risk: Example commands may write transaction responses or token material under /tmp.

Mitigation: Avoid persistent files where possible; when files are necessary, restrict permissions and delete temporary request, response, and refresh files after use.

## Reference(s):

- [Credit Karma request examples](artifact/references/requests.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes commands for cookie capture, transaction pagination, token refresh, response checks, and local secret-handling precautions.]

## Skill Version(s):

2.8.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
