## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's vectorization CLI/API for converting PNG or JPG raster images into scalable vector-style outputs and returned asset URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and sends selected inputs to dLazy-hosted services.

Mitigation: Review the third-party CLI before installation and submit only content appropriate for dLazy's hosted service.

Risk: An API key may be stored in the local CLI config when using interactive login or auth set.

Mitigation: Use DLAZY_API_KEY per invocation for ephemeral credentials when appropriate, and rotate or revoke organization keys from the dLazy dashboard when needed.

Risk: The documentation is inconsistent about whether the command takes --image or --prompt and whether the result is SVG or PNG.

Mitigation: Run dlazy vectorize -h and test with non-sensitive sample input before using the skill in production workflows.

## Reference(s):

- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a hosted asset URL or, with --save, a downloaded local file; async mode returns a task identifier for polling.]

## Skill Version(s):

1.2.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
