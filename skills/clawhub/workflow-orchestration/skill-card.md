## Description: <br>
A lightweight workflow orchestration engine for multi-phase task coordination with routing, phase execution, and exception handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terr123123](https://clawhub.ai/user/terr123123) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to route work into standard, lightweight, hotfix, or custom workflows, advance gated phases, preserve workflow state, and handle exceptions during multi-phase project coordination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved workflow instances can contain project context and artifacts, so loading untrusted state may expose or reintroduce sensitive or incorrect project data. <br>
Mitigation: Store workflow state only in approved locations, avoid placing secrets in context or artifacts, and load instance data only from trusted sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terr123123/skills/workflow-orchestration) <br>
- [API Reference](docs/api-reference.md) <br>
- [Usage Guide](docs/usage-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, and workflow configuration data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workflow names, phase results, exception outcomes, and JSON/YAML-serializable workflow state.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
