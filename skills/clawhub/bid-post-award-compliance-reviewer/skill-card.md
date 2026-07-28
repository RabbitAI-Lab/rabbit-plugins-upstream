## Description: <br>
Reviews post-award procurement and construction project compliance by comparing tender, bid, contract, change, acceptance, settlement, personnel, subcontracting, claims, and audit materials against built-in dual procurement-law and tendering-law guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, construction, contract-management, compliance, and audit users use this skill to structure post-award review, compare project documents, identify change, personnel, subcontracting, cost, acceptance, claim, and audit risks, and produce evidence-linked compliance findings. It is intended to support review workflows, not to replace legal, audit, or administrative determinations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intended for sensitive procurement, construction, contract, personnel, subcontracting, and audit materials. <br>
Mitigation: Use it only with documents the user is permitted to process, avoid unnecessary sensitive identifiers, and follow the skill's data-minimization guidance. <br>
Risk: Optional local archives may retain structured project data on the user's machine. <br>
Mitigation: Create archive files only after explicit user request and informed consent, store only structured review fields, and support deletion on request. <br>
Risk: Compliance findings may be mistaken for final legal, audit, or administrative determinations. <br>
Mitigation: Keep disclaimers visible, cite source documents and applicable rules, and direct users to qualified professionals or competent authorities for major determinations. <br>
Risk: Knowledge-base integrations may be unavailable, stale, or not mounted in the user's environment. <br>
Mitigation: Declare degraded operation when live IMA knowledge-base lookup is unavailable and rely on the bundled snapshot only with a recommendation to verify current rules. <br>


## Reference(s): <br>
- [README](artifact/README.md) <br>
- [Knowledge Base](artifact/references/knowledge-base.md) <br>
- [Output Templates](artifact/references/output-templates.md) <br>
- [Function Routing](artifact/references/function-routing.md) <br>
- [Constraints](artifact/references/constraints.md) <br>
- [IMA Knowledge Base Catalog](artifact/references/ima_kb_catalog.md) <br>
- [Archive Schema](artifact/references/archive-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown reports, tables, checklists, risk ratings, threshold calculations, and structured project snapshots] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May optionally maintain structured project archive data only after explicit user consent; otherwise project state remains in the current conversation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
