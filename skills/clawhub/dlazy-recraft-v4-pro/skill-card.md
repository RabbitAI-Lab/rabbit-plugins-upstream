## Description:

Generates 4MP high-resolution raster images suitable for print-ready assets and large-format use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request Recraft V4 Pro image generation through the dLazy CLI, returning hosted image results or saving generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly referenced local files may be sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or local files unless the user accepts dLazy processing and hosting.

Risk: The dLazy CLI may store an API key in the local user configuration file.

Mitigation: Use per-invocation credentials when persistence is not desired, protect the local config file, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated results are hosted by dLazy and returned as remote URLs.

Mitigation: Do not generate or upload confidential assets unless remote hosting is acceptable; save outputs locally when a local artifact is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON, image URLs]

**Output Format:** [Markdown guidance with bash examples and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image assets are returned as dLazy-hosted URLs and can be saved locally with --save.]

## Skill Version(s):

1.3.10 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
