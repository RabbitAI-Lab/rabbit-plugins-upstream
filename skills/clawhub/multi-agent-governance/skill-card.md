## Description: <br>
A comprehensive governance system for managing agent roles, responsibilities, handoff policies, and conflict resolution in multi-agent environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terr123123](https://clawhub.ai/user/terr123123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to define multi-agent roles, validate handoffs, resolve agent conflicts, and save reusable governance rules for collaborative agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and write user-selected YAML or JSON governance configuration files. <br>
Mitigation: Review configuration paths before loading or saving, and only use files and directories intended for governance state. <br>
Risk: Custom validation rules or role configurations can affect handoff, action validation, and conflict-resolution outcomes. <br>
Mitigation: Review custom rules and role definitions before using them in production multi-agent workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/terr123123/skills/multi-agent-governance) <br>
- [Usage Guide](docs/usage-guide.md) <br>
- [API Reference](docs/api-reference.md) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Configuration, Guidance] <br>
**Output Format:** [Python API results, JSON or YAML configuration files, governance reports, and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include validation results, handoff decisions, conflict resolutions, and saved governance configuration files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
