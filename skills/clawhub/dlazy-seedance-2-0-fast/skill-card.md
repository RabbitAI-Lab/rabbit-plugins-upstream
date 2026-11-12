## Description:

Fast version of ByteDance's Seedance 2.0. Generates videos faster with support for multi-modal references, first/last frame, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate Seedance 2.0 Fast videos from text prompts and optional image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial with medium confidence and noted a mismatch between the described video-generation purpose and observed CLI login and API credential examples.

Mitigation: Review the skill instructions and CLI setup details before installing, as the scan guidance recommends.

Risk: Prompts and local media supplied as references are sent to dLazy-hosted services for generation.

Mitigation: Avoid including confidential prompts or media unless they are approved for processing by the service.

## Reference(s):

- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video assets, JSON]

**Output Format:** [JSON result containing generated asset URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation accepts a prompt and optional media references; output may be returned asynchronously.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
