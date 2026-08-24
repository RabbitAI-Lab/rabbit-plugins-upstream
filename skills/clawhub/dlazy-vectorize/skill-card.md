## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to submit raster images to dLazy's hosted vectorization service and retrieve a scalable vector-style result URL or saved output file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and request parameters are sent to dLazy's hosted service.

Mitigation: Use only images and parameters appropriate for external processing, and avoid passing sensitive or unrelated local paths.

Risk: The dLazy API key is stored locally or supplied through the environment.

Mitigation: Keep the CLI config restricted to the OS user, prefer the pinned npx form when avoiding a global install, and rotate or revoke keys that are no longer needed.

Risk: Returned files or URLs may not match the expected vector output before downstream use.

Mitigation: Verify the returned file type before relying on it as SVG or using it in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns hosted output URLs from files.dlazy.com; the --save option can download the generated asset locally.]

## Skill Version(s):

1.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
