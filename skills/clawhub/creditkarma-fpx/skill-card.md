## Description: <br>
Query Credit Karma transaction data from a shell by using fpx for one-time cookie capture and curl against Credit Karma transaction and refresh endpoints without running creditkarma-mcp. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to generate shell commands and request patterns for fetching Credit Karma transaction pages, refreshing access tokens, paginating results, and projecting transaction data without installing or running the MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credit Karma session cookies, access tokens, refresh tokens, and transaction data can be exposed through shell history, logs, shared machines, or files. <br>
Mitigation: Use only on trusted non-shared machines, keep tokens in session variables when possible, disable or avoid logging sensitive commands, use private file permissions for any saved data, delete temporary response files, and re-login or revoke sessions if exposure is suspected. <br>
Risk: The skill relies on unpublished Credit Karma endpoints and replayed browser-session credentials, which can fail or change without notice. <br>
Mitigation: Review commands before execution, check HTTP status and in-body GraphQL auth errors before trusting results, refresh only on authentication failures, and stop for schema, validation, authorization, or unexpected response errors. <br>
Risk: A browser-extension bridge must be granted access to Credit Karma session cookies for cookie capture. <br>
Mitigation: Install only if that access is acceptable, restrict browser site access to Credit Karma, and avoid using the workflow on devices or browser profiles that handle unrelated sensitive sessions. <br>


## Reference(s): <br>
- [Credit Karma request examples](references/requests.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/creditkarma-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with shell, JSON, and jq examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes cookie capture, token refresh, GraphQL request construction, pagination, response projection, and error-handling guidance.] <br>

## Skill Version(s): <br>
2.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
