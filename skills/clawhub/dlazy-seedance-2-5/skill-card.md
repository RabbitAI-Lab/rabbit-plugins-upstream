## Description:

视频生成 Seedance 2.5 helps agents call dLazy's Seedance 2.5 video-generation CLI to create up to 30-second clips with native 4K support, multimodal references, and first/last-frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to generate video clips through the dLazy hosted Seedance 2.5 API from prompts and optional image, video, audio, or frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to the dLazy API and media storage.

Mitigation: Submit only prompts and media intended for upload to dLazy.

Risk: Generated outputs are hosted by dLazy.

Mitigation: Treat returned media URLs according to the user's sharing and retention requirements.

Risk: Authentication may store a dLazy API key in the local CLI config.

Mitigation: Use per-invocation credentials when appropriate and rotate or revoke the dLazy API key when access is no longer needed.

Risk: A global npm install persists a third-party CLI binary on the system.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 command when a non-persistent CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON with generated media URLs and optional saved media file path]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generateId for later polling instead of completed outputs.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
