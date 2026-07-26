## Description: <br>
Generate Music on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `generate-music`, AI music generation, background tracks, soundtrack drafts, instrumental songs, custom mode, music callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo music-generation payloads, choose simple or custom mode, submit async music tasks, and guide retrieval through webhooks or music detail queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses POYO_API_KEY to submit PoYo API requests. <br>
Mitigation: Keep the key in server-side environment variables or a backend secret manager, and do not expose it in browser code, public repositories, logs, screenshots, or chat output. <br>
Risk: Prompts, callback URLs, generated media URLs, and private lyrics may contain sensitive information. <br>
Mitigation: Review payloads before submission and avoid logging or publicly sharing sensitive request or result data unless the product policy allows it. <br>
Risk: Submitting music-generation jobs may incur provider usage costs. <br>
Mitigation: Make live API calls only when the user explicitly requests submission from a trusted server-side shell and has approved the payload. <br>
Risk: PoYo model-specific request fields can change over time. <br>
Mitigation: Verify current field support in PoYo's documentation before relying on options such as mv, negative_tags, and style_weight. <br>


## Reference(s): <br>
- [PoYo Generate Music API Reference](references/api.md) <br>
- [PoYo Generate Music model page](https://poyo.ai/models/generate-music) <br>
- [PoYo Generate Music API docs](https://docs.poyo.ai/api-manual/music-series/generate-music) <br>
- [PoYo query music detail docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo music webhook docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include the selected model id, mode choice, instrumental or vocal intent, final payload or concise parameter summary, returned task_id after submission, and next retrieval step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
