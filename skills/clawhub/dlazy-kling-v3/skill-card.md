## Description:

Helps agents generate Kling V3 videos from text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video or image-to-video generation with Kling V3 and retrieve the resulting media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media can be sent to dLazy for generation.

Mitigation: Share only prompts and media you are comfortable uploading to dLazy.

Risk: The CLI can store an API key in local configuration.

Mitigation: Use a per-invocation API key if you prefer not to save credentials locally.

Risk: Video generation can consume paid credits.

Mitigation: Check the cost estimate and confirm credit use before starting paid generations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI homepage listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Video links]

**Output Format:** [Markdown guidance with shell commands and generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID; completed media can be saved locally.]

## Skill Version(s):

1.3.29 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
