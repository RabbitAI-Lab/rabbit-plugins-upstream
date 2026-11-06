## Description:

Searches the ElevenLabs voice library by keyword, source, or category and returns playable previews to help choose a voice for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI assistant can search ElevenLabs voices by a short descriptor, source, and category, then review previews before choosing a voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests go to dLazy and may use account credits.

Mitigation: Use --dry-run to inspect the request and estimated cost before making an API call.

Risk: Logging in saves a revocable dLazy API key in the local CLI configuration.

Mitigation: Protect access to the local account and configuration, or supply DLAZY_API_KEY per invocation; rotate or revoke the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Voice search results, Playable previews]

**Output Format:** [JSON search results with matching voices and preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters include prompt, voice source, and category; result count defaults to 10.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
