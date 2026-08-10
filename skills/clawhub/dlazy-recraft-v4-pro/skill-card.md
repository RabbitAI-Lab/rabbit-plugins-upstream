## Description:

Generates 4MP high-resolution raster images suitable for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's Recraft V4 Pro image-generation service from an agent workflow. It supports prompt-driven raster image generation with configurable aspect ratio and optional asynchronous task handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any files explicitly passed to the CLI are sent to dLazy cloud endpoints for processing.

Mitigation: Use the skill only with data approved for dLazy's hosted service and avoid passing sensitive local files unless that transfer is intended.

Risk: The dLazy API key may be persisted in a local CLI configuration file.

Mitigation: Treat the key as sensitive, prefer DLAZY_API_KEY for per-run use when persistence is not desired, and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image results are returned by the dLazy CLI as JSON containing hosted image URLs, or as an async task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release metadata; bundled frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
