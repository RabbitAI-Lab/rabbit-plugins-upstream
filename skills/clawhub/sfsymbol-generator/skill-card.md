## Description: <br>
Generate an Xcode SF Symbol asset catalog .symbolset from an SVG. Use when you need to add a custom SF Symbol (build-time) by creating the symbolset folder, Contents.json, and SVG file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[svkozak](https://clawhub.ai/user/svkozak) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and iOS or macOS engineers use this skill to turn SVG artwork into Xcode SF Symbol .symbolset assets, including Contents.json and optionally template-aligned SVG output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local SVG files and writes generated symbol assets into project paths selected by the user. <br>
Mitigation: Confirm input and output paths before running the scripts, then review generated SVG, JSON, and asset catalog files before committing or shipping them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/svkozak/skills/sfsymbol-generator) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated Xcode asset catalog files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated files include a .symbolset directory, Contents.json, and SVG output in the selected asset catalog path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
