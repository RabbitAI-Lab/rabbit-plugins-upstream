## Description: <br>
Chart Craft helps teams generate business charts, apply reusable themes and templates, batch-create charts from CSV data, export charts in PNG, SVG, PDF, or JSON formats, and review chart usage statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business analysts, reporting teams, and developers use this skill to turn structured data and chart instructions into reusable chart configurations, batch-generated report graphics, and exportable chart artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill's local-only privacy claim conflicts with its stated LLM dependency, so chart prompts, source data, filenames, templates, or generated outputs may be exposed unless the publisher clarifies data flow. <br>
Mitigation: Avoid confidential business, financial, or customer data until the publisher documents whether any LLM or network service receives skill inputs or outputs. <br>
Risk: File-writing, batch generation, and scheduled workflow behavior are under-scoped and may overwrite, retain, or place generated artifacts unexpectedly. <br>
Mitigation: Use workspace-scoped output paths, review generated commands before execution, and avoid scheduled or batch workflows until overwrite, retention, and cleanup behavior are clear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chart-craft) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe local chart-generation commands, chart configuration, export settings, and batch-processing workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
