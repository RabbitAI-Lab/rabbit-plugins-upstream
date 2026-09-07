## Description:

Searches the ElevenLabs voice library by keyword, source, and category and returns playable previews for matched voices before TTS use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and agents use this skill to find ElevenLabs voices through the dLazy CLI, filter by voice source and category, and choose a playable preview for later TTS work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses dLazy hosted services and may send search parameters and account credentials to dLazy.

Mitigation: Install only if you trust dlazy-ai, use a scoped and revocable API key, and avoid sending sensitive prompts or parameters.

Risk: The artifact instructions mention local file uploads and generated media behavior that may not be necessary for voice search.

Mitigation: Prefer simple search-only invocations, avoid passing local file paths unless intentionally uploading files, and review CLI help before use.

Risk: The documented output schema mixes voice-search behavior with image/generation-style responses.

Mitigation: Verify actual CLI output before relying on returned fields or automating downstream actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with bash examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; results may include playable preview URLs, dry-run output, or async task status.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
