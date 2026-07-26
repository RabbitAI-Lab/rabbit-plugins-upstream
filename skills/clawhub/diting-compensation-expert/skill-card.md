## Description: <br>
Diting Compensation Expert supports compensation benchmarking, salary adjustment planning, pay equity analysis, compensation structure design, market percentile analysis, salary band design, and compensation competitiveness assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR, compensation, and leadership users use this skill to analyze compensation benchmarks, salary adjustment options, pay equity, salary bands, and total compensation competitiveness. It is intended for compensation questions and routes non-compensation HR topics to other specialists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Employee-level compensation files can expose sensitive HR data. <br>
Mitigation: Use pseudonyms or employee IDs, remove fields not needed for the analysis, restrict access to authorized HR or leadership users, and delete working files after completion. <br>
Risk: Compensation outputs may be misleading when source data is incomplete, stale, or based on assumptions. <br>
Mitigation: Require data source, year, sample-size, assumption, and confidence labels in outputs, and review recommendations before using them in compensation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tuobadaidai/skills/diting-compensation-expert) <br>
- [Output templates](artifact/references/output-templates.md) <br>
- [Compensation tools](artifact/references/tools.md) <br>
- [Classic compensation books](artifact/references/classic-books.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown reports with tables, risk notes, confidence statements, CSV templates, and Python calculation snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request or reason from sensitive employee-level compensation data; outputs should label assumptions, data sources, and confidence.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release metadata; artifact frontmatter says 2.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
