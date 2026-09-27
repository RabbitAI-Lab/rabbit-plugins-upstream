## Description:

Guides agents through retrieving a user's Credit Karma transactions with the fpx CLI for browser-session capture and curl for subsequent requests, without running the Credit Karma MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Credit Karma account holders use this skill to retrieve and paginate their own transaction data from a shell or script without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads signed-in browser cookies and handles live access and refresh tokens for a financial account.

Mitigation: Use only for your own authorized account; keep tokens out of shared files and logs, and revoke or re-sign the session if exposed.

Risk: Saved transaction responses can disclose sensitive financial-account data.

Mitigation: Limit access to response files and remove them when no longer needed.

## Reference(s):

- [Credit Karma transaction request examples](references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/creditkarma-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transaction data may be returned as JSON or tab-separated text when the commands are run.]

## Skill Version(s):

3.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
