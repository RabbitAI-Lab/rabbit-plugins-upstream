## Description:

Generates multilingual speech audio from a prompt using the Gemini 2.5 text-to-speech service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to turn a text prompt into speech audio in Chinese or English, with optional voice selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete: the stated TTS purpose differs from the reported authentication-only behavior, and CLI/package resolution was incomplete.

Mitigation: Verify the pinned @dlazy/cli package and confirm the TTS command behaves as documented before installing it or sharing sensitive prompts.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Hosted audio URL with JSON result or task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Chinese and English voice settings; asynchronous mode may return a task ID.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
