## Description:

PixVerse C1 is a video-generation skill for action, VFX, and high-motion scenes, covering text-to-video, image-to-video, first/last-frame-to-video, and reference-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate PixVerse C1 videos through the dLazy CLI from prompts, reference images, or first and last frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party npm CLI and sends prompts and selected media files to dLazy cloud services.

Mitigation: Install only after reviewing the package or source, prefer the documented pinned npx path when avoiding a persistent global binary, and submit only media authorized for upload.

Risk: Authentication can store a dLazy API key in the local user configuration.

Mitigation: Use DLAZY_API_KEY per invocation when local key persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [npm package: @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [JSON responses from the dLazy CLI, with optional saved generated media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests can return a generateId and status for later polling; generated asset URLs are hosted by dLazy.]

## Skill Version(s):

1.2.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
