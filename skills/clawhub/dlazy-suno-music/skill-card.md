## Description:

Suno music generation model that supports inspiration mode with automatic lyrics, custom mode with manual lyrics, and instrumental or vocal music generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate music through the dLazy Suno wrapper, including lyric-assisted songs, custom-lyric songs, and instrumental tracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external @dlazy/cli npm package and dLazy hosted API.

Mitigation: Use the pinned CLI version from the skill metadata, prefer npx for one-off use when avoiding a persistent global binary, and install only in environments where the dLazy CLI and service are trusted.

Risk: Prompts, selected media files, and generated assets may be sent to or hosted by dLazy service endpoints.

Mitigation: Avoid submitting sensitive prompts or media unless the dLazy service terms and data handling are acceptable for the intended use case.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Keep the key scoped to the user account, avoid elevated execution, and rotate or revoke the API key when access is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated-output URLs or an asynchronous task identifier when no-wait mode is used.]

## Skill Version(s):

1.3.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
