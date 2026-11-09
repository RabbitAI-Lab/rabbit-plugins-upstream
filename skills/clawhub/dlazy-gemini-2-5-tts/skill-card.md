## Description:

Generate multilingual speech audio from text using Gemini 2.5 text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to turn text into Chinese or English speech audio with selectable voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial with medium confidence and flagged a login step that was not clearly tied to the stated audio-generation purpose.

Mitigation: Review the dLazy login flow, account requirements, and pinned @dlazy/cli@1.2.3 install details before granting access.

Risk: Prompts and any referenced local media are sent to dLazy-hosted services for processing.

Mitigation: Avoid sending sensitive text or files, and review the service terms and sharing permissions before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI project page (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio]

**Output Format:** [Generated speech audio available through hosted file URLs; CLI returns a JSON result.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice language (Chinese or English) and voice are configurable.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
