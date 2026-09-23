## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run the dLazy vectorize CLI for converting raster image inputs into hosted vectorization outputs, with optional download of the returned asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a hosted dLazy service and may require storing or supplying a dLazy API key.

Mitigation: Install and use the skill only when the user accepts dLazy service use; prefer normal CLI authentication or per-invocation environment variables and rotate or revoke keys when needed.

Risk: Local image files passed to the CLI are uploaded to dLazy media storage for processing.

Mitigation: Avoid passing sensitive local media paths unless the user intends those files to be uploaded to the hosted service.

Risk: The evidence notes output and parameter inconsistencies that can affect workflows expecting SVG versus PNG results.

Mitigation: Verify the actual returned mime type and URL before building automated downstream workflows around the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and image input as a URL or local path; results may be returned asynchronously or saved to a local path.]

## Skill Version(s):

1.2.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
