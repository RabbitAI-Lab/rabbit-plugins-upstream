## Description:

MiniMax Hailuo omni-modal video model with native stereo audio, producing 5-15 second clips at up to 2K, with text-to-video, first/last frame transitions, and multi-asset references for character and scene consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short MiniMax Hailuo videos from text prompts, first and last frames, or reference media through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had partial coverage, and its summary notes a mismatch between the stated 2K limit and CLI help that advertises 4K output.

Mitigation: Review the pinned CLI package and confirm supported resolutions before relying on a particular output size.

Risk: Prompts and supplied image, video, or audio files are sent to dLazy's hosted service for generation.

Mitigation: Avoid submitting sensitive prompts or media unless they are appropriate to share with the service.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video assets, JSON result data]

**Output Format:** [Generated video URLs or saved video files, with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [5-15 second clips; text, first/last-frame, or multi-asset reference modes; optional local save path.]

## Skill Version(s):

1.2.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
