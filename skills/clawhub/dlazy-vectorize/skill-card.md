## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to convert raster PNG/JPG inputs into scalable vector-style image assets through the dLazy CLI and hosted service. It is suited for logos, icons, and flat illustrations where a generated output URL or saved asset is useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the dLazy CLI package and hosted service.

Mitigation: Prefer the pinned npx @dlazy/cli@1.2.3 path or an isolated install, and review the package or repository before use.

Risk: Image inputs and parameters may be uploaded to dLazy API and media storage endpoints.

Mitigation: Upload only images that are acceptable to process with dLazy under the user's organization policy and service terms.

Risk: Authentication requires a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Use a revocable organization-scoped key, restrict local config access, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples that point to generated image URLs or saved assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers when invoked with no-wait behavior; generated assets are hosted by dLazy media storage unless saved locally.]

## Skill Version(s):

1.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
