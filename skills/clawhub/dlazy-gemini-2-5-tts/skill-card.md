## Description:

Generate multilingual speech audio with Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to turn text into Chinese or English speech and select a voice. The skill documents submitting the request through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign but medium confidence and incomplete; it could not demonstrate how the advertised TTS commands behave and did not resolve some local references.

Mitigation: Before running the CLI, review the pinned package and its login/API-key flow, and use a key you trust that can be rotated or revoked.

## Reference(s):

- [CLI project (skill metadata link)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands, Guidance]

**Output Format:** [Audio generation result with JSON metadata; Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill documents Chinese and English voice options and requires a dLazy API key.]

## Skill Version(s):

1.3.42 (source: ClawHub server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
