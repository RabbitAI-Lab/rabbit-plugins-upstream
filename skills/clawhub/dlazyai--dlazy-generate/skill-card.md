## Description:

Generates images, videos, and audio by selecting a suitable dLazy CLI model for the user's request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can request image, video, or audio generation and have the skill select a matching dLazy model and return generated media results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad generate trigger may activate for unrelated requests.

Mitigation: Invoke the skill only when the user explicitly requests media generation or editing.

Risk: Prompts and supplied media are reported as sent to dLazy's API and media storage.

Mitigation: Avoid submitting sensitive prompts or files, and confirm the content is appropriate to share with the service.

Risk: Some linked or mentioned details were not fully validated in the security review.

Mitigation: Review the relevant service and package information before relying on those details.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, Videos, Audio, JSON]

**Output Format:** [JSON response envelope with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media outputs are hosted URLs; output content depends on the selected generation model.]

## Skill Version(s):

1.3.45 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
