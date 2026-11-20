## Description:

Generate high-quality cinematic effects videos with Google Veo 3.1 for text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate cinematic videos from text prompts, reference images, or an existing video using Google Veo 3.1 through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security scan did not assess the pinned CLI package because its install reference could not be resolved.

Mitigation: Review the pinned @dlazy/cli package and its source before installing, as recommended by the scan guidance.

Risk: Prompts and supplied local media are sent to dLazy's hosted API and media storage.

Mitigation: Avoid submitting sensitive prompts or media unless sharing them with the service is appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [CLI repository link listed in the skill metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, Files, JSON, Shell commands]

**Output Format:** [Generated media URLs in a JSON response, with optional saved media files]

**Output Parameters:** [Prompt plus optional image or video inputs, generation mode, aspect ratio, resolution, and duration]

**Other Properties Related to Output:** [May return an asynchronous task ID; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
