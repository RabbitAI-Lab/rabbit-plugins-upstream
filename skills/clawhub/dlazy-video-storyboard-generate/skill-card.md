## Description:

Builds a storyboard-based video generation pipeline for a canvas by deriving media dimensions, shared audio and image inputs, and per-storyboard audio-clone and video nodes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative workflow builders use this skill to convert storyboard context into a canvas-ready video generation pipeline with audio, image, and video elements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can send prompts and selected media to dLazy cloud services.

Mitigation: Use only media intended for upload, avoid sensitive inputs, and keep agent filesystem access limited to the assets needed for generation.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Prefer short-lived or environment-provided credentials when possible, keep config file permissions restricted, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Global installation runs a third-party npm CLI on the local machine.

Mitigation: Prefer pinned one-off npx use or an isolated environment, and review the @dlazy/cli package and version before installation.

Risk: The artifact includes broader terminal image-generation instructions alongside the storyboard canvas workflow.

Mitigation: Review the requested action before allowing terminal commands and avoid granting broad filesystem access beyond intended media files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON pipeline snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The storyboard pipeline is represented as JSON-like canvas node definitions that reference audio, image, video, prompt, aspect ratio, and resolution inputs.]

## Skill Version(s):

1.2.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
