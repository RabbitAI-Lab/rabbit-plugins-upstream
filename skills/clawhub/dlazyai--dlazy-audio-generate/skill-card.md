## Description:

Audio generation skill. Automatically selects the best dlazy CLI audio/TTS model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can create speech, dialogue, music, and sound effects from prompts by selecting a suitable dLazy audio model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reported image and video workflows extend beyond the skill’s stated audio and TTS focus.

Mitigation: Confirm the requested task and selected model are within the intended audio workflow before execution.

Risk: Prompts and supplied local media are sent to dLazy hosted services, and local media may be uploaded.

Mitigation: Avoid supplying sensitive prompts or files unless they are appropriate to share with the service.

Risk: The scanner could not resolve several local references, leaving some installation details unassessed.

Mitigation: Review the package and installation instructions before installing or updating the CLI.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project page (skill-declared link)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Audio, Text]

**Output Format:** [Generated audio or hosted audio URLs with text or JSON result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; generated media is hosted by the service.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
