## Description:

Automatically selects a suitable dLazy CLI audio or text-to-speech model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can request speech, music, dialogue, or sound effects from prompts and receive hosted audio outputs through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation includes image and video capabilities beyond its stated audio and text-to-speech purpose, as well as an English-only voice-search instruction.

Mitigation: Confirm these extra capabilities fit the intended use and use only the relevant model commands.

Risk: The security scan had partial coverage because several referenced local paths were missing.

Mitigation: Review the related paths and documentation before treating the scan as complete.

## Reference(s):

- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Text, JSON]

**Output Format:** [Hosted audio outputs and JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and supplied media are sent to dLazy's hosted service; generated audio is returned through hosted URLs.]

## Skill Version(s):

1.3.47 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
