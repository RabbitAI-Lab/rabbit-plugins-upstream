## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl, including sign-in, student lookup, lunch calendar and cart reads, orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, developers, and automation authors can use this skill to inspect and manage a My Hot Lunchbox account from shell scripts when the MCP server is unavailable. It is most useful for account reads, calendar and cart checks, printable reports, and carefully reviewed order or payment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes shell recipes for live account changes, including order changes, account data deletion, and payment checkout.

Mitigation: Review commands before execution and prefer the MCP wrapper for mutations because it provides typed tools, confirmation gates, and dry-run previews.

Risk: Payment checkout can charge a saved payment method.

Mitigation: Run pricing first, confirm the returned total, and do not call checkout speculatively.

Risk: Failed sign-in attempts can escalate to CAPTCHA and remove server-side sign-in for the account.

Mitigation: Stop after an invalid_grant response and verify credentials before trying again.

Risk: Unverified write request bodies can clear omitted data or report success without proving the intended account state changed.

Mitigation: Fetch the full model, inspect the request body, post only after confirmation, and re-read the resource afterward.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [My Hot Lunchbox endpoint reference](references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples, endpoint notes, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill provides curl and jq recipes for authenticated API calls and expects credentials to be supplied through environment variables.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
