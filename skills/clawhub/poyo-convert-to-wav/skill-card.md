## Description: <br>
Convert generated music tracks to WAV on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `convert-to-wav`, WAV export from a completed music task_id plus audio_id, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to prepare PoYo Convert-to-WAV payloads, submit trusted server-side conversion requests, and retrieve asynchronous status for completed PoYo music tracks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A PoYo API key could be exposed if it is placed in client-side code, logs, public repositories, screenshots, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side secret or environment variable and avoid printing authorization headers. <br>
Risk: Private task IDs, audio IDs, callback URLs, prompts, or generated file URLs could expose user or project data. <br>
Mitigation: Review payloads and keep those values out of logs, screenshots, and chat unless policy explicitly allows sharing. <br>
Risk: Submitting a payload sends a live conversion request to PoYo. <br>
Mitigation: Make live API calls only from a trusted server-side shell after the user confirms the prepared payload should be submitted. <br>


## Reference(s): <br>
- [PoYo Convert to WAV model page](https://poyo.ai/models/convert-to-wav) <br>
- [PoYo Convert to WAV API docs](https://docs.poyo.ai/api-manual/music-series/convert-to-wav) <br>
- [PoYo Convert to WAV OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/convert-to-wav.json) <br>
- [API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-convert-to-wav) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model selection, source task and audio identifiers, callback setup, submission result task_id, and status-retrieval next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
