## Description:

Generates PixVerse C1 videos from text prompts, images, reference images, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create short PixVerse C1 videos from prompts, reference media, or start and end frames, then retrieve a result URL or save the generated media locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services, and generation can use account credits.

Mitigation: Use only media you intend to upload and run --dry-run to review the payload and estimated cost before generation.

Risk: Logging in saves an API key in the local CLI configuration.

Mitigation: Protect access to the local account and device, and rotate or revoke the organization key if it may have been exposed.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)

## Skill Output:

**Output Type(s):** [Video files, JSON, Shell commands]

**Output Format:** [JSON result with generated media URLs, optionally saved as a local media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation settings include prompt, reference images or first and last frames, resolution, aspect ratio, duration, and optional audio.]

## Skill Version(s):

1.2.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
