## Description: <br>
Converts Markdown or plain text into polished, high-resolution long images and share posters using built-in visual styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and developers use this skill to transform supplied Markdown or plain text into styled local PNG posters or long images for sharing, documentation, notes, and presentation-style summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup workflow may install npm dependencies automatically. <br>
Mitigation: Review the dependency installation behavior before first use and install only in environments where npm package installation is acceptable. <br>
Risk: The export workflow launches headless Chrome and renders supplied HTML. <br>
Mitigation: Avoid rendering remote URLs or untrusted HTML, and run the skill in a constrained workspace when handling external content. <br>
Risk: The skill writes PNG outputs locally and may persist an output-directory setting through shell configuration. <br>
Mitigation: Choose an explicit output directory and do not allow changes to shell startup files unless persistent configuration is intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/text-to-elegant-image) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [styles_reference.md](artifact/resources/styles_reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with HTML/CSS generation steps, shell commands, and local PNG file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local HTML and PNG artifacts; supports configurable output directories, footer options, and style selection.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
