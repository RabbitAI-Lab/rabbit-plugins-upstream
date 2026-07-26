## Description: <br>
Audits skill libraries and active projects by profiling the project, scoring installed skills, checking capacity and liveness, comparing trends, supporting snapshot rollback, and producing CI-friendly reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gtbwpkwjnb-alt](https://clawhub.ai/user/gtbwpkwjnb-alt) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to audit installed skills or active project environments, identify stale or redundant capabilities, analyze capacity and liveness, and produce maintenance recommendations or CI gate output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill scans local projects and installed skills, reads profile, memory, and configuration files, and writes local audit data. <br>
Mitigation: Run it only in intended workspaces and review scan paths, data directories, and archive locations before use. <br>
Risk: Installer and maintenance workflows can make broad local changes. <br>
Mitigation: Review or clone installer scripts instead of using pipe-to-shell installation, and confirm exact paths, packages, repositories, and proposed actions before execution. <br>
Risk: Downstream Skills Manager actions could apply maintenance changes automatically. <br>
Mitigation: Require human confirmation for action lists and keep snapshot rollback enabled for editable skills. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gtbwpkwjnb-alt/skills/skills-audit) <br>
- [SKILL.md](SKILL.md) <br>
- [README.md](README.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>
- [Execution flow](references/execution-flow.md) <br>
- [Report template](references/report-template.md) <br>
- [CI output schema](references/ci-output-schema.md) <br>
- [Actions schema](references/actions-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown audit reports with optional JSON CI output and action recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local profile, cache, log, and snapshot files when used for skill maintenance.] <br>

## Skill Version(s): <br>
5.9.2 (source: frontmatter, changelog, VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
