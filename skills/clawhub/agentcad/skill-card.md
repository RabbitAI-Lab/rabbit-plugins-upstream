## Description: <br>
agentcad is a CAD tool for AI agents that executes build123d or CadQuery Python scripts and produces STEP files, PNG renders, mesh exports, and geometric metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdilla1277](https://clawhub.ai/user/jdilla1277) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers, designers, and AI agents use agentcad to create, inspect, iterate on, and export 3D CAD models from build123d or CadQuery scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on local code execution through the agentcad CLI to generate and modify CAD models. <br>
Mitigation: Review generated CAD scripts before execution and keep backups of important Fusion or CAD documents before using the workflow. <br>
Risk: Installation or setup commands may run code from external package or repository sources. <br>
Mitigation: Install from trusted package sources and review installer commands before running them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jdilla1277/skills/agentcad) <br>
- [agentcad documentation](https://agentcad.dev) <br>
- [agentcad PyPI package](https://pypi.org/project/agentcad/) <br>
- [agentcad CLI source](https://github.com/jdilla1277/agentcad) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Files, Analysis, Configuration instructions] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; agentcad commands return JSON and produce CAD artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.10-3.12 and the agentcad CLI on PATH.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
