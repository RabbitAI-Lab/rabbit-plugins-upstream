## Description:

Guides developers through building, testing, packaging, and publishing DSH/Cordis plugins, with templates, API references, and an upstream-version check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liupengyang-1008](https://clawhub.ai/user/liupengyang-1008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to create and troubleshoot DSH/Cordis plugins, including tools, commands, services, UI extensions, and plugin bundles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Helper scripts may access the network or fetch changing upstream content.

Mitigation: Review scripts, particularly dsh-sync.sh, before running them and verify the target upstream version.

Risk: Generated bundles may invoke npx or pass API keys to child processes.

Mitigation: Review generated bundles, pin package versions, and use limited, revocable credentials.

## Reference(s):

- [Declared project homepage (ClawHub metadata)](https://github.com/liupengyang-1008/dsh-plugin-development)
- [Version gate](artifact/references/00-version-gate.md)
- [Plugin workflow](artifact/references/06-workflow.md)
- [API cookbook](artifact/references/03-api-cookbook.md)
- [Plugin templates](artifact/references/02-templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated plugins and commands require local validation against the target DSH version.]

## Skill Version(s):

1.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
