## Description: <br>
Deterministic SanMar API toolkit that wraps SanMar SOAP web services and PromoStandards order-shipment services behind typed CLI tools for product search, inventory, pricing, purchase-order workflows, PO PDF parsing, and color-code resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations agents use this skill to query SanMar catalog, inventory, pricing, order status, and tracking data, and to prepare or submit SanMar purchase orders through deterministic JSON-in/JSON-out CLI actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SanMar account credentials can be exposed through normal tool inputs or command transcripts. <br>
Mitigation: Prefer environment variables or a managed secret channel, avoid inline credentials when possible, and do not share raw command transcripts containing credential-bearing payloads. <br>
Risk: Purchase-order actions can place external orders when confirmed. <br>
Mitigation: Run pricing and cart validation first, review the order with the user, and submit only when explicit confirmation is present. <br>
Risk: Purchase-order dry runs or raw outputs can expose sensitive order details before payload redaction is fixed. <br>
Mitigation: Keep previews and outputs in trusted channels and avoid copying them into logs, tickets, or chat history. <br>


## Reference(s): <br>
- [SanMar Skill Examples](references/examples.md) <br>
- [SanMar Web Services](references/web_services.md) <br>
- [Purchase Orders](references/purchase_orders.md) <br>
- [FTP Feeds](references/ftp_feeds.md) <br>
- [Authentication and Patterns](references/auth_and_patterns.md) <br>
- [SanMar Website](https://www.sanmar.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/zmtucker/sanmar) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON objects from CLI actions, with Markdown guidance in the skill documentation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions return structured results; purchase-order submission requires explicit confirmation; failures return normalized JSON errors.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
