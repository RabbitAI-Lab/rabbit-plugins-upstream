## Description:

ByteDance's latest video generation model. Supports multi-modal reference (images, video, audio) to generate videos, as well as first/last frame and text-to-video modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can generate short videos from text prompts, multimodal references, or first and last frame images through dLazy's Seedance 2.0 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy cloud services, generation may incur charges, and the locally stored organization API key is sensitive.

Mitigation: Submit only media you are authorized to share, review dLazy's privacy terms, use --dry-run to preview costs, and protect or revoke the API key as needed.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated media assets with JSON result metadata; asynchronous runs can return task status before results are available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports image, video, and audio references, first/last-frame inputs, and configurable resolution, aspect ratio, duration, and audio generation.]

## Skill Version(s):

1.3.31 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
