## Description:

Analyze construction drawings to extract dimensions, annotations, symbols, and metadata. Support quantity takeoff and design review automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction)

### License/Terms of Use:

MIT

## Use Case:

Construction project managers, estimators, designers, and automation developers use this skill to extract structured information from construction drawings, generate drawing analysis reports, and support quantity takeoff or design review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Construction drawings and generated reports may contain sensitive project names, identifiers, design details, or internal notes.

Mitigation: Review drawings and generated outputs before sharing them outside the intended project team.

Risk: Drawing extraction may miss or misread dimensions, symbols, title block fields, or quality issues.

Mitigation: Validate extracted results against the original drawings before using them for takeoff, design review, or downstream project decisions.

Risk: The skill depends on Python drawing-processing packages such as pdfplumber.

Mitigation: Install dependencies in an isolated Python environment and consider pinning package versions for repeatable behavior.

## Reference(s):

- [Drawing Analyzer ClawHub page](https://clawhub.ai/datadrivenconstruction/skills/drawing-analyzer)
- [Publisher profile](https://clawhub.ai/user/datadrivenconstruction)
- [Data Driven Construction homepage](https://datadrivenconstruction.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, Python code examples, shell commands, and optional CSV, Excel, or JSON export guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided drawing files or project data and can report title block data, dimensions, annotations, symbols, summary statistics, and quality issues.]

## Skill Version(s):

2.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
