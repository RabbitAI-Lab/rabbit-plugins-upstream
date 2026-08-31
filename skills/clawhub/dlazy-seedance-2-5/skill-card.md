## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative, multi-modal references, and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy Seedance 2.5 video-generation CLI, configure authentication, submit prompts and optional media references, and retrieve generated video assets or task status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced image, video, or audio files are sent to dLazy's hosted service for generation.

Mitigation: Use approved inputs only, avoid sensitive media unless authorized, and review dLazy service terms before production use.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied through DLAZY_API_KEY.

Mitigation: Store keys only on trusted systems, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: A global npm installation persists the third-party dLazy CLI on the host.

Mitigation: Prefer the pinned npx invocation for temporary use, or review the CLI source before installing it globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [npm package @dlazy/cli](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return generated asset URLs, asynchronous task identifiers, or downloaded files when invoked with --save.]

## Skill Version(s):

1.2.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
