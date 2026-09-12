## Description:

Use when someone needs spoken narration or voiceover, including explainer tracks, documentary lines, or voice to pair with generated video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through generating text-to-speech narration with Replicate's Google Gemini 3.1 Flash TTS model, including prompt intake, voice selection, API calls, polling, and follow-on audio/video workflow guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends unpinned automatic installs of external PrunaAI skills.

Mitigation: Review the referenced skills before installation and prefer pinned versions or trusted reviewed releases.

Risk: User scripts, prompts, and generated audio are sent to a third-party Replicate API.

Mitigation: Do not submit secrets, regulated data, or private content unless Replicate use is approved for the use case.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/gemini-3-1-flash-tts)
- [Pruna AI publisher profile](https://clawhub.ai/user/pruna-ai)
- [Replicate Gemini 3.1 Flash TTS readme](https://replicate.com/google/gemini-3.1-flash-tts/readme)
- [Replicate predictions endpoint](https://api.replicate.com/v1/models/google/gemini-3.1-flash-tts/predictions)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to collect text, voice, prompt, and language_code inputs; generated audio is produced by the external Replicate model.]

## Skill Version(s):

1.0.12 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
