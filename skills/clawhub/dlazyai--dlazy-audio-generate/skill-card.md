## Description:

Generates audio by selecting a dLazy CLI audio or text-to-speech model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can request speech, music, dialogue, or sound effects in natural language; the skill chooses a dLazy audio model and returns generated audio links and result details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy; local media paths passed to media fields are uploaded.

Mitigation: Review prompts and media before submission, and avoid sending sensitive content.

Risk: The external CLI implementation and its claimed local file protections are unverified; login stores an API key in local configuration.

Mitigation: Review the pinned @dlazy/cli@1.2.3 before installing, and rotate or revoke the API key if needed.

Risk: Audio generation can consume paid credits.

Mitigation: Monitor credit use while generating audio.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files or hosted URLs, JSON result metadata, Shell commands]

**Output Format:** [Hosted audio URLs with JSON result envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are hosted by dLazy; CLI results can be piped into subsequent commands.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
