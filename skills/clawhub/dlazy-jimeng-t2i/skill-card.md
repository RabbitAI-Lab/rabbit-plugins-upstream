## Description:

Generates images from text prompts with Jimeng through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts, optionally using reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided local media are sent to the third-party dLazy service.

Mitigation: Review prompts and media before submission, and use the service only when that sharing is acceptable.

Risk: Generation consumes dLazy credits and requires an API key that can be saved locally.

Mitigation: Check costs with --dry-run; use DLAZY_API_KEY per invocation if you prefer not to save the key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and JSON containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Images can be saved locally; asynchronous jobs may return a task ID instead of an image URL.]

## Skill Version(s):

1.3.28 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
