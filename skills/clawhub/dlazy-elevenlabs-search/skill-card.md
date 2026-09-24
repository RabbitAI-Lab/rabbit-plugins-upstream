## Description:

Searches the ElevenLabs voice library by keyword, source, and category, returning playable previews so users can choose voices before TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search ElevenLabs voices by keyword, source, and category before selecting a voice for text-to-speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the broader dLazy CLI, which can store API keys, upload local media paths, download assets, and run async tasks.

Mitigation: Use npx @dlazy/cli@1.2.3 or DLAZY_API_KEY for less persistence, review the CLI source or package before global install, and pass only files intended for upload.

Risk: Prompts, parameters, and selected local media paths are sent to dLazy services.

Mitigation: Avoid sensitive prompts and local file paths unless disclosure to the service is intended.

Risk: A locally saved dLazy API key may persist in user configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistence is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns voice-search results with preview URLs; async mode may return a task identifier for polling.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
