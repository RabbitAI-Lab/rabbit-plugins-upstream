## Description:

Generates fast lip-synced media from video and audio using the dLazy-hosted HeyGen Lipsync Speed model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to synchronize video lip movements with supplied audio when quick generation matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external CLI sends supplied media and parameters to dLazy's hosted service.

Mitigation: Confirm you trust the CLI and service before installation or uploading sensitive media.

Risk: Authentication may persist an API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials or npx to avoid a persistent global CLI installation.

Risk: The sample --prompt command conflicts with the listed video and audio flags.

Mitigation: Check the CLI help for the correct video and audio options before running a generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON CLI results and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include generated media URLs or an asynchronous generation ID; optional --save downloads the asset.]

## Skill Version(s):

1.3.26 (source: server-resolved ClawHub release; skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
