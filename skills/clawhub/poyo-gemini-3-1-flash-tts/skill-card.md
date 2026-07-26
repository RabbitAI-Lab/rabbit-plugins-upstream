## Description: <br>
Generate speech on PoYo via the Gemini 3.1 Flash TTS model, including payload preparation, async task submission, callback guidance, and task status retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Gemini 3.1 Flash TTS requests, choose text-to-speech options, submit trusted server-side payloads, and explain how to retrieve generated speech results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text-to-speech prompts, callback URLs, task ids, and generated audio URLs may contain sensitive information. <br>
Mitigation: Review payloads before submission and avoid sending or logging sensitive content unless policy allows it. <br>
Risk: The skill requires a PoYo API key for live submissions. <br>
Mitigation: Keep POYO_API_KEY server-side in environment variables or a secret manager and do not expose it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Live API calls send prepared text-to-speech prompts to PoYo. <br>
Mitigation: Install and use the skill only when that external submission is intended, and make live calls only from a trusted server-side environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gemini-3-1-flash-tts) <br>
- [PoYo Gemini 3.1 Flash TTS model page](https://poyo.ai/models/gemini-3-1-flash-tts) <br>
- [PoYo Gemini 3.1 Flash TTS API documentation](https://docs.poyo.ai/api-manual/music-series/gemini-3-1-flash-tts) <br>
- [API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model id, voice settings, style instructions, payload summaries, task ids, and next-step retrieval guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
