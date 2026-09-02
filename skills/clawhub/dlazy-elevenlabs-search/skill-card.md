## Description:

Searches the ElevenLabs voice library by keyword, source, and category, returning playable voice previews so an agent can help select a voice before text-to-speech generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to search available ElevenLabs voices by prompt, source, category, and result count, then choose a playable preview for downstream TTS work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice-search terms, filters, and account context are sent to dLazy's hosted service.

Mitigation: Avoid sensitive search terms unless approved for that service, and review dLazy account and service terms before use.

Risk: Authentication may persist an API key in the local dLazy CLI config.

Mitigation: Use per-invocation DLAZY_API_KEY or npx @dlazy/cli@1.2.3 when persistent global installation or saved credentials are not desired; rotate or revoke keys from the dLazy dashboard as needed.

Risk: Some artifact documentation appears copied from generic dLazy tooling and incorrectly describes image outputs or local media uploads for this voice-search command.

Mitigation: Treat those image-output and media-upload statements as generic documentation, and rely on the elevenlabs-search CLI help and server security guidance for this skill's actual behavior.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy service homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON search-result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; voice search terms and filters are sent to dLazy's hosted service.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
