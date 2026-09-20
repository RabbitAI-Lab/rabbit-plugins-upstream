## Description:

creditkarma-fpx helps agents guide users through querying Credit Karma transaction data from a shell using fpx for one-time browser-cookie capture and curl for GraphQL reads and token refresh.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to retrieve Credit Karma transactions from an authenticated browser session without installing or running the Credit Karma MCP server. It provides setup steps, shell commands, request bodies, pagination guidance, and token-refresh handling for direct Credit Karma API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reuses live Credit Karma session cookies, access tokens, and refresh tokens in shell commands.

Mitigation: Use a trusted single-user machine, keep tokens in shell variables when possible, avoid terminal and session logging, unset token variables after use, and re-sign out or revoke the browser session if exposure is suspected.

Risk: Example commands write request and response JSON files under temporary paths, which can expose financial data or tokens on shared systems.

Mitigation: Replace shared /tmp examples with a private mktemp directory, apply restrictive permissions, clean up response files, and only persist CKAT, ACCESS, or REFRESH in files protected like secrets.

Risk: The skill targets unpublished Credit Karma endpoints and safelisted operation hashes that may change without notice.

Mitigation: Check HTTP status and in-body GraphQL errors before trusting output, treat schema or validation errors as endpoint drift, and refresh or recapture tokens only for documented authentication failure signals.

## Reference(s):

- [Credit Karma request examples](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Credit Karma GraphQL endpoint](https://api.creditkarma.com/graphql)
- [Credit Karma token refresh endpoint](https://www.creditkarma.com/member/oauth2/refresh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, jq, curl, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance assumes a user-controlled authenticated Credit Karma browser session and may produce temporary request or response JSON files when commands are followed.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
