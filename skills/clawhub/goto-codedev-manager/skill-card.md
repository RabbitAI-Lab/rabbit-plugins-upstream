## Description: <br>
Coordinates multiple IDE and AI coding-agent tools to manage code development, Git Diff analysis, EF Core entity detection, migration generation, schema-contract handoff, tests, builds, and development reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[feixuelingcloud](https://clawhub.ai/user/feixuelingcloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate local coding agents and IDE CLIs, inspect project changes, identify .NET/EF Core database changes, generate migration handoff artifacts, and run development validation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can invoke local CLIs, edit workspaces, run build or test commands, and coordinate database-migration workflows. <br>
Mitigation: Install it only for trusted repositories and databases, review workspace and adapter configuration before use, and keep confirmation gates enabled for coding tasks, migrations, database updates, and commits. <br>
Risk: Configured build, test, adapter, or migration commands may execute arbitrary project code in the local environment. <br>
Mitigation: Avoid using the skill on untrusted repositories and inspect configured command paths, adapter arguments, and TEST_DB_CONNECTION values before running workflows. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill Definition](SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/feixuelingcloud/skills/goto-codedev-manager) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown, JSON files, shell command results, and structured development reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write schema-contract artifacts, migration files, reports, and workspace changes through configured local adapters after confirmation gates.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, pyproject.toml, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
