## Description:

Generates and edits images from text prompts and reference images using Nano Banana 2.0.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from prompts and optional reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service.

Mitigation: Send only content you are comfortable sharing with dLazy.

Risk: The CLI can save an API key in local configuration.

Mitigation: Use a revocable key or supply DLAZY_API_KEY per invocation if you prefer not to save it locally.

Risk: Installing the third-party CLI grants it access to the environment where it runs.

Mitigation: Review the pinned CLI before global installation or use the documented npx invocation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON with image URLs; optionally saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID before images are ready.]

## Skill Version(s):

1.3.28 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
