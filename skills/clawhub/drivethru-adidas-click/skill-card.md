## Description: <br>
Browser-driven adidas Click B2B toolkit that uses Playwright to place purchase orders and run live inventory or wholesale-pricing checks on the adidas Click portal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to draft or submit adidas Click B2B purchase orders, check live stock levels, and calculate wholesale pricing for selected styles, sizes, and quantities. The ordering path can place real purchases when explicitly confirmed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real adidas B2B orders and has no sandbox order path. <br>
Mitigation: Run dry runs first and require explicit user confirmation before using confirm=true. <br>
Risk: The skill intentionally masks browser automation signals to operate through adidas Click anti-bot controls. <br>
Mitigation: Install only when authorized to automate the adidas Click account and after accepting the related legal and compliance risk. <br>
Risk: The skill handles adidas Click credentials and may mutate carts on a shared account. <br>
Mitigation: Store credentials in environment or secret storage, prefer a dedicated account, and require explicit confirmation before cart-deleting workflows. <br>


## Reference(s): <br>
- [adidas Click Portal](https://b2bportal.adidas-group.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/zmtucker/skills/drivethru-adidas-click) <br>
- [order_flow_notes.md](references/order_flow_notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [JSON command output with human-facing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Python and Playwright; credentials may be supplied through environment variables, stdin JSON, or CLI flags.] <br>

## Skill Version(s): <br>
0.6.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
