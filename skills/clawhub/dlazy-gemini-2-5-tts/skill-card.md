## Description:

Generate multilingual, natural-sounding speech from text using Gemini 2.5 text-to-speech through the dLazy hosted CLI/API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate Mandarin or English speech audio from a text prompt with selectable Gemini 2.5 TTS voices. It is useful when an agent workflow needs a cloud-hosted text-to-speech step exposed through shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any explicitly supplied local media files are sent to dLazy hosted services for generation.

Mitigation: Avoid submitting sensitive or restricted content unless the user has approved that hosted-service processing.

Risk: Authentication can store a dLazy API key in the local user configuration file.

Mitigation: Prefer per-invocation DLAZY_API_KEY for temporary use, or review file permissions on ~/.dlazy/config.json when storing a key locally.

Risk: A global CLI install persists the dLazy executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gemini-2-5-tts)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI returns hosted audio output URLs or asynchronous task status.]

## Skill Version(s):

1.3.5 (source: server release metadata; artifact frontmatter reports 1.3.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
