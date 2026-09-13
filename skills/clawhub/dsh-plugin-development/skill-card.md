## Description:

Guides developers and AI agents through building, debugging, packaging, and publishing DSH (DeepSeek Harness) / Cordis plugins with templates, API checks, and troubleshooting references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, review, debug, package, and publish DSH / Cordis plugins. It is intended for development-time guidance rather than as a DSH runtime plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Copy-ready plugin templates may run unpinned external packages while forwarding API keys.

Mitigation: Review generated templates before use, pin external packages to exact reviewed versions, avoid floating npx or uvx package specs for credentialed processes, and use only low-quota, revocable keys needed for the integration.

Risk: DSH plugin APIs are pre-stable, so stale guidance can lead to broken plugin code.

Mitigation: Run the bundled version gate and probe scripts against the target DSH checkout before relying on API names, slots, services, or implementation-level details.

## Reference(s):

- [Server-resolved source repository](https://github.com/liupengyang-1008/dsh-plugin-development)
- [ClawHub skill page](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [DeepSeek Harness upstream](https://github.com/deepseek-ai/deepseek-harness)
- [Version gate](references/00-version-gate.md)
- [API claims register](references/api-claims.md)
- [Templates](references/02-templates.md)
- [Workflow](references/06-workflow.md)
- [Pitfalls](references/05-pitfalls.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces development guidance and proposed artifacts for DSH / Cordis plugins; generated code and commands should be reviewed before execution.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
