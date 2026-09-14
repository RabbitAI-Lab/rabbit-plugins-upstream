## Description:

A development-time skill that guides developers and agents through creating, debugging, packaging, and publishing DSH (DeepSeek Harness) / Cordis plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build or review DSH/Cordis plugins, choose the right plugin form, apply templates, verify version-sensitive API assumptions, troubleshoot loading and runtime issues, and package plugin bundles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts and templates can execute code or child processes during plugin development.

Mitigation: Review scripts and templates before use, prefer the Python probe, and avoid running the Bash probe with untrusted repository paths.

Risk: Sample MCP bundle patterns can expose forwarded environment credentials to downloaded child processes.

Mitigation: Pin exact package versions, forward only one least-privilege revocable credential, and separate download and review from execution.

Risk: Repository-derived findings from untrusted forks could persist misleading guidance outside the current project.

Mitigation: Keep findings scoped to the current project and do not write untrusted fork guidance into global agent memory.

## Reference(s):

- [Project homepage](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Cordis repository](https://github.com/cordiverse/cordis)
- [Version gate](references/00-version-gate.md)
- [Mental model](references/01-mental-model.md)
- [Templates](references/02-templates.md)
- [API cookbook](references/03-api-cookbook.md)
- [Pitfalls](references/05-pitfalls.md)
- [Workflow](references/06-workflow.md)
- [Conventions](references/07-conventions.md)
- [Cheatsheet](references/08-cheatsheet.md)
- [Community plugins](references/12-community-plugins.md)
- [Inbound HTTP and timers](references/14-inbound-http-and-timers.md)
- [Skill scope and maintenance](references/15-skill-scope-and-maintenance.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, configuration snippets, and generated plugin files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be checked against the current DSH source or probe results before relying on version-sensitive API details.]

## Skill Version(s):

1.0.9 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
