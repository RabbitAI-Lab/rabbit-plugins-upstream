## Description: <br>
Generates structured classroom evaluation rubrics from lesson plan content, supporting text, pasted content, and PDF, Word, or Markdown uploads for primary, secondary, and vocational education. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, curriculum designers, and teaching-support staff use this skill to turn lesson plans into structured classroom assessment rubrics with observable process criteria, scored learning outcomes, and editable previews before file generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read lesson-plan files supplied by the user, which can include sensitive classroom or student context. <br>
Mitigation: Use only lesson-plan files appropriate for the agent session and remove unnecessary personal or sensitive information before processing. <br>
Risk: Excel generation may require a pip install request and depends on referenced helper or example files being present. <br>
Mitigation: Confirm dependency installation before execution and verify the required helper and example files exist before generating the workbook. <br>
Risk: Incomplete lesson inputs can produce partial rubric criteria or require human judgment before use. <br>
Mitigation: Review the Markdown preview, check any missing-field notes, and confirm or revise the rubric before generating the Excel file. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/flyboat403/generating-evaluation-rubrics) <br>
- [ClawHub skill page](https://clawhub.ai/flyboat403/skills/generating-evaluation-rubrics) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown rubric preview with JSON data and an Excel workbook when generation is confirmed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Excel generation may require a local helper script and openpyxl; incomplete lesson metadata is surfaced for user review.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
