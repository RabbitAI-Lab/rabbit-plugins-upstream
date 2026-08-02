## Description: <br>
Reconciles vendor documents and Sports Inc invoices against Odoo purchase orders, corrects supported PO price variances, files outcomes, and posts matching vendor bills while escalating ambiguous cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Accounts payable operators and authorized agents use this skill to reconcile BaconCo Purchasing documents and Sports Inc invoices against Odoo purchase orders. It supports unambiguous price corrections, internal log notes, document filing, draft bill creation, matched bill posting, and reviewer escalation for unresolved cases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Odoo accounting records, including PO prices and vendor bill posting. <br>
Mitigation: Install only for agents authorized for the AP workflow; use dry-run or draft modes during validation and post only when invoice totals match within tolerance. <br>
Risk: An overly broad ODOO_MCP_TOKEN could permit unrelated Odoo actions if exposed or mis-scoped. <br>
Mitigation: Treat ODOO_MCP_TOKEN as a secret, never paste it into chat, and confirm the token is scoped to the required AP and document workflow before use. <br>
Risk: Incorrect or ambiguous document matching could create wrong price corrections or payable records. <br>
Mitigation: Correct only when the vendor document unambiguously supports the change; route unresolved PO numbers, vendor mismatches, quantity or line variances, and total mismatches to reviewer escalation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-payable-matching) <br>
- [Odoo](https://www.odoo.com) <br>
- [matching_procedure.md](references/matching_procedure.md) <br>
- [sportsinc_payables.md](references/sportsinc_payables.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON command examples and script-backed Odoo MCP actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ODOO_MCP_URL and ODOO_MCP_TOKEN; helper scripts require python3 and uv.] <br>

## Skill Version(s): <br>
0.7.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
