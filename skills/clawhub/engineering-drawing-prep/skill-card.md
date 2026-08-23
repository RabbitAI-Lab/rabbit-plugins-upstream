## Description:

Automated pre-design document preparation for engineering projects. Standardize client DWGs, audit deliverables, extract data tables, and generate RFIs before real design begins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mclyang](https://clawhub.ai/user/mclyang)

### License/Terms of Use:

MIT-0

## Use Case:

Engineering, EPC, MEP, infrastructure, and document-control teams use this skill to prepare messy client deliverable folders before design work starts. It inventories and hashes inputs, stages WIP DWGs, emits audit reports, extracts register data, and drafts RFIs for missing or inconsistent source information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The intake workflow can modify the source folder by removing macOS noise and lock files.

Mitigation: Run the skill only on a copied client deliverable folder and keep originals backed up or read-only.

Risk: Drawing standardization may be overstated because the bundled script copies DWGs to WIP and reports placeholder behavior unless full AutoCAD processing scripts are supplied.

Mitigation: Do not treat WIP DWGs as standardized until layer, font, title-block, plot-setting, and PDF outputs are implemented and independently checked.

Risk: Registers and RFIs are generated from best-effort scans of filenames and readable text, so missing survey, CRS, benchmark, and placeholder findings can be incomplete or false positive.

Mitigation: Have an engineer or document controller review generated reports and RFIs against the original deliverables before issuing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mclyang/skills/engineering-drawing-prep)
- [Industry Standards and Field Lessons](references/industry_standards.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command examples; generated artifacts include JSONL manifests, hash logs, text reports, JSON/CSV tables, RFI JSON, WIP DWG copies, and PDFs when CAD tooling supports export.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed against original client deliverables before being treated as standardized, complete, or design-ready.]

## Skill Version(s):

0.1.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
