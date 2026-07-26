## Description: <br>
Generate speech through PoYo's ElevenLabs V3 TTS API by preparing text-to-speech payloads, selecting voice and delivery options, submitting async tasks, and guiding result retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create PoYo ElevenLabs V3 TTS requests, choose voice, language, timestamp, and text-normalization options, and submit or explain async speech-generation workflows. It is suited for server-side workflows that need concise payload guidance, curl examples, or task status retrieval steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: TTS payloads may contain private text, callback URLs, task IDs, audio URLs, timestamp files, or customer content. <br>
Mitigation: Review payload JSON before submission and avoid logging generated IDs, URLs, audio, timestamps, or customer text unless policy allows it. <br>
Risk: Exposing POYO_API_KEY can authorize unintended PoYo API usage. <br>
Mitigation: Keep POYO_API_KEY server-side in an environment variable or secret manager and never place it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: The skill submits jobs to PoYo's external API when a live request is explicitly run. <br>
Mitigation: Use it only when sending TTS job payloads to PoYo is intended, and make live calls only from a trusted shell or server-side environment. <br>


## Reference(s): <br>
- [PoYo ElevenLabs V3 TTS model page](https://poyo.ai/models/elevenlabs-v3-tts) <br>
- [PoYo ElevenLabs V3 TTS API documentation](https://docs.poyo.ai/api-manual/music-series/elevenlabs-v3-tts) <br>
- [Skill API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id after an explicitly requested live submission; execution requires curl and a server-side POYO_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
