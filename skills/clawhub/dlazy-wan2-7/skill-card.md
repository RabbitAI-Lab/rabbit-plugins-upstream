## Description:

Tongyi Wanxiang 2.7 video generation through the dLazy CLI, supporting text-to-video, reference media inputs, and first/last-frame video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy hosted Tongyi Wanxiang 2.7 video-generation service from an agent workflow, including prompt-based generation and generation from reference images, videos, audio, or first/last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to the dLazy hosted service, and generated files are hosted by dLazy.

Mitigation: Use the skill only with content intended for cloud upload, and avoid passing sensitive local media unless upload is intended.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Use organization-scoped keys that can be rotated or revoked, and prefer per-invocation environment variables when persistent local storage is not desired.

Risk: A global CLI installation persists on the system.

Mitigation: Use the pinned `npx @dlazy/cli@1.2.3` option when a persistent global CLI is not desired.

Risk: Broad trigger phrasing and third-party service use may cause unintended invocation.

Mitigation: Review the requested generation action before execution and confirm that third-party service use is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [JSON responses with generated asset URLs, optional downloaded media files, and concise command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, local save paths, and API-key based authentication.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
