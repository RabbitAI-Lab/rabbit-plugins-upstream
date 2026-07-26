## Description: <br>
Creates automation command skills, or slash commands, for Claude Code projects that automate multi-step workflows with safety gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design command-style agent skills for repeatable workflows such as deploys, releases, migrations, commits, and cross-repo operations. It helps structure command frontmatter, phases, approval gates, error handling, and audit checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated commands may deploy, commit, delete, modify another repository, or call external APIs if used without review. <br>
Mitigation: Review every generated command before use, keep disable-model-invocation enabled for side-effecting commands, restrict allowed tools where practical, and require explicit approval before irreversible actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/command-skill-creator) <br>
- [Project Homepage](https://github.com/tenequm/skills/tree/main/skills/command-skill-creator) <br>
- [Command Skill Design Patterns](references/design-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown skill files with YAML frontmatter, phased instructions, command snippets, and audit notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces user-facing command skill guidance that should be reviewed before running side-effecting workflows.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
