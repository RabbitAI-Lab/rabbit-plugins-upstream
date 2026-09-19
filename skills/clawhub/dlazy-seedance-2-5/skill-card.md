## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through the dLazy Seedance 2.5 CLI, including prompts with image, video, audio, or first/last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files are sent to the dLazy hosted service for generation.

Mitigation: Avoid submitting sensitive media or confidential prompts unless the dLazy service terms and data handling meet the user's requirements.

Risk: The CLI may store a dLazy API key in the local user configuration.

Mitigation: Use per-invocation environment variables or rotate and revoke keys from the dLazy dashboard when access should change.

Risk: A persistent global npm install adds a local CLI dependency.

Mitigation: Use the pinned npx invocation when a temporary install is preferred, and review the referenced @dlazy/cli package before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses and optional downloaded media files from CLI execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when invoked with --no-wait; generated media URLs are hosted by files.dlazy.com.]

## Skill Version(s):

1.2.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
