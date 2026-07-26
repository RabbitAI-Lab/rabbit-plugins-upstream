## Description: <br>
Generates SVG visual maps from existing YAML map data in TRPG projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ice26985850](https://clawhub.ai/user/ice26985850) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, game masters, and TRPG content creators use this skill to turn existing YAML map definitions into browser-viewable SVG maps for play sessions and rulebook materials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent reads workspace TRPG map YAML files and creates SVG files next to eligible maps. <br>
Mitigation: Confirm the workspace scope before installation and review generated SVG outputs; the skill directs the agent not to alter source YAML files. <br>
Risk: When YAML maps lack node coordinates, generated SVG layout may be approximate. <br>
Mitigation: Review generated maps before use and adjust coordinates or SVG placement if the layout is unclear. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ice26985850/skills/trpg-yaml-to-svg-maps) <br>


## Skill Output: <br>
**Output Type(s):** [code, files] <br>
**Output Format:** [Standard SVG files generated alongside source YAML maps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates one SVG per eligible YAML map and does not modify existing YAML files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
