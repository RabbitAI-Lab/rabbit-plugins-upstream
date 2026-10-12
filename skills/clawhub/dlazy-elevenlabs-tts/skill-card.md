## Description:

Helps agents generate multilingual speech for dubbing, audiobooks, and character dialogue using ElevenLabs voices through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate multilingual voiceovers, audiobooks, and character dialogue with selectable voices and speech controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and intentionally supplied local files may be sent to a third-party cloud service.

Mitigation: Review content and file paths before submission; avoid sending sensitive material without approval.

Risk: Signing in saves an API key locally, and installing the CLI globally persists a third-party executable.

Mitigation: Protect the local key and consider the pinned on-demand npx option instead of a global install.

Risk: The documented text-to-speech output example shows an image rather than audio.

Mitigation: Verify the actual response and output type with the publisher before relying on that example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown guidance and CLI JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed tasks return hosted result URLs; asynchronous tasks return a task ID for later retrieval.]

## Skill Version(s):

1.3.28 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
