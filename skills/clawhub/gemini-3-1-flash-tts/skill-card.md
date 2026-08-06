## Description: <br>
Use when someone needs spoken narration or voiceover - explainer tracks, documentary lines, or voice to pair with generated video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to prepare Replicate Gemini Flash TTS requests for narration, explainer tracks, documentary lines, and voiceover audio paired with generated video. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user's script and style prompt to Replicate for text-to-speech generation. <br>
Mitigation: Confirm the script, voice, language, and style prompt with the user before making the Replicate request. <br>
Risk: Generated audio may need length checks or editing before it is used in downstream video or narration workflows. <br>
Mitigation: Use ffmpeg or ffprobe when trimming, concatenating, mixing, or verifying clip length for downstream use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/gemini-3-1-flash-tts) <br>
- [Replicate Gemini 3.1 Flash TTS readme](https://replicate.com/google/gemini-3.1-flash-tts/readme) <br>
- [Replicate Gemini 3.1 Flash TTS predictions endpoint](https://api.replicate.com/v1/models/google/gemini-3.1-flash-tts/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent through Replicate TTS request setup, polling, download, and optional audio post-processing.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
