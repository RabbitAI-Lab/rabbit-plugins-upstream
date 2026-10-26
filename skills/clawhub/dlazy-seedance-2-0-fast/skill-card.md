## Description:

Fast version of ByteDance's Seedance 2.0. Generates videos faster with support for multi-modal references, first/last frame, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to generate short videos from text prompts and optional image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy-hosted services for generation.

Mitigation: Only submit prompts and media you are comfortable uploading to dLazy.

Risk: Generation may incur charges, and the skill requires an organization API key.

Mitigation: Review the pinned CLI before installation, protect the saved API key, and use --dry-run to preview requests and estimated cost.

## Reference(s):

- [dLazy CLI package (metadata link)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON response containing generated video output URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video assets are hosted by dLazy and can be downloaded locally with --save.]

## Skill Version(s):

1.3.32 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
