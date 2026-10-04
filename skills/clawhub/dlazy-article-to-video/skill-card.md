## Description:

Turns articles and documents into narrated explainer videos through the hosted dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn written articles or documents into narrated explainer, training, or report videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy's hosted service.

Mitigation: Submit sensitive documents only when your organization permits use of the service.

Risk: Logging in can save an API key on the local machine.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent local storage is not desired.

Risk: Running the dLazy CLI executes third-party package code.

Mitigation: Review the pinned CLI package and its listed source before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-article-to-video)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video links, Guidance]

**Output Format:** [Text responses with project status and links to generated video when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation takes place in the hosted dLazy service.]

## Skill Version(s):

1.0.28 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
