## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos faster with support for multi-modal references, first/last frame generation, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to invoke dLazy's hosted Seedance 2.0 Fast video generation service from an agent workflow using text prompts, reference media, or first/last frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and user-provided media paths are sent to dLazy's hosted API and media storage.

Mitigation: Only submit data approved for external cloud processing, and review dLazy's service terms before using sensitive prompts or media.

Risk: Authentication can save a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated output URLs are hosted on files.dlazy.com.

Mitigation: Treat generated media links as externally hosted outputs and verify sharing or retention expectations before distributing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON responses containing generated media URLs or async task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.6 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
