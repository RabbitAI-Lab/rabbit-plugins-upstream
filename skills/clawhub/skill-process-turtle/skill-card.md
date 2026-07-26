## Description: <br>
生成项目流程可视化图表；支持乌龟图(5M1E)、泳道图、流程图、时间线等多种模板；用户需要绘制项目流程图、过程乌龟图或导出流程可视化时使用 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, quality teams, and process analysts use this skill to turn structured process descriptions into turtle diagrams, swimlane diagrams, flowcharts, and timelines. The skill helps prepare local SVG or PNG visuals for reports, presentations, and project documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SVG or PNG diagrams may contain incorrect process details if the source description is incomplete or untrusted. <br>
Mitigation: Review generated diagrams before sharing, especially when source text came from an untrusted party. <br>
Risk: The script reads a JSON config and writes output files using caller-provided paths. <br>
Mitigation: Keep config and output paths inside the project workspace. <br>
Risk: PNG output requires the optional cairosvg dependency. <br>
Mitigation: Use SVG output as the fallback when cairosvg is unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-process-turtle) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-process-turtle) <br>
- [Template reference](references/templates.md) <br>
- [Diagram generator script](scripts/process_turtle.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and shell commands; generated local artifacts are SVG or PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads a user-provided JSON config and writes diagram files in the current workspace; PNG export depends on cairosvg.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
