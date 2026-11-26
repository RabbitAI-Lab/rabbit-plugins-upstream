## Description:

Generates images, videos, and audio by selecting a dLazy CLI model based on the request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can request image, video, or audio generation and have the skill select a suitable dLazy model and CLI command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad “generate” trigger may route unrelated requests into a media generation workflow.

Mitigation: Confirm that image, video, or audio generation is intended before invoking the skill.

Risk: Prompts and supplied local media may be sent to dLazy hosted services, and generation may incur charges.

Mitigation: Avoid sending sensitive content and check consent and account costs before submitting a request.

Risk: The security scan was partial because some referenced local materials could not be resolved.

Mitigation: Review the skill instructions and relevant references before installing or using the workflow.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI repository (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, JSON, Image, video, and audio URLs]

**Output Format:** [JSON responses containing hosted media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; model and media type depend on the request.]

## Skill Version(s):

1.3.46 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
