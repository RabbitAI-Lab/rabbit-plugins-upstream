## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage a My Hot Lunchbox account from a shell when the MCP server is unavailable or a scriptable curl workflow is preferred. It covers account sign-in, student lookup, lunch calendars, carts, order details, transactions, subscriptions, printable reports, and carefully confirmed write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes account mutation and payment checkout commands that can change orders or charge a real payment method.

Mitigation: Confirm the exact payload and total before any write or checkout command, price the cart with initCheckout first, and prefer the MCP's confirm-gated writes when available.

Risk: Credentials and bearer tokens can leak through command history, logs, or saved local files.

Mitigation: Load credentials from the environment or a silent prompt, keep tokens out of logs, and delete local order or transaction files after use.

Risk: Some write request bodies are documented as unverified and a successful HTTP 200 response may not prove the intended change landed.

Mitigation: Inspect payloads before sending them and re-read the affected resource after each mutation to confirm the final account state.

Risk: Repeated failed sign-in attempts may trigger CAPTCHA or remove server-side sign-in for the account.

Mitigation: Stop after an invalid_grant response and verify credentials before trying again.

## Reference(s):

- [My Hot Lunchbox endpoints](references/endpoints.md)
- [My Hot Lunchbox API base URL](https://ordernow.myhotlunchbox.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-controlled My Hot Lunchbox credentials, bearer-token handling, jq, and review of mutation payloads before execution.]

## Skill Version(s):

0.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
