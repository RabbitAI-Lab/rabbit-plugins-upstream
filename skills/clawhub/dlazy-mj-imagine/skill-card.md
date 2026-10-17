## Description:

Generates stylized images from prompts with selectable aspect ratio, bot type, and grid or U1–U4 output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request artistic, strongly stylized images from prompts and choose aspect ratio, bot type, and output position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly provided to the skill are sent to dLazy-hosted services.

Mitigation: Review prompts and selected files for sensitive information before submitting them.

Risk: Saved login can persist a dLazy API key on the local device.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials if local persistence is unwanted.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON response with image URLs or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports grid or U1–U4 selection and optional local image download.]

## Skill Version(s):

1.3.29 (source: ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
