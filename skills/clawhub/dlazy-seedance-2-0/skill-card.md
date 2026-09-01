## Description:

Seedance 2.0 is a ByteDance video generation model exposed through dLazy that supports multimodal image, video, and audio references, first/last-frame generation, and text-to-video modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to ask an agent to generate videos with dLazy's Seedance 2.0 CLI from prompts and optional image, video, audio, or frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image, video, or audio paths can be uploaded to dLazy's hosted service.

Mitigation: Use the skill only when that data-sharing posture is acceptable, and avoid sending sensitive media or prompts unless approved for dLazy processing.

Risk: Authentication may save a dLazy API key in local CLI configuration.

Mitigation: Use OS user file permissions, prefer per-invocation DLAZY_API_KEY when appropriate, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The skill depends on a pinned third-party npm CLI package for execution.

Mitigation: Review the pinned npm package or source before installation, and use npx if a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands and JSON result objects.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return hosted media URLs or an async generateId; the CLI can optionally save generated assets to a local path.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
