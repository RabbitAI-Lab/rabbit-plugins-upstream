## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to convert raster images such as logos, icons, and flat illustrations into vector-style assets through the dLazy hosted vectorization service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local image files are uploaded to dLazy-hosted storage for processing.

Mitigation: Review dLazy service terms and avoid sending sensitive or restricted images unless that use is approved.

Risk: The dLazy API key can be saved in local CLI configuration.

Mitigation: Use normal credential handling, rotate or revoke keys when no longer needed, and remove local credentials from shared environments.

Risk: The artifact has documentation inconsistencies around --image versus --prompt usage and SVG versus PNG output examples.

Mitigation: Confirm actual CLI behavior with dlazy vectorize -h before relying on command examples or output type claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted image output URLs and can optionally save generated assets locally.]

## Skill Version(s):

1.2.12 (source: server release evidence; artifact frontmatter reports 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
