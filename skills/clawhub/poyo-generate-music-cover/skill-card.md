## Description: <br>
Generate music cover versions on PoYo / poyo.ai via `https://api.poyo.ai/api/generate/submit`; use for `generate-music-cover`, cover generation from a completed music task_id, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Generate Music Cover payloads from a completed music task, submit asynchronous cover-generation jobs, and explain callback or status retrieval steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API keys and authorization headers can be exposed if copied into browser code, public repositories, logs, screenshots, or chat output. <br>
Mitigation: Keep `POYO_API_KEY` in a server-side environment variable or backend secret manager and redact authorization headers from outputs and logs. <br>
Risk: The submission script can make a live external API request that creates a PoYo task when run with a real API key and payload. <br>
Mitigation: Run live submissions only after the user confirms the payload and intended PoYo workflow, and use least-privilege service credentials. <br>
Risk: Task ids, callback URLs, prompts, and generated audio URLs may identify private jobs or customer data. <br>
Mitigation: Avoid logging or sharing private task identifiers, callback URLs, prompts, and generated audio URLs unless the applicable product policy allows it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-generate-music-cover) <br>
- [PoYo Generate Music Cover model page](https://poyo.ai/models/generate-music-cover) <br>
- [PoYo Generate Music Cover API docs](https://docs.poyo.ai/api-manual/music-series/generate-music-cover) <br>
- [PoYo Generate Music Cover OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/generate-music-cover.json) <br>
- [Local API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include PoYo model id, source task id summary, callback setup summary, request payload, returned task_id, and next retrieval step.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
