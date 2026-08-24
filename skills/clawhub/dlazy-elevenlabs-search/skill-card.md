## Description:

Search the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices so users can choose a voice before running TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search dLazy's ElevenLabs voice library by prompt, voice source, category, and result count, then inspect returned previews before selecting a voice for text-to-speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party dLazy API key and sends search prompts to dLazy's hosted API.

Mitigation: Confirm the user is comfortable with dLazy API use before installation or invocation, and avoid sending sensitive prompt content unless permitted.

Risk: Authentication can persist credentials in ~/.dlazy/config.json.

Mitigation: Use DLAZY_API_KEY per invocation for tighter control, or rotate and revoke the key from the dLazy dashboard when access should change.

Risk: The skill depends on a pinned third-party CLI package and hosted dLazy endpoints.

Mitigation: Review the pinned CLI package and source link before installing, and account for availability or policy failures from the hosted API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying command returns voice-search results and may return asynchronous task metadata when invoked with no-wait behavior.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
