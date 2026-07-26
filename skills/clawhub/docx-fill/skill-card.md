## Description: <br>
Docx Fill generates Word documents by filling .docx templates with content from reference materials while preserving the original document styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neuhanli](https://clawhub.ai/user/neuhanli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document authors use this skill to generate structured Word documents from .docx templates and source materials. It is especially suited for table-heavy templates such as project proposals, lesson plans, curriculum standards, course outlines, and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated document may silently clear undeclared table cells. <br>
Mitigation: Review or diff the generated document, declare template static text and fill locations carefully, and keep the output path separate from the original template. <br>
Risk: The local workflow reads user-provided templates and reference files and writes a new Word document. <br>
Mitigation: Install and run the skill only when local file access is acceptable, use explicit input and output paths, and avoid providing unrelated sensitive files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/docx-fill) <br>
- [Fill Contract Schema](references/fill_contract_schema.md) <br>
- [Structure Agent](references/structure_agent.md) <br>
- [Content Agent](references/content_agent.md) <br>
- [Conflict Checker](references/conflict_checker.md) <br>
- [Evaluator](references/evaluator.md) <br>
- [Evaluation Rules](references/evaluation_rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, intermediate JSON contracts and content, and generated .docx file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Preserves template styles where supported; generated documents should be reviewed because undeclared table cells may be cleared.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
