## Description:

Use when someone wants an original AI song with vocals - sung lyrics, a style prompt track, or source audio for a music video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate original vocal songs from lyrics and optional style prompts, including source audio for music-video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions use mutable third-party npx skill installs that may change between runs.

Mitigation: Review the referenced PrunaAI skills and installer source before use; prefer pinned versions or immutable commits where possible.

Risk: Lyrics, prompts, and related generation inputs are sent to hosted APIs.

Mitigation: Avoid confidential lyrics, prompts, secrets, or regulated data, and confirm user consent before submission.

## Reference(s):

- [ClawHub music-2.5 skill page](https://clawhub.ai/pruna-ai/skills/music-2-5)
- [Replicate MiniMax music-2.5 predictions API](https://api.replicate.com/v1/models/minimax/music-2.5/predictions)
- [MiniMax privacy policy](https://www.minimax.io/platform/protocol/privacy-policy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline bash and JSON/curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to submit lyrics and style prompts, poll generation status, and download generated audio output.]

## Skill Version(s):

1.0.12 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
