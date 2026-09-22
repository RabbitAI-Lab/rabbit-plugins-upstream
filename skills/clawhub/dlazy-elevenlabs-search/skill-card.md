## Description:

Searches the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices before TTS use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and agents use this skill to find ElevenLabs voices by descriptor, source, and category before running text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the release suspicious because its documentation describes broader cloud upload, asset saving, and persisted API-key behavior than the stated voice-search purpose explains.

Mitigation: Review the dLazy CLI and command behavior before installation, use npx @dlazy/cli@1.2.3 for non-persistent execution when appropriate, and invoke only with inputs intended for dLazy's API endpoints.

Risk: Prompts and search parameters are sent to api.dlazy.com, and generic CLI media options may upload local files to files.dlazy.com.

Mitigation: Avoid sending sensitive prompts or local media unless the user has approved that data transfer and understands the service boundary.

Risk: The dLazy API key may be stored in ~/.dlazy/config.json or passed through DLAZY_API_KEY.

Mitigation: Protect local config permissions, avoid exposing the key in logs or shell history, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The security guidance says the documented output schema is unreliable until the publisher clarifies the real ElevenLabs search response format.

Mitigation: Treat returned result fields as untrusted, verify preview URLs and voice metadata before downstream TTS use, and handle missing or asynchronous task outputs explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON results with shell command usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; preview/result URLs are hosted by files.dlazy.com.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
