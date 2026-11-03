## Description:

Generates fast Seedance 2.0 videos from text prompts and multimodal references, including images, video, audio, and first or last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short Seedance 2.0 Fast videos from text prompts and optional image, video, audio, or first and last frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted service, and uploaded media may contain sensitive information.

Mitigation: Use only prompts and media you are comfortable sharing with dLazy, and review the service terms before generation.

Risk: The external CLI package and its claimed credential protections are unverified, and generation uses account credits.

Mitigation: Prefer the device login flow over sharing an API key in chat, understand the credit charges, and rotate or revoke a key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [CLI project homepage listed in release metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video media, JSON]

**Output Format:** [Generated video asset URLs or saved video files, with JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video results can be downloaded to a local path with the --save option.]

## Skill Version(s):

1.3.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
