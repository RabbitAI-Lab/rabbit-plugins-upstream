## Description:

Generates PixVerse C1 videos from text prompts, reference images, or first and last frames through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request PixVerse C1 video generation from text prompts, reference images, or a first and last frame pair, then retrieve generated media through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment notes a mismatch between the video-generation purpose and the reported `dlazy login` behavior.

Mitigation: Review the CLI login behavior and the pinned package before installing or authenticating.

Risk: Prompts and supplied local media are sent to dLazy's hosted API and media storage.

Mitigation: Only submit content approved for that service, especially when prompts or media may be sensitive.

Risk: The release security assessment has medium confidence and partial coverage.

Mitigation: Review the pinned CLI dependency and any unresolved references before providing API credentials.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated video/media, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON result envelope with generated media URLs, plus command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text, image/reference-image, and first/last-frame inputs; generation settings include resolution, aspect ratio, duration, and optional audio.]

## Skill Version(s):

1.2.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
