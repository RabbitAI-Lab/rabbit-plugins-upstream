## Description: <br>
Helps agents prepare and submit PoYo Upload and Extend Audio requests for uploaded-audio continuation, custom parameters, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a user has chosen PoYo for an uploaded-audio extension workflow and needs payload guidance, server-side curl commands, callback setup, or music result retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys could be exposed through browser code, logs, screenshots, repositories, or chat output. <br>
Mitigation: Keep POYO_API_KEY in a server-side secret store and avoid printing authorization headers or secrets. <br>
Risk: Audio URLs, callback URLs, lyrics, task ids, or customer data may be shared with PoYo during an extension job. <br>
Mitigation: Review payloads before submission and send private or customer data only when policy permits sharing it with PoYo. <br>
Risk: A live API submission could start an unintended PoYo audio-extension job. <br>
Mitigation: Submit requests only after the user explicitly asks for a live PoYo call and confirms the prepared payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-upload-and-extend-audio) <br>
- [PoYo Upload and Extend Audio model page](https://poyo.ai/models/upload-and-extend-audio) <br>
- [PoYo Upload and Extend Audio API docs](https://docs.poyo.ai/api-manual/music-series/upload-and-extend-audio) <br>
- [PoYo Upload and Extend Audio OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/upload-and-extend-audio.json) <br>
- [PoYo music detail docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo music webhook docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payload examples and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, upload URL handling notes, parameter summaries, task id reporting, callback guidance, and music detail retrieval next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
