## Description: <br>
Create SVG images and convert them to PNG without external graphics libraries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lijy2015](https://clawhub.ai/user/lijy2015) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to create SVG illustrations, avatars, logos, and artwork from direct SVG code, then optionally convert SVG files to PNG using the bundled rsvg-convert wrapper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may write generated SVG or PNG files during normal use. <br>
Mitigation: Review output paths before execution and keep generated files in an expected workspace location. <br>
Risk: PNG conversion invokes the local rsvg-convert command on SVG input. <br>
Mitigation: Use trusted SVG inputs where possible and confirm rsvg-convert is installed from a trusted system package. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lijy2015/skills/svg-draw) <br>
- [Publisher profile](https://clawhub.ai/user/lijy2015) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with SVG/XML code, bash commands, and generated SVG or PNG file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write generated SVG and PNG files; PNG conversion depends on local rsvg-convert availability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
