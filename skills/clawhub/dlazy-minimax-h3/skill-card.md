## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K. Supports text-to-video, first/last frame transitions and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts, frame pairs, or reference images, videos, and audio, then retrieve the generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy for generation, which uses service credits.

Mitigation: Share only assets intended for cloud processing and check credit costs before generating.

Risk: The external CLI implementation was not verified, and advertised resolution support is inconsistent.

Mitigation: Review the CLI before installation and confirm available resolutions with current service documentation.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-minimax-h3)

## Skill Output:

**Output Type(s):** [Files, API Calls]

**Output Format:** [Generated video media, returned with JSON result metadata and hosted asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-based or reference-guided generation; duration, aspect ratio, and resolution options are documented.]

## Skill Version(s):

1.2.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
