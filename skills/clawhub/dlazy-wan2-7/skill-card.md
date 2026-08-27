## Description:

Tongyi Wanxiang 2.7 video model for text-to-video, first/last-frame-to-video, and reference-based video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Wan 2.7 video generation workflow from an agent, using prompts and optional image, video, or audio inputs to produce generated media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media files are sent to dLazy's hosted service for generation.

Mitigation: Do not submit confidential prompts or media unless the intended dLazy account, organization, and service terms are acceptable for that data.

Risk: The login flow can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local key storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on npm or npx to run the pinned dLazy CLI.

Mitigation: Review the pinned CLI package and install source before use, and keep execution within environments approved for third-party CLI tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media assets are returned as hosted URLs, or as asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
