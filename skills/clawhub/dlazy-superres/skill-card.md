## Description:

Guides image upscaling through dLazy's super-resolution CLI and returns a link to the enhanced image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to enhance low-resolution images and obtain a link to the upscaled result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images supplied through the CLI may be uploaded to dLazy-hosted services.

Mitigation: Confirm you trust the dLazy service before submitting sensitive images.

Risk: The CLI may save an API key locally, and a global installation persists on the system.

Mitigation: Use the pinned on-demand npx invocation if preferred; rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-superres)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service can return an enhanced-image URL or an asynchronous task ID.]

## Skill Version(s):

1.3.31 (source: ClawHub release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
