## Description: <br>
Generate music on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `elevenlabs-music`, text-to-music, instrumental music, structured composition plans, section timing, audio output formats, async task submission, callbacks, and task status retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo ElevenLabs Music payloads, submit async text-to-music or composition-plan jobs, and guide task status retrieval or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit music-generation requests to PoYo using a secret API key. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment or secret manager and do not expose it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Music prompts, lyrics, callback URLs, task IDs, or generated audio URLs may contain private workflow information. <br>
Mitigation: Review payloads before submission and avoid logging or sharing private request and result data unless it fits the product policy. <br>
Risk: Live PoYo API calls may create external network activity and generated media tasks. <br>
Mitigation: Make live calls only when the user explicitly asks and a trusted server-side shell is available. <br>


## Reference(s): <br>
- [PoYo ElevenLabs Music model page](https://poyo.ai/models/elevenlabs-music) <br>
- [PoYo ElevenLabs Music API docs](https://docs.poyo.ai/api-manual/music-series/elevenlabs-music) <br>
- [Bundled API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-elevenlabs-music) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a selected model id, input path, concise parameter summary, prepared payload, task id, and next retrieval step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
