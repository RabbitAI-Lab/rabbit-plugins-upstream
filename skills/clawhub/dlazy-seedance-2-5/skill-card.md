## Description:

Generates videos with Seedance 2.5 from text prompts and optional image, video, audio, or first and last frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can use the skill to submit prompts and optional reference media to dLazy's hosted service and generate video clips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service, and generation jobs may incur costs.

Mitigation: Use the service only if you trust dLazy with the submitted content, and review generation costs before submitting jobs.

Risk: The CLI uses a dLazy API key stored in local configuration or supplied through an environment variable.

Mitigation: Protect the API key and rotate or revoke it when it is no longer needed.

## Reference(s):

- [CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video assets and JSON task or result responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video duration, resolution, aspect ratio, audio generation, and reference media are configurable.]

## Skill Version(s):

1.2.33 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
