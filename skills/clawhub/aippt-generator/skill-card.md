## Description: <br>
AI 驱动的专业 PPT 生成能力，可在工作汇报、客户提案、季度总结、项目汇报、培训分享等商务演示场景中收集结构化业务内容，生成决策导向的 Markdown PPT 成稿，并导出为可编辑的 .pptx 文件。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincent-chao-lang](https://clawhub.ai/user/vincent-chao-lang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, consultants, sales teams, project managers, and trainers use this skill to turn business inputs into structured, decision-oriented presentation drafts and editable PowerPoint files. It supports reports, proposals, quarterly reviews, project updates, training decks, and direct conversion of existing content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Business presentations may contain sensitive metrics, customer information, budgets, or project details supplied by the user. <br>
Mitigation: Provide only content appropriate for the agent and model environment, and remove or anonymize sensitive information before generation when required. <br>
Risk: Generated slides may contain incorrect, unsupported, or misleading business recommendations if source inputs are incomplete or inaccurate. <br>
Mitigation: Review the generated Markdown and exported PowerPoint before use, checking claims, numbers, and recommendations against the underlying business evidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincent-chao-lang/skills/aippt-generator) <br>
- [Scenario diagnosis configuration](references/scenarios.md) <br>
- [Prompt templates and shared requirements](references/prompt_templates.md) <br>
- [Styling guide](references/styling_guide.md) <br>
- [Gold-standard PPT Markdown example](references/example_output.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown slide draft with chart data blocks, plus shell commands and configuration guidance for exporting editable .pptx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The export script consumes Markdown input and can produce a local PowerPoint file with native charts, selectable themes, custom colors, and font settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
