## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query and manage a My Hot Lunchbox parent account with shell commands when the MCP server is unavailable or when scripting account reads. The skill also documents cautious workflows for order changes, checkout pricing, printable reports, and endpoint error handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent shell-level recipes for live My Hot Lunchbox account changes and payment actions.

Mitigation: Inspect payloads before use, price checkout with initCheckout first, confirm totals out of band, and avoid speculative calls to payment checkout.

Risk: Write request bodies are described as unverified and missing fields may clear existing order data.

Mitigation: Fetch the current model, edit only intended fields, post the full payload, and re-read the resource afterward to confirm the result.

Risk: Repeated failed sign-ins can escalate to CAPTCHA and remove server-side sign-in for the account.

Mitigation: Stop after invalid_grant, verify credentials outside the agent flow, and only retry after correcting the credentials.

Risk: The recommended MCP wrapper provides stronger safeguards than raw shell snippets.

Mitigation: Prefer the MCP wrapper when available because it adds confirm-gated writes and dry-run previews.

## Reference(s):

- [My Hot Lunchbox endpoint reference](artifact/references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command snippets, endpoint recipes, and operational cautions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes account-management and checkout guidance that should be reviewed before execution.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
