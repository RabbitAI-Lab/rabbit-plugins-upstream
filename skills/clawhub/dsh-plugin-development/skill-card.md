## Description:

Guides developers through building, debugging, packaging, and publishing DSH (DeepSeek Harness) and Cordis plugins with templates, API references, and version checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose a DSH plugin form, implement tools, commands, services, UI slots, or routes, and validate and package plugins against the target DSH version. The skill is development guidance, not an installable DSH plugin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to write derived API findings to persistent global memory without clear user control.

Mitigation: Remove or override that instruction; keep API verification notes in the current project or final report instead.

Risk: Optional source-sync steps can fetch DSH source from a configurable repository or mirror.

Mitigation: Get developer approval before fetching source and review repository, mirror, and confirmation-bypass options before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liupengyang-1008/skills/dsh-plugin-development)
- [Publisher-listed project homepage](https://github.com/liupengyang-1008/dsh-plugin-development)
- [DSH version gate](artifact/references/00-version-gate.md)
- [Plugin templates](artifact/references/02-templates.md)
- [API cookbook](artifact/references/03-api-cookbook.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include plugin templates and local verification steps.]

## Skill Version(s):

1.5.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
