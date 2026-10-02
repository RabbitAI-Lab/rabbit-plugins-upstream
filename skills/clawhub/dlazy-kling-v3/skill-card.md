## Description:

Helps an agent generate Kling V3 videos from text prompts or reference images through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video or image-to-video generation and retrieve the resulting media link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy.

Mitigation: Review prompts and media for sensitive content before submitting them.

Risk: Generation may consume paid credits.

Mitigation: Use the available cost-estimate dry run and confirm expected charges before generating.

Risk: Authentication may save an API key locally.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: Saving results writes media to a local path.

Mitigation: Use an explicitly approved destination when requesting a local download.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON responses]

**Output Format:** [Markdown guidance with shell commands; CLI results in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include a media URL or an asynchronous task ID; saving media locally is optional.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
