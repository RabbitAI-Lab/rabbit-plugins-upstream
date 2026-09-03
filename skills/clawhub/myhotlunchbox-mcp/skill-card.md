## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, and check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and automate My Hot Lunchbox account tasks from a shell when the MCP server is unavailable or unsuitable. It is most useful for account reads, calendar and cart checks, printable reports, and carefully reviewed account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes shell commands that can perform real account changes and payment checkout.

Mitigation: Install only when this shell-based access is intentional; before executing write or checkout commands, verify the exact order IDs, amount, student, and payment method.

Risk: Failed sign-in retries can escalate to CAPTCHA and block server-side sign-in for the account.

Mitigation: Do not retry after an invalid_grant response; stop and verify credentials before trying again.

Risk: Write request bodies are documented as unverified and incomplete payloads can clear account data.

Mitigation: Fetch the current model, inspect the complete payload before posting, and re-read the resource afterwards to confirm the intended change.

Risk: The server evidence flags the release as suspicious because it can use credentials for account changes.

Mitigation: Prefer the MCP for writes when available because it provides confirm-gated mutations and dry-run previews.

## Reference(s):

- [My Hot Lunchbox endpoint reference](references/endpoints.md)
- [My Hot Lunchbox service API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl, jq, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may use user-provided My Hot Lunchbox credentials and can perform real account changes or payment checkout if executed.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
