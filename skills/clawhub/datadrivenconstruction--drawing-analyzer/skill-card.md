## Description: <br>
Analyze construction drawings to extract dimensions, annotations, symbols, and metadata. Support quantity takeoff and design review automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction project teams, developers, and engineers use this skill to analyze user-provided PDF or DWG drawing files, extract title block data, dimensions, annotations, and symbols, and support quantity takeoff or design review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided construction drawings may contain confidential project or client information. <br>
Mitigation: Only provide files intended for analysis and review generated reports or exports before sharing them. <br>
Risk: The skill uses filesystem access and a local Python dependency to process drawing files. <br>
Mitigation: Install pdfplumber from a trusted Python package source and limit analysis to expected local drawing paths. <br>


## Reference(s): <br>
- [Data Driven Construction homepage](https://datadrivenconstruction.io) <br>
- [ClawHub Drawing Analyzer skill page](https://clawhub.ai/datadrivenconstruction/skills/drawing-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with structured tables, summary statistics, key findings, and optional export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe extracted drawing metadata, dimensions, annotations, symbols, quality issues, and follow-up export options.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
