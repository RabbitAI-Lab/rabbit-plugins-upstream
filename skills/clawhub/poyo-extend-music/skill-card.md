## Description: <br>
Extend existing music on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `extend-music`, music continuation, audio_id based extension, custom style, title, prompt, continuation timing, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Extend Music payloads, server-side curl commands, callback notes, and status-retrieval guidance for continuing an existing track from an audio_id. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API credentials, prompts, audio IDs, callback URLs, generated results, and account usage may be exposed to PoYo or logs during use. <br>
Mitigation: Keep POYO_API_KEY server-side, avoid logging private request or response data, and review payloads before submission. <br>
Risk: The helper can submit live music-extension jobs to PoYo when a prepared payload and API key are used. <br>
Mitigation: Run live API calls only after the user confirms the payload and intends to send it to PoYo. <br>


## Reference(s): <br>
- [PoYo Extend Music API Reference](references/api.md) <br>
- [PoYo Extend Music model page](https://poyo.ai/models/extend-music) <br>
- [PoYo Extend Music API docs](https://docs.poyo.ai/api-manual/music-series/extend-music) <br>
- [PoYo Extend Music OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/extend-music.json) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-extend-music) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, mode selection, source audio identifier summary, continuation settings, callback guidance, task_id, and status retrieval next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
