## Description:

Searches the ElevenLabs voice library by keyword, source, and category to help users choose a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can search ElevenLabs voices by a short descriptive keyword, voice source, and category, then review matching voice details and preview assets before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the integration sends requests through dLazy and may incur credit costs; the service handles API authentication and voice-search data.

Mitigation: Review dLazy data handling and credit terms, and avoid sending sensitive information unless permitted.

Risk: Logging in stores an API key in the local dLazy CLI configuration.

Mitigation: Keep the local configuration private, do not expose the key in prompts or logs, and rotate or revoke it if compromised.

Risk: The documented response example shows an image output although the skill describes voice preview samples.

Mitigation: Check the actual returned media type and preview behavior before relying on it to audition voices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Text, Preview asset URLs]

**Output Format:** [Structured voice-search results with matching voice details and preview asset links; the documented example shows an image output, so confirm the preview media type.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are filtered by keyword, voice source, and category; preview media behavior should be confirmed.]

## Skill Version(s):

1.3.33 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
