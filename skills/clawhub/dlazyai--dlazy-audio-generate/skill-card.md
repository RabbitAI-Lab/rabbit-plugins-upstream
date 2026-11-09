## Description:

Generates speech, music, dialogue, and sound effects by selecting an appropriate dLazy audio or text-to-speech model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can request generated speech, music, dialogue, or sound effects and have the skill choose a suitable audio model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any local media supplied to the skill are sent to dLazy hosted services.

Mitigation: Avoid submitting sensitive prompts or media, and review dLazy's service terms before use.

Risk: The security review was partial and noted a mismatch between the audio/TTS description and reported visual-media examples.

Mitigation: Review the skill and its unresolved references before installation, and confirm its behavior matches the intended audio tasks.

Risk: The documented voice-library search expects one short English descriptor, which may not suit every user's search terms.

Mitigation: Use a concise English keyword as directed, then review the returned voice previews before choosing.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, Voice search results, JSON result envelopes]

**Output Format:** [Hosted audio files returned with URLs and JSON result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice search can return playable previews; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
