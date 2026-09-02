## Description:

Image replicate tool: analyzes the visuals, composition, colors, lighting, and style of the source image, builds a replicate prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate a new image in the style of one or more reference images through the dLazy hosted image-replication service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images or other local media paths supplied to the CLI are uploaded to dLazy's hosted service.

Mitigation: Review media for sensitive content before use, prefer non-sensitive inputs, and use --dry-run when checking payloads and costs.

Risk: Authentication stores a dLazy organization API key locally when using dlazy login or dlazy auth set.

Mitigation: Use per-invocation DLAZY_API_KEY where appropriate, protect the local config file, and rotate or revoke keys from dLazy when access changes.

Risk: A global npm install persists the dLazy CLI binary on the system.

Mitigation: Use the pinned npx invocation when a temporary execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted image URLs, saved image files when --save is used, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
