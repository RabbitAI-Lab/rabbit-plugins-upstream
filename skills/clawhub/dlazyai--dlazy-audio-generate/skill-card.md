## Description:

Audio generation skill that automatically selects an appropriate dLazy CLI audio or TTS model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to select and run dLazy CLI audio models for text-to-speech, dialogue, music, sound effects, and voice search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and user-provided media files may be sent to dLazy hosted services.

Mitigation: Avoid passing sensitive prompts or local files unless that data is appropriate for the dLazy service.

Risk: A saved dLazy API key grants access to the user's dLazy organization.

Mitigation: Use npx for one-off execution when a global binary is unnecessary, and rotate or revoke the saved API key from the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and CLI JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned @dlazy/cli 1.2.3 package, requires a dLazy API key, and may return generated media URLs hosted by dLazy.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
