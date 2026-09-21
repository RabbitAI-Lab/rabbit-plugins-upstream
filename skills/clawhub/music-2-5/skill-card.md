## Description:

Use when someone wants an original AI song with vocals, sung lyrics, a style prompt track, or source audio for a music video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect lyrics and style inputs, call Replicate's MiniMax music-2.5 model, and download the generated song for use directly or as source audio for video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote skill package installs can change installed agent behavior.

Mitigation: Review the remote package and prefer pinned, reviewed versions before running the npx skills add commands, especially the full-suite install.

Risk: Lyrics, prompts, and related generation data are sent to Replicate/MiniMax.

Mitigation: Do not submit confidential lyrics, secrets, regulated data, or content you are not authorized to send to Replicate/MiniMax.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-2-5)
- [Replicate MiniMax music-2.5 predictions API](https://api.replicate.com/v1/models/minimax/music-2.5/predictions)
- [MiniMax privacy policy](https://www.minimax.io/platform/protocol/privacy-policy)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent guidance may include Replicate API polling and download steps; the remote model returns generated audio.]

## Skill Version(s):

1.0.13 (source: evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
