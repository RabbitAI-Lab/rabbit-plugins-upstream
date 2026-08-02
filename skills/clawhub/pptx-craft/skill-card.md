## Description: <br>
PPT Craft converts structured data, dashboards, reports, standard HTML, and design-canvas JSON into editable PowerPoint decks with template-aware layout, spacing checks, previews, and QA reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanxinluo12345](https://clawhub.ai/user/yuanxinluo12345) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and presentation authors use this skill to generate editable .pptx reports from HTML, JSON data models, or canvas exports, including workflows that fill an existing PowerPoint template while preserving its theme and usable content area. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local report, HTML/JSON, PPT template, and output paths as part of normal deck generation. <br>
Mitigation: Run it only on files intended for the presentation workflow, review generated PPTX and QA JSON outputs, and avoid giving it unrelated sensitive directories. <br>
Risk: The security summary identifies a temp-file copy weakness for template handling in shared or multi-user environments. <br>
Mitigation: Avoid sensitive templates in shared environments until template copying uses a unique private temporary file and cleanup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yuanxinluo12345/skills/pptx-craft) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and generated local files such as editable PPTX decks, SVG/PNG previews, QA JSON reports, and input snapshot JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled scripts operate on user-provided local HTML, JSON, PPTX template, and output paths; generated QA reports describe geometry errors, warnings, fill rate, and template usage.] <br>

## Skill Version(s): <br>
1.2.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
