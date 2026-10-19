## Description:

Generates music with or without vocals from prompts, using automatic lyrics or user-provided lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate vocal or instrumental music from a prompt, with optional custom lyrics and style controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill depends on an external npm CLI.

Mitigation: Review the dLazy CLI package before installing; use the pinned on-demand npx command if a global install is unwanted.

Risk: Prompts and any supplied local media files are sent to dLazy services.

Mitigation: Avoid supplying sensitive prompts or private files unless you intend to share them with dLazy.

Risk: Generation requires an API key and may consume paid service credits.

Mitigation: Manage and rotate the API key through the dLazy dashboard, and check the cost estimate before generation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and links to generated music]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return hosted result URLs or an asynchronous task ID; saving a result locally is optional.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
