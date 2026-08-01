## Description: <br>
ERPClaw is an AI-native ERP skill for accounting, invoicing, inventory, purchasing, tax, billing, HR, payroll, advanced accounting, and financial reporting with local-first double-entry ledger operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mailnike](https://clawhub.ai/user/mailnike) <br>

### License/Terms of Use: <br>
GNU General Public License v3 <br>


## Use Case: <br>
Small business owners, operators, and finance teams use ERPClaw to run ERP workflows from plain English, including company setup, invoicing, payments, inventory, payroll, tax, and financial reporting. Developers and administrators can also use it to configure a local ERP database, install approved modules, and expose actions through OpenClaw or MCP-compatible runtimes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad local authority over accounting, payroll, HR, credentials, backups, and installed ERP modules. <br>
Mitigation: Install it only in an account or isolated environment where that authority is acceptable, and require explicit confirmation for high-impact operations. <br>
Risk: Module installation and validation can introduce code-execution or filesystem risk. <br>
Mitigation: Review modules before installing or updating them, avoid validating untrusted modules on the host, and limit module sources to trusted publisher repositories. <br>
Risk: Restore, import, cleanup, and reporting-elimination workflows can materially change business records or reporting outcomes. <br>
Mitigation: Keep current backups, review action details before confirming, and treat these workflows as high-impact business operations. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/mailnike/skills/erpclaw) <br>
- [ERPClaw website](https://www.erpclaw.ai) <br>
- [ERPClaw documentation](https://www.erpclaw.ai/docs) <br>
- [OpenClaw](https://openclaw.org) <br>
- [Pattern catalog](scripts/erpclaw-os/references/pattern_catalog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text or Markdown with optional shell command blocks and JSON action results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may describe or execute local ERP operations; high-impact business operations require explicit user confirmation.] <br>

## Skill Version(s): <br>
4.14.0 (source: frontmatter and changelog, released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
