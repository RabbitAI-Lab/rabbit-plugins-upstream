## Description: <br>
Pptx Craft helps agents create editable PowerPoint decks from structured dashboard or report data using text-first layout guidance and a bundled Python reference engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanxinluo12345](https://clawhub.ai/user/yuanxinluo12345) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and reporting teams use this skill to produce editable PowerPoint decks from structured dashboard or report data. It is most relevant when the user needs reusable layout guidance, template-aware deck generation, and reviewable PowerPoint output rather than a screenshot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The public skill text describes template and data automation that may not be present in the bundled sample engine without manual adaptation. <br>
Mitigation: Verify or add real template_path and structured-data input handling before using the skill for production reporting. <br>
Risk: Generated decks may be treated as business-ready even though layout, template fit, and source data handling still require review. <br>
Mitigation: Run the engine in a controlled working directory, keep backups of PPT templates, and review generated decks before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanxinluo12345/skills/pptx-craft) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with Python code and shell commands; generated artifacts may include editable .pptx decks and SVG layout previews.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled engine depends on python-pptx and should be adapted to the target template path and structured data before production use.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
