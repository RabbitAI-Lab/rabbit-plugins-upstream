## Description: <br>
Generate speech through PoYo using the elevenlabs-tts-turbo-2-5 text-to-speech model, including payload preparation, async task submission, callback guidance, and task status retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo text-to-speech requests, tune voice and delivery parameters, submit trusted server-side jobs, and explain how to retrieve generated speech results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text, callback URLs, and generated-task metadata are sent to PoYo when live submissions are made. <br>
Mitigation: Use the skill only when sending that data to PoYo is acceptable for the workflow, and make live submissions only with explicit intent. <br>
Risk: POYO_API_KEY exposure could allow unauthorized use of the PoYo account. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager, and never include it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Private scripts, callback URLs, task ids, or generated audio URLs may be sensitive operational data. <br>
Mitigation: Avoid logging these values unless the product policy explicitly permits it. <br>


## Reference(s): <br>
- [PoYo ElevenLabs TTS Turbo 2.5 model page](https://poyo.ai/models/elevenlabs-tts-turbo-2-5) <br>
- [PoYo ElevenLabs TTS Turbo 2.5 API documentation](https://docs.poyo.ai/api-manual/music-series/elevenlabs-tts-turbo-2-5) <br>
- [PoYo API key dashboard](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-elevenlabs-tts-turbo-2-5) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, voice and language choices, delivery controls, final payloads, returned task_id values, and next-step retrieval guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
