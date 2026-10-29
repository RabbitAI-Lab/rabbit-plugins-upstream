## Description:

Generates Seedance 2.5 videos from prompts, with image, video, and audio references or first and last frame controls, for clips up to 30 seconds and resolutions up to 4K.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate short videos from text prompts and optional reference media, or to control a clip with first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference media are sent to dLazy services, and local media may be uploaded for generation.

Mitigation: Only submit media and prompts you are authorized to share with the service.

Risk: Video generation consumes organization credits, and login stores an API key in the local CLI configuration.

Mitigation: Review costs before generation, protect the local configuration, and rotate or revoke the key when needed.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands]

**Output Format:** [Generated video asset with a JSON result containing output URLs; optionally saved as a local file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Clip duration up to 30 seconds; selectable resolution, aspect ratio, and audio generation.]

## Skill Version(s):

1.2.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
