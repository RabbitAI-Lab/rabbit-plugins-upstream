## Description:

Searches the ElevenLabs voice library by keyword, source, and category, returning voice matches with previews for TTS selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find and preview ElevenLabs voices before selecting one for text-to-speech projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search prompts and parameters are sent to the dLazy hosted service.

Mitigation: Use the service only when its handling of submitted search data is acceptable; avoid sensitive prompts.

Risk: Use requires a locally stored dLazy API key and an external CLI package not included in this artifact.

Mitigation: Review the pinned CLI package before use, protect or rotate the API key, and use the on-demand npx form if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI project (metadata homepage)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with voice matches and preview links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search can filter by keyword, voice source, and category; preview availability depends on the service response.]

## Skill Version(s):

1.3.29 (source: ClawHub release; bundled skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
