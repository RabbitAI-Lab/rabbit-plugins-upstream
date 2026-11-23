## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative. Supports multi-modal references (image + video + audio) and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request Seedance 2.5 video generation from text prompts, optionally guided by image, video, audio, or first and last frame references. They can choose clip duration, resolution, aspect ratio, and audio generation, then receive hosted media URLs or save the generated asset locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports partial coverage and could not resolve the CLI package and service endpoints; it also notes an unexplained login operation whose downstream behavior the available scan evidence does not establish.

Mitigation: Review the external CLI package and assess its login behavior before installing or running it.

Risk: Prompts and supplied local image, video, or audio files are sent to dLazy services, and local media may be uploaded for generation.

Mitigation: Avoid submitting sensitive or unauthorized material, and review the service terms before sending inputs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [JSON response containing generated media URLs; optionally saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated clips can be 4–30 seconds; generated media is hosted by dLazy and can optionally be saved locally.]

## Skill Version(s):

1.2.39 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
