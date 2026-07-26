## Description: <br>
ERPClaw is an AI-native ERP skill for accounting, invoicing, inventory, purchasing, tax, billing, HR, payroll, advanced accounting, and financial reporting through a local-first business database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mailnike](https://clawhub.ai/user/mailnike) <br>

### License/Terms of Use: <br>
GPL-3.0 <br>


## Use Case: <br>
Small business owners, operators, and their agents use ERPClaw to set up and run accounting, sales, purchasing, inventory, payroll, tax, billing, and reporting workflows from plain-English requests. Developers and administrators can also use it to initialize and maintain a local ERP database with optional approved modules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on a persistent local ERP database containing financial, payroll, banking, backup, and business records. <br>
Mitigation: Install only in a dedicated ERPCLAW_HOME and review database, backup, credential, payroll, and fiscal-close workflows before production use. <br>
Risk: Module install and update flows can fetch user-approved code from GitHub and affect the local ERP installation. <br>
Mitigation: Require explicit human approval for module install/update actions and review the module source and registry workflow before enabling additional modules. <br>
Risk: High-impact actions such as fiscal close, restore, payroll payment files, and schema rollback can be hard to undo. <br>
Mitigation: Require a real human confirmation immediately before these actions and verify current backups before restore or rollback operations. <br>
Risk: Some file and data handling paths are under-scoped according to the security summary. <br>
Mitigation: Avoid exposing arbitrary server file paths for imports and limit runtime access to directories required for the ERPClaw installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mailnike/skills/erpclaw) <br>
- [ERPClaw website](https://www.erpclaw.ai) <br>
- [ERPClaw docs](https://www.erpclaw.ai/docs) <br>
- [OpenClaw](https://openclaw.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with optional shell commands, JSON-like action results, and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces business-facing responses and may invoke local ERP actions that read or mutate a persistent database after appropriate confirmation.] <br>

## Skill Version(s): <br>
4.13.0 (source: frontmatter, changelog, server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
