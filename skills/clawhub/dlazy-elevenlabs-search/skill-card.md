## Description:

Search the ElevenLabs voice library by keyword, source, and category, and review playable previews before selecting a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can search for ElevenLabs voices by descriptor, source, and category, then review the returned previews before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to dLazy, which acts as an intermediary and may charge service credits; the external CLI package and hosted service were not fully audited.

Mitigation: Use only if comfortable sharing search terms with dLazy and accepting possible credit charges; review the service terms and send only appropriate search terms.

Risk: Logging in stores an organization API key in the local CLI configuration.

Mitigation: Use the documented DLAZY_API_KEY environment-variable option to avoid saving the key through login, and rotate or revoke the key when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Audio preview links]

**Output Format:** [Structured voice search results with voice details and playable preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be filtered by keyword, voice source, and category.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
