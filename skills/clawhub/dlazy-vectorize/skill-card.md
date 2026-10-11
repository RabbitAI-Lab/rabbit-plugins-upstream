## Description:

Converts PNG or JPG images into vector artwork through dLazy's hosted service and returns a result URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to vectorize logos, icons, and flat illustrations from raster images using the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images and prompts sent to dLazy's hosted service may contain sensitive information.

Mitigation: Only submit images and prompts approved for upload to the service.

Risk: Logging in can save an API key to local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: The documented --image and --prompt options and SVG and PNG output descriptions conflict.

Mitigation: Check the installed CLI help and inspect the result's actual format before using it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command snippets and a result URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a saved output path or an asynchronous task ID.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
