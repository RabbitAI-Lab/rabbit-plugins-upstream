## Description:

视频生成 Seedance 2.0 helps agents generate videos with ByteDance Seedance 2.0 from text prompts, reference images, video, audio, or first and last frames through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to generate short videos from prompts and multimodal references using dLazy's hosted Seedance 2.0 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy's hosted service for generation.

Mitigation: Only submit media and prompt content appropriate for that external service and avoid sensitive local files unless approved.

Risk: The dLazy API key can be saved in local CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a pinned third-party npm CLI package.

Mitigation: Review the pinned @dlazy/cli package before installation when npm package provenance matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI homepage metadata link](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are hosted by dLazy; async mode may return a generateId for polling.]

## Skill Version(s):

1.3.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
