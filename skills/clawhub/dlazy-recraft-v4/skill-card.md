## Description:

Generates 1MP raster images with Recraft V4 for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request raster image generation through the dLazy Recraft V4 CLI, including prompt-based generation, aspect-ratio selection, dry runs, and asynchronous task polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media file paths provided to the skill are sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive prompts or media unless that use is approved for dLazy's service.

Risk: Local media paths passed to image, video, or audio fields may cause files to be uploaded to dLazy media storage.

Mitigation: Review file paths before invocation and provide only files intended for cloud processing.

Risk: Login can store an organization-scoped API key in the local dLazy CLI configuration.

Mitigation: Use the pinned npx invocation when a global install is not desired, protect the local config, and rotate or revoke the key when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response containing generated image URLs or asynchronous task status, with shell commands and human-facing guidance for setup and errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are returned as hosted URLs; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
