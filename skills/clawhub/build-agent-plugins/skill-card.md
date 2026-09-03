## Description:

Create or standardize portable Agent Plugins, MCP servers, and skill bundles with bounded effects, tests, and activation proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noelillinger](https://clawhub.ai/user/noelillinger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose the smallest portable capability package, author Agent Plugins or related skills and MCP servers, and preserve validation evidence for compatibility and security review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or standardized plugins may later include MCP tools, external writes, or provider integrations that require separate review.

Mitigation: Review generated plugins separately before installing them or connecting credentials, and keep tool effects explicit and reviewable.

Risk: Plugin artifacts can accidentally include secrets, personal paths, generated clutter, duplicate policy owners, or undeclared effects.

Mitigation: Inspect the final diff and validation evidence before activation, and keep secrets out of manifests, source, logs, chat, fixtures, and generated artifacts.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/noelillinger/build-agent-plugins)
- [Agent Plugins documentation](https://agent-plugins.org)
- [ClawHub skill page](https://clawhub.ai/noelillinger/skills/build-agent-plugins)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with checklists, file layouts, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
