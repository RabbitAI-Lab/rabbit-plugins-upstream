## Description:

DSH Plugin Development guides developers and agents through creating, debugging, packaging, and publishing DSH/Cordis plugins with templates, API guidance, version checks, and support scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, package, and publish DSH/Cordis plugins, including tools, slash commands, config schemas, services, UI slots, HTTP routes, timers, and plugin bundles. It is designed for development-time guidance rather than as a runtime DSH plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile-changing commands and plugin_manager actions can install, remove, update, or otherwise alter a DSH profile.

Mitigation: Review and approve those commands before execution, especially dsh plugin add, remove, update, and plugin_manager actions.

Risk: Network source synchronization can fetch newer DSH source material and change the evidence used for generated guidance.

Mitigation: Approve network sync only when verifying against a newer DSH version, and prefer local or pinned source evidence when available.

Risk: Generated plugin code or advice may become stale because DSH is pre-stable and changes on a short cadence.

Mitigation: Run the version gate and probe scripts before relying on volatile DSH APIs, and mark unverified APIs for developer confirmation.

## Reference(s):

- [Project homepage](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Version Gate and Anti-Staleness Workflow](references/00-version-gate.md)
- [DSH Plugin Mental Model](references/01-mental-model.md)
- [Template Library](references/02-templates.md)
- [API Cookbook](references/03-api-cookbook.md)
- [UI and Slots](references/04-ui-and-slots.md)
- [Workflow, Packaging, and Debugging](references/06-workflow.md)
- [Pitfalls and Error Lookup](references/05-pitfalls.md)
- [API Claims Register](references/api-claims.md)
- [Skill Scope and Maintenance](references/15-skill-scope-and-maintenance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, configuration snippets, and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DSH plugin skeletons, Cordis patch configuration, validation commands, and debugging checklists.]

## Skill Version(s):

1.3.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
