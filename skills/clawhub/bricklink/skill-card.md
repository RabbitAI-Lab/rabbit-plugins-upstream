## Description: <br>
BrickLink Store API helper/CLI (OAuth 1.0 request signing). Covers orders, store inventory (read + write), catalog, categories, colors, feedback, and push notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and BrickLink store operators use this skill to let an agent run OAuth-signed BrickLink Store API CLI commands for orders, inventory, catalog lookup, pricing, feedback, notifications, and local order or invoice HTML views. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform mutating BrickLink store actions, including order, payment, feedback, and inventory changes. <br>
Mitigation: Install only when the agent is intended to use BrickLink OAuth credentials with store read/write authority, and review every mutating command before execution. <br>
Risk: Order detail and invoice HTML can contain customer order data and may be persisted locally. <br>
Mitigation: Use private workspace or /tmp output paths on trusted machines and delete generated files when no longer needed. <br>


## Reference(s): <br>
- [BrickLink ClawHub skill page](https://clawhub.ai/odrobnik/skills/bricklink) <br>
- [Setup instructions](SETUP.md) <br>
- [BrickLink Catalog Item API](references/catalog-api.md) <br>
- [BrickLink Store Inventory API](references/inventory-api.md) <br>
- [BrickLink Orders API](references/orders-api.md) <br>
- [BrickLink catalog resource representations](https://www.bricklink.com/v3/api.page?page=resource-representations-catalog) <br>
- [BrickLink inventory resource representations](https://www.bricklink.com/v3/api.page?page=resource-representations-inventory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, HTML files] <br>
**Output Format:** [Markdown guidance with shell command invocations, JSON API responses, and optional HTML order or invoice files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and BrickLink OAuth credentials; mutating commands act on a live store account.] <br>

## Skill Version(s): <br>
1.4.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
