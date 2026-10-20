## Description:

Generates images from text prompts and edits or combines images using reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or edit and combine images using up to five reference inputs via dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files supplied to the CLI may be uploaded to dLazy's hosted service.

Mitigation: Use only inputs approved for external processing and review dLazy's service terms before use.

Risk: Logging in stores an API key locally.

Mitigation: Use DLAZY_API_KEY for per-run authentication when appropriate; revoke or rotate stored keys through the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI source (tooling reference)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results include hosted image URLs; optional saving downloads the image locally, and asynchronous calls return a task ID.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
