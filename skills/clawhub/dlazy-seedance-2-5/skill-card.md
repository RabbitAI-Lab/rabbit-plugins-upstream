## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Seedance 2.5 video-generation service from an agent workflow, supplying prompts and optional image, video, audio, or frame references to produce generated media URLs or saved assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly selected media files are sent to dLazy's hosted service for generation.

Mitigation: Avoid submitting private or sensitive prompts and media unless the user accepts upload to the hosted service.

Risk: The dLazy API key may be stored in the user's local CLI configuration for future use.

Mitigation: Use per-invocation `DLAZY_API_KEY` where appropriate, keep local config access restricted to the current OS user, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Global CLI installation persists a third-party executable on the system.

Mitigation: Use `npx @dlazy/cli@1.2.3` for on-demand execution when a persistent global install is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results are returned by the dLazy CLI as JSON containing output URLs or asynchronous task status; the CLI can also save generated media to a local path.]

## Skill Version(s):

1.2.5 (source: server release metadata; skill frontmatter and CLI install metadata reference 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
