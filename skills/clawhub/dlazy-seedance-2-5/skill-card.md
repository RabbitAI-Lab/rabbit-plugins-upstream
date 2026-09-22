## Description:

视频生成 Seedance 2.5 helps agents invoke dLazy's Seedance 2.5 video-generation CLI to create clips up to 30 seconds with 4K, multimodal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate Seedance 2.5 videos through the dLazy CLI, including prompt-only, multimodal reference, and first/last-frame workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs a third-party npm CLI.

Mitigation: Review the dLazy CLI package before use and prefer `npx @dlazy/cli@1.2.3` when you do not want a persistent global install.

Risk: Authentication may store a dLazy API key in local CLI configuration.

Mitigation: Use `DLAZY_API_KEY` for per-invocation credentials or rotate and revoke organization API keys from the dLazy dashboard when needed.

Risk: Prompts and selected image, video, or audio files are sent to dLazy endpoints for generation.

Mitigation: Submit only content appropriate for dLazy's hosted service and review user-provided media before passing local file paths to the CLI.

Risk: Generated result URLs may be hosted by dLazy media storage.

Mitigation: Handle returned URLs according to the user's sharing and retention requirements, or use the CLI save option when a local copy is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI may return hosted media URLs, asynchronous task identifiers, or save generated assets to a local path.]

## Skill Version(s):

1.2.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
