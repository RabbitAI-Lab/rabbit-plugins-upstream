## Description:

Search the ElevenLabs voice library by keyword, source, and category to find voices and preview samples for TTS selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers search available voices by keyword, source, or category and preview matches before choosing a voice for TTS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the third-party CLI requires trust in its package and dLazy account model.

Mitigation: Review the pinned @dlazy/cli package and service terms before installing or authenticating.

Risk: Search queries and parameters are sent to the dLazy service, and API keys may be stored locally.

Mitigation: Avoid sensitive queries; use the per-invocation DLAZY_API_KEY option when local key persistence is unsuitable.

Risk: The documentation includes image and media examples that may be inaccurate; supplying local file paths could upload files.

Mitigation: Confirm CLI behavior and do not supply local file paths unless the upload is intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [CLI JSON responses with voice search results and preview references; Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice results may include playable previews; the documentation's sample JSON instead depicts an image, so confirm actual response shape. Async mode returns a task ID for later polling.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
