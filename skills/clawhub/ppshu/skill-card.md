## Description: <br>
Creates self-contained HTML diagrams, visual explanations, charts, state or flow diagrams, and interactive UI prototypes, then saves them in a numbered gallery outside the user's project repository. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ppshux](https://clawhub.ai/user/ppshux) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, designers, educators, and other agent users use this skill when they want visual or interactive output instead of prose, such as architecture diagrams, process flows, charts, state machines, or clickable HTML prototypes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated diagrams and prototypes are saved persistently under ~/.workbuddy/ppshu by default. <br>
Mitigation: Use PPSHU_DIR or the save_html.py --dir option to redirect output, and periodically delete old generated HTML files or the gallery if retention is not desired. <br>
Risk: The skill can create interactive HTML prototypes, so generated files may contain executable browser JavaScript. <br>
Mitigation: Review generated HTML before sharing or opening it in sensitive contexts, and keep generated diagrams self-contained without external network dependencies. <br>


## Reference(s): <br>
- [HTML drawing cookbook](artifact/references/html_cookbook.md) <br>
- [ClawHub skill page](https://clawhub.ai/ppshux/skills/ppshu) <br>
- [Publisher profile](https://clawhub.ai/user/ppshux) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline HTML, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces self-contained HTML files and a local gallery index under ~/.workbuddy/ppshu by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and manifest.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
