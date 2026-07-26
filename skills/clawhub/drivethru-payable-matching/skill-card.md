## Description: <br>
Payable matching for BaconCo that reconciles vendor documents and Sports Inc invoices against Odoo purchase orders, corrects supported PO line price variances, files reviewed documents, and creates draft vendor bills for human posting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance operations agents use this skill to review Odoo Purchasing documents, compare vendor prices against confirmed purchase orders, correct unambiguous price variances, and route unresolved issues for human review. The Sports Inc flow extends the same matching process to API-sourced invoices and creates draft bills that a human must post. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live accounting changes, including PO line price corrections and draft vendor bill creation. <br>
Mitigation: Install only for trusted AP automation agents, use a least-privilege Odoo token, require clear operator approval for batch corrections and draft bills, and keep audit logging enabled. <br>
Risk: Runtime dependency bootstrapping may install Python packages when the host has not preinstalled them. <br>
Mitigation: Prefer host-managed or pinned dependencies, and review the runtime environment before enabling the skill. <br>
Risk: Sports Inc delegated credential sharing can expose an API key to an unintended agent connection if configured incorrectly. <br>
Mitigation: Enable Sports Inc credential sharing only on the intended delegated connection and test the flow in a sandbox or small folder first. <br>


## Reference(s): <br>
- [Matching Procedure](references/matching_procedure.md) <br>
- [Sports Inc Payables](references/sportsinc_payables.md) <br>
- [Odoo](https://www.odoo.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/zmtucker/skills/drivethru-payable-matching) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON command payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational instructions and tool-call payloads for Odoo payable matching; does not post vendor bills automatically.] <br>

## Skill Version(s): <br>
0.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
