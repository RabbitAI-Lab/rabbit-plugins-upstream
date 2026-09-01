## Description:

Use when someone needs spoken narration or voiceover - explainer tracks, documentary lines, or voice to pair with generated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to guide an agent through Replicate-based text-to-speech generation for narration, voiceover, and audio tracks paired with video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided text and style prompts to Replicate using the user's API token.

Mitigation: Confirm the user intends to submit the content to Replicate and avoid sending sensitive text or prompts unless the user has approved that use.

Risk: The skill suggests installing related prerequisite skills with npx before generation.

Mitigation: Review the referenced Pruna prerequisite skills and install commands before allowing those commands to run.

## Reference(s):

- [Replicate Gemini 3.1 Flash TTS readme](https://replicate.com/google/gemini-3.1-flash-tts/readme)
- [Replicate Gemini 3.1 Flash TTS prediction endpoint](https://api.replicate.com/v1/models/google/gemini-3.1-flash-tts/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided text; optional voice, prompt, and language_code; uses REPLICATE_API_TOKEN and may require ffmpeg or ffprobe for media post-processing.]

## Skill Version(s):

1.0.10 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
