## Description:

Generates preliminary interior decoration estimates and material plans from room types, work details, and reviewed CAD measurement candidates; it does not replace bill-of-quantities settlement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction estimators and project teams use the skill to prepare preliminary interior decoration quantities and material plans from room and finish schedules, then review missing items and project-specific assumptions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious with medium confidence, citing automatic installation and setup of an external CAD dependency, capabilities beyond the stated estimating purpose, and incomplete reference coverage; this does not establish malicious intent.

Mitigation: Before installing, review the setup scripts and dependency source, decide whether the CAD import and additional features are needed, and resolve the missing reference so you can assess the incomplete scan coverage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [Base contract and measurement handoff](references/base-contract.md)
- [Waterproofing standards reference](references/waterproof-standards.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance]

**Output Format:** [XLSX workbooks, CSV files, and a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary estimates and material plans include review items; quantities, standards, and prices require project-specific verification.]

## Skill Version(s):

0.9.33 (source: server-resolved release, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
