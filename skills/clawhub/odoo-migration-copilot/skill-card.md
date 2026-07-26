## Description: <br>
Plan and de-risk Odoo version upgrades using odoo-mcp's migration workbench to audit custom addons, classify upgrade-log failures, resolve model renames, and preview JSON-2 payloads for XML-RPC migration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuanle96](https://clawhub.ai/user/tuanle96) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan Odoo upgrades, inspect addon and migration risks, turn rehearsal failures into an ordered worklist, and prepare integrations for Odoo's XML-RPC sunset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Migration work can touch sensitive business records, addon source code, and staged data writes. <br>
Mitigation: Configure odoo-mcp for the intended staging database, keep rehearsal fixes out of production, and review gated data-write steps batch by batch. <br>
Risk: Upgrade-log analysis can produce misleading work items if the input log slice is incomplete or guessed. <br>
Mitigation: Require the relevant pasted log evidence before classifying failures, then preserve evidence lines in the worklist for review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tuanle96/skills/odoo-migration-copilot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with worklist tables and inline command or configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a phase-status header, ordered action table, and go/no-go recommendation with open needs_script count.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
