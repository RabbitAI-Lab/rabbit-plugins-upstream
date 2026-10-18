## Description:

Converts PNG and JPG images to vector artwork through dLazy's hosted service and returns a result URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, developers, and other users can submit raster images for vectorization and receive a hosted result URL or save the resulting asset locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to dLazy's hosted service.

Mitigation: Upload only images you are authorized and comfortable sharing with dLazy.

Risk: The third-party CLI requires an API key and can save it locally.

Mitigation: Review the pinned CLI before installing; use an environment variable for the key if local persistence is undesirable.

Risk: The claimed SVG output conflicts with the PNG example in the documentation.

Mitigation: Check the returned file type before relying on vector output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Image URLs]

**Output Format:** [JSON result with a hosted asset URL; optionally a downloaded image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documentation describes SVG output, but its example returns PNG; verify the actual format.]

## Skill Version(s):

1.2.29 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
