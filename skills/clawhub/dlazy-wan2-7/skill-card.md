## Description:

Tongyi Wanxiang Wan 2.7 helps an agent generate video from text prompts, reference images or videos, audio, and first/last frame inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Wan 2.7 service for text-to-video, image/video-reference-to-video, first/last-frame video generation, and saving generated media outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media paths provided to the skill are sent to dLazy's hosted service for generation.

Mitigation: Only submit prompts and media that are acceptable to upload to dLazy, and review organization policy before using sensitive content.

Risk: Authentication stores a dLazy API key locally or uses the DLAZY_API_KEY environment variable.

Mitigation: Use the documented login or auth flow, protect local configuration files, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing a third-party npm CLI globally can introduce supply-chain and persistence risk.

Mitigation: Prefer the pinned npx command or a sandbox for per-use execution, and review the linked source/package before installation.

Risk: Generation calls may consume account credits.

Mitigation: Use dry-run or cost checks where appropriate and monitor available dLazy credits before large generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, saved media files, or asynchronous task identifiers.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter states 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
