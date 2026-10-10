## Description:

Generates preliminary building-decoration cost estimates and material plans from room details and drawings, with CAD measurements retained as inputs requiring review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction estimators and site engineers use this skill to draft decoration quantities, preliminary costs, and material plans while tracking calculations, supporting references, and items needing confirmation. It does not replace formal quotations or final measurements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted CAD-derived measurements or metadata may lead to incorrect estimates.

Mitigation: Review imported measurements against project drawings and resolve flagged inputs before using estimates.

Risk: CAD validation can run an external validator script.

Mitigation: Use a trusted cad-file-reader installation, or disable validation when its validator path is not controlled.

Risk: Generated spreadsheets may contain untrusted project-derived content.

Mitigation: Inspect spreadsheets before sharing or opening them with external content enabled.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [Skill usage and scope](artifact/README.md)
- [Included standards reference rules](artifact/rules/国家规范要求.json)

## Skill Output:

**Output Type(s):** [Guidance, CSV files, Excel spreadsheets, Markdown reports]

**Output Format:** [Markdown report, CSV tables, and six-sheet XLSX workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary estimates require review of missing items, drawing measurements, and reference prices; CC-BY-NC-SA-4.0 restricts commercial reuse.]

## Skill Version(s):

0.9.0 (source: frontmatter, manifest, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
