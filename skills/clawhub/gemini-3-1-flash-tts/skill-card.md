## Description: <br>
Use when someone needs spoken narration or voiceover for explainer tracks, documentary lines, or voice to pair with generated video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to prepare Replicate Gemini Flash TTS requests for narrated explainers, documentary lines, voiceover tracks, and generated-video audio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends narration text and related prompt details to Replicate for text-to-speech generation. <br>
Mitigation: Use it only when sharing that text with Replicate is acceptable, and provide a Replicate API token only in an environment intended for this workflow. <br>
Risk: Additional prerequisite skills may be installed before generation, including the full Pruna suite option. <br>
Mitigation: Review the referenced PrunaAI prerequisite skills before installing them, especially when choosing the full suite. <br>
Risk: Long audio or video-bound narration can exceed model or downstream clip limits. <br>
Mitigation: Keep combined text and prompt within the documented byte limit, use ffmpeg or ffprobe when trimming or validating duration, and keep p-video-bound lines near 19 seconds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/gemini-3-1-flash-tts) <br>
- [Replicate Gemini 3.1 Flash TTS readme](https://replicate.com/google/gemini-3.1-flash-tts/readme) <br>
- [Replicate prediction API endpoint](https://api.replicate.com/v1/models/google/gemini-3.1-flash-tts/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides collection of text, voice, prompt, language_code, and Replicate API token before generating audio.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
