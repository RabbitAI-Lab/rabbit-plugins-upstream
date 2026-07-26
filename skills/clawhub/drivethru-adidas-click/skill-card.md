## Description: <br>
Browser-driven adidas Click B2B toolkit that places purchase orders and checks live inventory or wholesale pricing on the adidas Click portal with Playwright. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and business users use this skill to draft or place adidas Click B2B purchase orders, and to check live stock levels or wholesale net pricing before buying. It is intended for accounts where adidas Click browser automation is authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place a real adidas Click purchase order with no sandbox when confirm=true is used. <br>
Mitigation: Use dry runs first, confirm order details with the user, and only run confirm=true for an intended purchase on an authorized account. <br>
Risk: The skill uses adidas Click credentials and may receive them through environment variables, stdin JSON, or CLI flags. <br>
Mitigation: Treat credentials as secrets, prefer environment variables or stdin JSON, and avoid exposing credentials in shell history or process listings. <br>
Risk: On shared accounts, the skill can create, switch, and delete matching carts while pricing checks briefly create a throwaway cart. <br>
Mitigation: Use the default fresh-cart behavior, keep the DO NOT BUY marker for pricing checks, review warnings, and manually remove any leftover throwaway cart if deletion fails. <br>
Risk: Browser automation may be blocked, stall, or require a one-time Chromium download and display support. <br>
Mitigation: Install the declared Playwright dependency, expect the first-run Chromium download, and use headed mode or Linux Xvfb only where the account and host environment permit it. <br>


## Reference(s): <br>
- [Order Flow Notes](references/order_flow_notes.md) <br>
- [adidas Click B2B Portal](https://b2bportal.adidas-group.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/zmtucker/skills/drivethru-adidas-click) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, guidance] <br>
**Output Format:** [JSON object on stdout, with structured error JSON on failure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Order results can include dry-run status, submitted confirmation number, totals, warnings, out-of-stock decisions, inventory, pricing, and cart deletion status.] <br>

## Skill Version(s): <br>
0.5.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
