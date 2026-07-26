## Description: <br>
Extracts questions from .xlsx, .xls, .docx, and .pdf exam or question-bank files, evaluates test quality across content validity, structural validity, difficulty control, discrimination potential, and standardization, and generates an interactive HTML visual report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, exam authors, and assessment reviewers use this skill to evaluate exam or question-bank quality after files are uploaded or when multiple papers need comparison. It helps structure questions, compute quality metrics, review low-confidence parsing, score five assessment dimensions, and produce visual HTML reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded exam or question-bank files may contain sensitive student, institutional, or assessment data. <br>
Mitigation: Review files for sensitive content before analysis and delete temporary JSON and generated reports when finished. <br>
Risk: The artifact references helper scripts that may be needed for parsing and report generation but were not included in the evidence bundle. <br>
Mitigation: Verify the parsing, validation, metric, and report scripts before running commands suggested by the skill. <br>
Risk: Generated reports may load Chart.js from an external CDN, which can be unsuitable for highly sensitive reports. <br>
Mitigation: For sensitive deployments, avoid external CDN loading or use a reviewed local chart library asset. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/flyboat403/skills/exam-evaluator) <br>
- [Server-Resolved GitHub Source](https://github.com/flyboat403/exam-evaluator) <br>
- [Bloom Taxonomy Reference](references/bloom_taxonomy.md) <br>
- [Evaluation Criteria Reference](references/evaluation_criteria.md) <br>
- [Question Types Reference](references/question_types.md) <br>
- [Vocational Standards Reference](references/vocational_standards.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON, HTML] <br>
**Output Format:** [Markdown guidance with shell commands, JSON schemas, and generated HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce temporary clean, metrics, duplicates, and evaluation JSON files before writing interactive HTML reports.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
