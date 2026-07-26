## Description: <br>
Add instrumental accompaniment to uploaded audio on PoYo via the add-instrumental API, including payload preparation, submission guidance, callback notes, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to prepare PoYo add-instrumental requests for uploaded audio, generate payloads or curl commands, submit approved jobs, and retrieve task results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a PoYo API key to submit network requests. <br>
Mitigation: Keep POYO_API_KEY in a server-side environment variable or secret manager and do not expose it in browser code, logs, screenshots, repositories, or chat output. <br>
Risk: Payloads may include private audio URLs, callback URLs, generated asset URLs, task IDs, or style notes. <br>
Mitigation: Review payloads before submission and avoid sending or logging private recordings or callback URLs unless sharing them with PoYo is acceptable. <br>
Risk: The included shell script can submit a prepared payload to PoYo. <br>
Mitigation: Run live submissions only after the user explicitly confirms the payload and intends to use PoYo for add-instrumental generation. <br>


## Reference(s): <br>
- [PoYo Add Instrumental API Reference](references/api.md) <br>
- [PoYo Add Instrumental Model Page](https://poyo.ai/models/add-instrumental) <br>
- [PoYo Add Instrumental API Docs](https://docs.poyo.ai/api-manual/music-series/add-instrumental) <br>
- [PoYo Add Instrumental OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/add-instrumental.json) <br>
- [PoYo Music Detail Docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo Music Webhook Docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, source audio URL notes, title, tags, negative tags, optional style controls, task_id, and retrieval or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
