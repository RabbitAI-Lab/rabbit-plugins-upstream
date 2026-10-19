## Description:

Helps agents generate and edit videos with Happy Horse 1.0 using text prompts, first frames, reference images, or existing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video, first-frame-to-video, reference-to-video, and video editing through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy's hosted service.

Mitigation: Only submit prompts and files you intend to share with that service.

Risk: Signing in can save an API key in local configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY and the npx invocation if you prefer less local persistence.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return task status or links to generated media.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
