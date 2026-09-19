## Description:

Search the ElevenLabs voice library by keyword, source, and category, returning playable previews for matched voices before text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search ElevenLabs voice options through the dLazy CLI and choose a voice preview before generating TTS audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because the documentation mixes voice-search behavior with unrelated media-upload, async generation, and image-output examples.

Mitigation: Confirm the actual dLazy CLI behavior before using --save, passing local file paths, or relying on the documented output schema.

Risk: The dLazy CLI stores an API key locally and sends prompts and parameters to dLazy-hosted endpoints.

Mitigation: Review the third-party CLI before installing and use revocable API keys or DLAZY_API_KEY for per-invocation credentials when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy CLI authentication; search filters include prompt, voice_type, category, and page_size.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter declares 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
