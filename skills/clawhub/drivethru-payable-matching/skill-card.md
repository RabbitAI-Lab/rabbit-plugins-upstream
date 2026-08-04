## Description: <br>
Payable matching for BaconCo that reconciles vendor documents and Sports Inc invoices against Odoo purchase orders, corrects supported price variances, creates or posts vendor bills only when totals match, and routes unresolved cases for human review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and authorized finance operators use this skill to reconcile live Odoo purchasing and payables records for BaconCo. It supports invoice-to-PO matching, PO price corrections, internal audit notes, document filing, Sports Inc payables creation, and guarded posting when totals reconcile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify live Odoo purchasing and payables records, including PO prices, document filing, chatter notes, draft bills, and posted vendor bills. <br>
Mitigation: Install it only for agents authorized to perform BaconCo/Odoo payables work, confirm the intended Odoo environment, and use draft or dry-run mode for first runs or uncertain posting flows. <br>
Risk: Credential exposure could grant access to the Odoo MCP endpoint or related payables integrations. <br>
Mitigation: Protect ODOO_MCP_TOKEN and SPORTSINC_API_KEY as secrets, avoid pasting them into chat, and restrict runtime access to authorized operators. <br>
Risk: Rendered invoice image directories may contain sensitive payable documents. <br>
Mitigation: Periodically clean rendered image outputs and restrict filesystem access to directories used for document rendering. <br>
Risk: Incorrect matching or premature posting could create inaccurate financial records. <br>
Mitigation: Correct only vendor-supported price variances, route ambiguous quantity, line, vendor, or total mismatches to human review, and post bills only when configured total checks pass. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/drivethru-payable-matching) <br>
- [Odoo](https://www.odoo.com) <br>
- [Payable matching procedure](references/matching_procedure.md) <br>
- [Sports Inc payables procedure](references/sportsinc_payables.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, API Calls, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON tool payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce live Odoo updates, internal log notes, document filing actions, draft vendor bills, and posted vendor bills when configured safeguards pass.] <br>

## Skill Version(s): <br>
0.9.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
