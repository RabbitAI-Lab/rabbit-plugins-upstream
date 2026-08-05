## Description: <br>
Generates cognitive-science-grounded interactive mind maps from Markdown outlines or JSON, with exports to HTML, PNG, JPG, SVG, PDF, and XMind plus a structure quality report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ftois](https://clawhub.ai/user/ftois) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, researchers, and knowledge workers use this skill to turn notes, articles, meeting summaries, learning material, or structured outlines into editable visual mind maps and shareable export files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes generated mind-map files locally and interactive HTML autosave can overwrite a bound HTML file in supported browsers. <br>
Mitigation: Choose an explicit output path, review generated files before sharing, and only bind autosave to HTML files intended to be overwritten. <br>
Risk: Image and PDF export may trigger optional Pillow installation when the dependency is missing. <br>
Mitigation: In shared or locked-down Python environments, run with --no-auto-install and install Pillow manually inside a virtual environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ftois/skills/generate-mindmap) <br>
- [Mind map content design methodology](references/methodology.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated mind-map files in HTML, PNG, JPG, SVG, PDF, and XMind formats] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; Pillow is optional for image/PDF export and can be installed manually with --no-auto-install.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
