## Description:

Guides developers and agents through creating, debugging, packaging, and publishing DSH / Cordis plugins with templates, API references, pitfalls, and version checks for a pre-stable upstream.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, package, and publish DSH / Cordis plugins. It helps route requests to the right plugin form, verify DSH API assumptions, and produce plugin code, bundle configuration, commands, and validation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Bash helper can execute unintended local code from a crafted repository path.

Mitigation: Prefer the Python probe and avoid the Bash probe until its path handling is fixed; run helpers only against trusted local paths.

Risk: Sample MCP bundle patterns can pass API keys to downloaded third-party packages.

Mitigation: Verify the package, publisher, registry, and artifact before reuse, and use dedicated low-scope revocable API keys that forward only the credential the integration needs.

Risk: DSH is pre-stable, so stale API claims can cause generated plugin code or configuration to fail.

Mitigation: Run the version gate and probe against the target DSH source before relying on mutable API names, events, services, or loader behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [Project homepage](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Version gate](references/00-version-gate.md)
- [Mental model](references/01-mental-model.md)
- [Templates](references/02-templates.md)
- [API cookbook](references/03-api-cookbook.md)
- [Pitfalls](references/05-pitfalls.md)
- [Workflow](references/06-workflow.md)
- [Conventions](references/07-conventions.md)
- [Cheatsheet](references/08-cheatsheet.md)
- [API claims](references/api-claims.md)
- [Skill scope and maintenance](references/15-skill-scope-and-maintenance.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline code blocks and file-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated plugin files, Cordis patch configuration, validation commands, and version-gate notes.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
