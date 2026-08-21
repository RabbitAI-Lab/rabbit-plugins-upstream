## Description:

Tongyi Wanxiang 2.7 video model for text-to-video, first/last-frame-to-video, and reference-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos with dLazy's Tongyi Wanxiang Wan 2.7 CLI from text prompts, reference media, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy endpoints for generation.

Mitigation: Confirm the user wants dLazy/Tongyi Wanxiang before use and avoid sending sensitive prompts or media unless appropriate for that service.

Risk: The dLazy CLI can save an API key under the user's local configuration directory.

Mitigation: Prefer a per-run DLAZY_API_KEY when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return hosted output URLs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
