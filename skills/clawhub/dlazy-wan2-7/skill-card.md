## Description:

Tongyi Wanxiang 2.7 video model covers text-to-video, first/last-frame-to-video, and reference-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Wan 2.7 videos through the dLazy CLI from prompts, reference media, first/last frames, and optional audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI stores an API key for authenticated requests.

Mitigation: Use OS-user-restricted configuration, rotate or revoke the key from the dLazy dashboard when needed, or pass DLAZY_API_KEY per invocation.

Risk: Local image, video, or audio paths passed to the CLI may be uploaded to dLazy-hosted media storage for generation.

Mitigation: Only provide media files intended for cloud processing and avoid sensitive local assets.

Risk: Generation may consume account credits.

Mitigation: Use --dry-run when unsure to validate inputs and estimate cost before making an API call.

Risk: A global npm install persists a third-party CLI on the local system.

Mitigation: Prefer the pinned npx invocation when a non-persistent install is desired, and review the CLI package/source before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task IDs; the --save option can download generated assets locally.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
