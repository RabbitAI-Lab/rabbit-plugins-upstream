## Description:

DSH Plugin Development guides developers through building, debugging, packaging, and publishing DSH (DeepSeek Harness) / Cordis plugins, including plugin forms, templates, API guidance, pitfalls, and a required version gate for the pre-stable upstream.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-assisted engineering teams use this skill to create, modify, troubleshoot, package, and publish DSH or Cordis plugins. It helps route plugin requests to appropriate forms, templates, validation steps, and version checks before implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide agents to preserve long-lived source-derived conclusions in global memory.

Mitigation: Approve and scope any memory updates explicitly, and avoid storing DSH source-derived claims globally unless they have been reviewed.

Risk: Copyable bundle templates may run registry code or MCP servers while API keys are available.

Mitigation: Review copied bundle templates and commands before enabling npx-run MCP servers or passing API keys.

Risk: DSH is described as pre-stable, so API and plugin guidance can become stale.

Mitigation: Run the skill's version gate and probe against the current DSH source before relying on API names, plugin contracts, or breaking-change claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [Publisher Profile](https://clawhub.ai/user/liupengyang-1008)
- [Project Homepage](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Cordis Project](https://github.com/cordiverse/cordis)
- [Version Gate](references/00-version-gate.md)
- [Mental Model](references/01-mental-model.md)
- [Templates](references/02-templates.md)
- [API Cookbook](references/03-api-cookbook.md)
- [Pitfalls](references/05-pitfalls.md)
- [Workflow](references/06-workflow.md)
- [Conventions](references/07-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include version-gated recommendations, template files, validation steps, and review notes for DSH plugin work.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
