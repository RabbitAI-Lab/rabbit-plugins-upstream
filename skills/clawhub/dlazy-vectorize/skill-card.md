## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to convert PNG or JPG assets into color vector outputs through the dLazy CLI and hosted API. It is suited for logos, icons, and flat illustrations that need scalable vector-style results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image files supplied for conversion may be uploaded to dLazy's hosted service.

Mitigation: Use the skill only with files approved for upload to dLazy and avoid submitting sensitive or restricted images unless the service is approved for that data.

Risk: The dLazy CLI may save an API key in local configuration.

Mitigation: Prefer per-invocation credentials or an isolated environment when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing a global CLI adds a persistent executable to the user's system.

Mitigation: Use the pinned npx invocation or install in an isolated environment if a persistent global binary is not appropriate.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, downloaded files when --save is used, or asynchronous task identifiers when --no-wait is used.]

## Skill Version(s):

1.2.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
