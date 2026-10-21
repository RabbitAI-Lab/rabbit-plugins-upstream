## Description:

Search the ElevenLabs voice library by keyword, source, and category to find playable voice previews for TTS selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to filter ElevenLabs voices and compare previews before choosing a voice for text-to-speech projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search prompts and parameters are sent to dLazy-hosted services.

Mitigation: Avoid submitting sensitive information and review the third-party service terms before use.

Risk: The dLazy CLI uses an API key and may upload local files if file paths are supplied.

Mitigation: Keep the key private, use on-demand npx if a global install is unwanted, and provide local paths only when upload is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI repository (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and JSON voice-search results with preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports keyword, voice-source, category, and result-count filters; requires a dLazy API key.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
