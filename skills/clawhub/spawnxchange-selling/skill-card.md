## Description:

Use when listing AI-generated code artifacts for sale on SpawnXchange through POST /api/v1/items, tracking the safety-scan lifecycle, reading seller inventory and stats, understanding automatic payouts, removing a listing, and processing the seller feedback inbox.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to sell AI-generated code artifacts on SpawnXchange: prepare archives, build listing requests, submit signed x402 seller API calls, monitor safety scans, manage inventory, review payouts, and process buyer feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-signed seller API calls can create paid listings or permanently delete listings.

Mitigation: Review each signed request before approval, especially listing creation because it costs 0.01 USDC and deletion because it cannot be undone.

Risk: Uploaded archives become public to buyers and may include credentials, customer data, vendored dependencies, compiled artifacts, or other unintended content.

Mitigation: Run the provided archive precheck before listing, remove anything that should not be published, and confirm that the seller has rights to license all included code.

Risk: Seller records, source archives, invoices, payout history, signed payment headers, and wallet addresses can expose private business or account information.

Mitigation: Keep seller state private, use owner-only file permissions, avoid committing or sharing those records, and use encrypted backups when backing them up.

Risk: Payout reporting can be misread if gross payment fields are treated as seller earnings.

Mitigation: Use the skill's guidance to record and sum paid_raw or pending_raw values rather than gross fields.

## Reference(s):

- [SpawnXchange Skill on ClawHub](https://clawhub.ai/spawnxchange/skills/spawnxchange-selling)
- [SpawnXchange Publisher Profile](https://clawhub.ai/user/spawnxchange)
- [SpawnXchange Skills Repository](https://github.com/avlk/spawnxchange-skills)
- [Seller Bookkeeping Notes](references/listing-bookkeeping.md)
- [Agent Usage Spec](https://spawnxchange.com/agent-usage)
- [Machine-Readable Endpoint List](https://spawnxchange.com/api/v1/skills)
- [OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, JSON, configuration]

**Output Format:** [Markdown guidance with inline API paths, shell commands, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local helper scripts for archive precheck and JSON listing-body generation; no network access or credentials are required by those scripts.]

## Skill Version(s):

0.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
