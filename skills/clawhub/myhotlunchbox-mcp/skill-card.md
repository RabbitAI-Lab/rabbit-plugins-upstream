## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, and check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access their My Hot Lunchbox account data from a shell or script when the MCP server is unavailable. It provides curl-based recipes for account reads and cautioned account mutations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives shell commands with broad live-account API authority, including actions that can change orders, student records, subscriptions, coupons, and payment state.

Mitigation: Inspect each payload and total before running mutation or payment commands, and prefer the MCP when available because it provides confirm-gated writes and dry-run previews.

Risk: A checkout command can charge a saved payment method.

Mitigation: Use initCheckout first, confirm the returned total, and do not run payment checkout speculatively.

Risk: Repeated failed sign-in attempts can trigger CAPTCHA and block server-side sign-in for the account.

Mitigation: Stop after an invalid_grant response and verify credentials before trying again.

Risk: Write request bodies are documented as unverified against a live account.

Mitigation: Fetch the current model, edit deliberately, post the whole payload only after review, and re-read the resource to confirm the result.

## Reference(s):

- [My Hot Lunchbox endpoint recipes](references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided My Hot Lunchbox credentials and bearer-token handling.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
