## Description: <br>
Helps an agent create, edit, price, submit, and confirm BaconCo Odoo sales orders through the drivethru_mcp sales-entry tools, including customer-note review, grid entry, decorations, customizations, preview, and pre-submission checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and sales operations agents use this skill to enter and manage BaconCo custom-apparel sales quotes and orders in Odoo while checking customer notes, decoration requirements, manufactured product construction, and submission readiness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can call live Odoo sales-entry tools with a bearer token for business-critical write actions. <br>
Mitigation: Install only if the publisher and MCP endpoint are trusted, use a least-privilege token, and expose only the intended BaconCo sales tools through the endpoint. <br>
Risk: Order edits, submissions, and confirmations can change live sales and manufacturing workflows. <br>
Mitigation: Confirm every write or order confirmation explicitly, run preview and pre-submission checks before submit or confirm, and prefer submission for human review when final confirmation should remain manual. <br>
Risk: Credential exposure could allow unauthorized Odoo MCP access. <br>
Mitigation: Provide ODOO_MCP_TOKEN through the environment, do not paste it into chat, and rotate or revoke the token if exposure is suspected. <br>


## Reference(s): <br>
- [Drivethru Odoo Sales Assistant on ClawHub](https://clawhub.ai/zmtucker/skills/drivethru-odoo-sales-assistant) <br>
- [Odoo](https://www.odoo.com) <br>
- [Customer Prep](references/customer_prep.md) <br>
- [Order Entry Fields](references/order_entry_fields.md) <br>
- [Grid Build and Apply](references/grid_build_and_apply.md) <br>
- [Decoration Flow](references/decoration_flow.md) <br>
- [Pre-submission Checklist](references/pre_submission_checklist.md) <br>
- [Lessons Learned](references/lessons_learned.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON tool arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses JSON request and response envelopes when calling Odoo MCP tools.] <br>

## Skill Version(s): <br>
0.1.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
