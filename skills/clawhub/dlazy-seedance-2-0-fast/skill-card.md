## Description:

Fast version of ByteDance's Seedance 2.0 for generating videos from text prompts, multimodal references, and first or last frame inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to invoke the dLazy CLI for Seedance 2.0 Fast video generation with prompts, reference media, frame controls, resolution, aspect ratio, duration, and audio options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the dLazy CLI and npm package to call a hosted video-generation service.

Mitigation: Install only if the publisher and package source are trusted, and prefer on-demand or sandboxed use when evaluating the skill.

Risk: Prompts and selected local media files are sent to dLazy service endpoints for generation.

Mitigation: Pass only media and prompt content intended for upload to dLazy.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Use normal local credential protections and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous generation identifiers, or locally saved generated assets when a save path is provided.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
