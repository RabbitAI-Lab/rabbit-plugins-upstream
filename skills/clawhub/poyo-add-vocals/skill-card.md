## Description: <br>
Adds AI-generated vocals to uploaded instrumental audio with PoYo's add-vocals workflow, including payload preparation, submission guidance, callback setup, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to prepare and optionally submit PoYo Add Vocals requests for instrumental tracks, with guidance for lyrics or vocal prompts, style controls, callbacks, and result retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed if placed in client code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Store POYO_API_KEY only in server-side environment variables or a backend secret manager and redact authorization headers from all outputs. <br>
Risk: Private recordings, sensitive lyrics, prompts, callback URLs, or generated audio URLs may be shared with PoYo during request submission. <br>
Mitigation: Review payloads before submission and avoid sending private or sensitive content unless the user accepts that disclosure. <br>
Risk: A live API submission can start an asynchronous generation task before the user has confirmed the payload. <br>
Mitigation: Prepare payloads by default and submit only after explicit user approval from a trusted shell. <br>


## Reference(s): <br>
- [PoYo Add Vocals API Reference](references/api.md) <br>
- [PoYo Add Vocals model page](https://poyo.ai/models/add-vocals) <br>
- [PoYo Add Vocals API docs](https://docs.poyo.ai/api-manual/music-series/add-vocals) <br>
- [PoYo Add Vocals OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/add-vocals.json) <br>
- [PoYo query music detail docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo music webhook docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash or curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a PoYo task_id when the user explicitly approves a live submission.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
