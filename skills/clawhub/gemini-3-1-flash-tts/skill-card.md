## Description:

Use when someone needs spoken narration or voiceover - explainer tracks, documentary lines, or voice to pair with generated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare and run Replicate text-to-speech requests for narration, voiceover, documentary lines, and generated-video audio tracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scripts, style prompts, selected voices, language codes, and token-authenticated requests are sent to Replicate for audio generation.

Mitigation: Confirm the user is comfortable sending this content to Replicate and avoid submitting sensitive or confidential scripts unless approved.

Risk: The skill recommends installing companion skills from a remote source.

Mitigation: Review and trust the PrunaAI companion skills before installing or executing their guidance.

Risk: Generated narration can exceed downstream timing constraints for video-avatar workflows.

Mitigation: Use ffprobe to check line duration and keep audio segments within the documented downstream limits before passing them into video workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/gemini-3-1-flash-tts)
- [Replicate Gemini 3.1 Flash TTS readme](https://replicate.com/google/gemini-3.1-flash-tts/readme)
- [Replicate Gemini 3.1 Flash TTS predictions endpoint](https://api.replicate.com/v1/models/google/gemini-3.1-flash-tts/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides token-authenticated Replicate TTS requests and may reference ffmpeg or ffprobe checks for downstream audio handling.]

## Skill Version(s):

1.0.11 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
