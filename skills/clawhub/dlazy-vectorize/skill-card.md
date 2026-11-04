## Description:

Converts raster images such as PNG and JPG into color vector SVG and returns a URL for scalable logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers use the skill to turn raster logos, icons, and flat illustrations into scalable vector artwork through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images supplied from local paths are uploaded to dLazy's hosted media service.

Mitigation: Only submit images you are comfortable sharing with the service; avoid sensitive or confidential images.

Risk: The CLI uses a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: Use of the hosted conversion service may incur charges.

Mitigation: Review the service's costs before running a conversion.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON result containing a generated image URL; the asset can optionally be saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the generated asset URL; asynchronous mode may return a task identifier before completion.]

## Skill Version(s):

1.2.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
