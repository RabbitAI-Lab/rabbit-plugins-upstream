## Description:

Search the ElevenLabs voice library by keyword, source, and category, and return playable previews to help users choose a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Voice and audio production users can search for ElevenLabs voices by descriptor, source, and category, then listen to previews before selecting a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice search parameters are sent to dLazy, and login stores an organization API key locally.

Mitigation: Avoid sensitive search terms, keep the key private, and rotate or revoke it when it is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Voice search results with voice details and playable preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search requires a dLazy API key; results depend on the selected search filters.]

## Skill Version(s):

1.3.36 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
