## Description:

Use when someone needs spoken narration or voiceover - explainer tracks, documentary lines, or voice to pair with generated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to prepare text-to-speech narration or voiceover requests for the Replicate-hosted google/gemini-3.1-flash-tts model, including voice, language, and style-prompt choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends installing unpinned external skills that may change after review.

Mitigation: Review the PrunaAI skill source and prefer pinned or otherwise verified skill versions before running the listed npx skills add commands, especially the full-suite install.

Risk: Text submitted for narration is sent to Replicate using the user's API token.

Mitigation: Avoid sensitive or private script text unless the user is comfortable sending it to Replicate under their account and token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/gemini-3-1-flash-tts)
- [Replicate model readme](https://replicate.com/google/gemini-3.1-flash-tts/readme)
- [Replicate predictions API endpoint](https://api.replicate.com/v1/models/google/gemini-3.1-flash-tts/predictions)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to confirm text, voice, style prompt, language code, Replicate API token availability, and optional ffmpeg-based audio checks.]

## Skill Version(s):

1.0.13 (source: release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
