## Description: <br>
drivethru-sanmar helps agents work with SanMar catalog, pricing, inventory, purchase-order, tracking, invoicing, return, and purchase-order PDF workflows through deterministic command-line tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Purchasing, operations, and accounts-payable agents use this skill to look up SanMar products, prices, inventory, order status, tracking, invoices, and returns. Authorized agents can also validate and submit SanMar purchase orders after review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles live SanMar account credentials. <br>
Mitigation: Install it only for agents that need SanMar access, prefer environment variables or a secret store, and avoid placing credentials in shared prompts or logs. <br>
Risk: Purchase-order submission can place live vendor orders when confirm=true is used. <br>
Mitigation: Require operator review of purchase-order details before any confirmed submission. <br>
Risk: Raw SOAP payloads or responses may expose passwords or other sensitive account data. <br>
Mitigation: Redact raw_payload and raw_response values before approval or before sharing command outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-sanmar) <br>
- [SanMar homepage](https://www.sanmar.com) <br>
- [SanMar runtime docs index](references/README.md) <br>
- [Authentication, environments, and integration patterns](references/auth_and_patterns.md) <br>
- [SanMar skill agent examples](references/examples.md) <br>
- [SanMar web services](references/web_services.md) <br>
- [Purchase orders](references/purchase_orders.md) <br>
- [Invoicing](references/invoicing.md) <br>
- [Shipment status](references/shipment_status.md) <br>
- [FTP feeds](references/ftp_feeds.md) <br>
- [Returns flow notes](references/returns_flow_notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON command inputs and outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tool calls return a single JSON object on stdout or a structured JSON error.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
