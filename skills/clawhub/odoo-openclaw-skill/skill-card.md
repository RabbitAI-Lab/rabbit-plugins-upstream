## Description: <br>
Query Odoo data including salesperson performance, customer analytics, orders, invoices, CRM, accounting, VAT, inventory, and AR/AP, and generate WhatsApp cards, PDFs, and Excel reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ashrf-in](https://clawhub.ai/user/ashrf-in) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, finance teams, and developers use this skill to request read-only Odoo financial, sales, CRM, inventory, VAT, and AR/AP reporting. It helps generate local report outputs such as WhatsApp cards, PDFs, Excel workbooks, and methodology-backed financial summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read sensitive financial and operational data from the configured Odoo account. <br>
Mitigation: Use a least-privilege Odoo API user and install only when that account's readable data is appropriate for the agent. <br>
Risk: The broad raw Odoo read interface may expose more data than a narrow report workflow needs. <br>
Mitigation: Avoid the raw rpc-call command unless necessary and prefer the predefined reporting commands. <br>
Risk: Generated local reports may contain sensitive business data. <br>
Mitigation: Restrict access to generated report files and clean up local outputs when they are no longer needed. <br>
Risk: Dependencies may need maintenance for patched versions. <br>
Mitigation: Update or pin dependencies to patched versions before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ashrf-in/skills/odoo-openclaw-skill) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Autonomous CFO README](artifact/assets/autonomous-cfo/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local report file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce local PDF, Excel, and WhatsApp image card reports from read-only Odoo queries.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
