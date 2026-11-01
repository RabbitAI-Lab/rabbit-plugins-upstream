## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K. Supports text-to-video, first/last frame transitions and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate short MiniMax Hailuo video clips from text prompts, first and last frames, or reference media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy hosted services, and local media may be uploaded for generation.

Mitigation: Submit only prompts and media you are comfortable sharing with dLazy.

Risk: The CLI saves an API key in the local user configuration, and video generation may consume account credits.

Mitigation: Protect access to the saved key, rotate or revoke it if exposed, and check credit costs before generating.

Risk: Resolution documentation is inconsistent, and this review does not verify the external CLI implementation.

Mitigation: Check the current CLI help and dLazy documentation before choosing generation settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)
- [GitHub CLI link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated video files, JSON task and result metadata]

**Output Format:** [Hosted media assets with JSON task or result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return asynchronously; results include hosted asset URLs.]

## Skill Version(s):

1.2.33 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
