## Description:

Video generation skill that automatically selects a suitable dLazy CLI model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate or edit videos from prompts and reference media, including image-to-video, first/last-frame, digital-human, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image, video, or audio inputs are sent to dLazy hosted services; the scan notes that image and audio workflows extend beyond the stated video purpose.

Mitigation: Review the documented workflows and service terms, and submit only prompts and media you are authorized to process there.

Risk: Some references were unresolved, so the benign, medium-confidence security scan is incomplete.

Mitigation: Review unresolved references and current service behavior before installation or use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI source (declared skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Image files, Audio files, JSON results, Shell commands]

**Output Format:** [Generated media files and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and local image, video, or audio inputs may be sent to dLazy hosted services for processing.]

## Skill Version(s):

1.4.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
