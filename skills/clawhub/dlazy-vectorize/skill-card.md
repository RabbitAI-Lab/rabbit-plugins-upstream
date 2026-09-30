## Description:

Helps agents convert raster images into vector-style assets using dLazy's hosted service and return a result URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can ask an agent to process PNG or JPG images for logos, icons, and flat illustrations and obtain a hosted result URL or a downloaded asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local images and parameters are sent to dLazy's hosted service.

Mitigation: Confirm the exact file and obtain approval before uploading sensitive images.

Risk: Using the CLI requires a dLazy API key that may be stored locally.

Mitigation: Protect the key, avoid exposing it in shared output, and rotate it if compromised.

Risk: Documentation claims SVG output, but its example returns a PNG image.

Mitigation: Check the actual output MIME type and file format before relying on vector scaling.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI repository (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON result URLs]

**Output Format:** [Markdown guidance with shell commands and a hosted asset URL or JSON result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A downloaded asset is optional; verify the returned MIME type before treating it as SVG.]

## Skill Version(s):

1.2.22 (source: server-resolved ClawHub release; artifact frontmatter lists 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
