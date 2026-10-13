## Description:

Helps agents generate images from text prompts or reference images using Doubao Seedream 4.5 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image and image-to-image generation and retrieve the resulting image links or saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images may be sent to dLazy, and generated images are hosted on its file storage.

Mitigation: Only submit prompts and images you are comfortable sharing with the hosted service; review its terms before use.

Risk: Image-generation requests may consume paid credits.

Mitigation: Check the cost estimate with the CLI's dry-run option before submitting a request.

Risk: Login can save an API key locally, and global installation keeps the CLI on the system.

Mitigation: Use a per-invocation environment variable for the key and npx for on-demand execution if persistence is unwanted.

## Reference(s):

- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs or saved locally on request.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
