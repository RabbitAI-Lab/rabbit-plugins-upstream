## Description: <br>
Navigate and understand codebases using agentlens hierarchical documentation. Use when exploring new projects, finding modules, locating symbols in large files, finding TODOs/warnings, or understanding code structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nguyenphutrong](https://clawhub.ai/user/nguyenphutrong) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and coding agents use this skill to navigate projects that include AgentLens documentation, locate modules and symbols, inspect TODOs and warnings, and understand code structure before making changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to use project-local .agentlens documentation, which may be incomplete, stale, or untrusted. <br>
Mitigation: Review the .agentlens documentation in repositories from untrusted sources and confirm important findings against source code before making changes. <br>


## Reference(s): <br>
- [Agentlens ClawHub Page](https://clawhub.ai/nguyenphutrong/skills/agentlens) <br>
- [AgentLens Output Structure](references/structure.md) <br>
- [Navigation Patterns](references/navigation.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown guidance with file paths and navigation patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs the agent to consult project-local .agentlens documentation before reading source files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
