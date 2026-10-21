## Description:

Converts PNG and JPG images into color vector SVGs for scalable logos, icons, and flat illustrations, returning a result URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to convert raster logos, icons, and flat illustrations to scalable vector images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented SVG conversion does not match the PNG example response, and example commands conflict with the documented --image option.

Mitigation: Confirm that vectorize returns SVG before relying on it; use --image as documented and check the CLI help.

Risk: Selected local image files are uploaded to dLazy's hosted service.

Mitigation: Only supply images you are permitted to upload.

Risk: Authentication can leave an API key in local CLI configuration.

Mitigation: Protect the local configuration or provide DLAZY_API_KEY per invocation; rotate or revoke exposed keys.

Risk: A global CLI installation persists on the host.

Mitigation: Use the documented pinned npx invocation if a persistent global installation is unnecessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [CLI commands and JSON containing a hosted result URL; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documentation describes SVG output, but its example shows a PNG result; verify the actual output format before relying on vector data.]

## Skill Version(s):

1.2.31 (source: server-resolved release; artifact frontmatter lists 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
