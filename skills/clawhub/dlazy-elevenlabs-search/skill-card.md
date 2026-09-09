## Description:

Searches the ElevenLabs voice library by keyword, source, and category and returns playable previews so agents can help users choose voices before text-to-speech generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and external agent users can use this skill to search ElevenLabs voice options by descriptor, source, and category before selecting a voice for TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a pinned third-party npm CLI and sends prompts and search parameters to dLazy services.

Mitigation: Prefer the on-demand npx invocation, review the pinned package before use, and use a revocable dLazy API key.

Risk: The documentation includes broader upload and download behavior beyond basic voice-library search.

Mitigation: Avoid passing local file paths unless the command specifically requires them and review generated URLs or saved files before reuse.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses containing voice search results and preview URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and uses the pinned @dlazy/cli package version declared by the skill metadata.]

## Skill Version(s):

1.3.13 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
