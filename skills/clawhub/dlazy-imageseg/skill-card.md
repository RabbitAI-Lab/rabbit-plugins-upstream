## Description:

Image matting tool that separates foreground from background and returns a transparent-background image URL for product image processing, character cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production teams use this skill to run dLazy image segmentation from an agent, separating a foreground subject from its background and returning a transparent PNG URL or saved file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or local file paths passed to the CLI may be uploaded to dLazy hosted API and file storage.

Mitigation: Use only inputs approved for dLazy cloud processing and avoid passing sensitive images or paths unless the user accepts that handling.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer scoped keys, use DLAZY_API_KEY for one-off invocations when appropriate, and rotate or revoke keys from the dLazy dashboard if access changes.

Risk: The --save option writes generated assets to a local path.

Mitigation: Choose an explicit destination path and avoid overwriting important files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands; runtime output is JSON containing image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task metadata when --no-wait is used; --save writes the result asset to a selected local path.]

## Skill Version(s):

1.3.18 (source: release evidence; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
