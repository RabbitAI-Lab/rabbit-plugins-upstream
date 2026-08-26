## Description:

Browser-driven adidas Click B2B toolkit for placing purchase orders, checking live inventory and wholesale pricing, reporting restock dates, and retrieving shipment tracking from the adidas Click portal with Playwright.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Retail, operations, and purchasing agents use this skill to automate authorized adidas Click B2B workflows: draft or place purchase orders, check live stock and wholesale pricing, report restock dates, and retrieve shipment tracking by PO number.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place real adidas Click B2B orders when purchase confirmation is enabled.

Mitigation: Run purchase flows with confirm=false for review first, and require explicit authorization before any confirm=true execution.

Risk: First-run browser setup or missing Chromium host libraries may attempt host dependency changes.

Mitigation: Preinstall Playwright, Chromium, and required system libraries in the approved agent environment before deployment.

Risk: Portal credentials, order details, URLs, and captured HTML can expose sensitive business data.

Mitigation: Pass credentials through environment variables or stdin, avoid CLI flags for secrets, and redact live portal HTML and URLs before sharing logs or prompts.

Risk: Browser automation depends on adidas Click page structure and access controls, which can change or block automation.

Mitigation: Use only with authorized adidas Click accounts and monitor live runs, especially after portal changes or when running from new network locations.

## Reference(s):

- [Order flow notes](references/order_flow_notes.md)
- [adidas Click portal](https://b2bportal.adidas-group.com)
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-adidas-click)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON responses from CLI actions, with human-facing markdown guidance from the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions can return order, inventory, pricing, tracking, warning, confirmation-needed, or structured error details.]

## Skill Version(s):

0.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
