## Description: <br>
Helps agents prepare and submit PoYo Upload and Cover Audio jobs, including payloads, server-side curl commands, callbacks, and music detail retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to integrate PoYo's upload-and-cover-audio model into audio cover workflows, prepare safe request payloads, submit asynchronous jobs, and retrieve or handle results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY could be exposed if placed in browser code, logs, screenshots, chat output, or public repositories. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and avoid echoing authorization headers. <br>
Risk: Payloads may disclose private audio URLs, sensitive lyrics, generated audio URLs, callback URLs, or task identifiers to PoYo or logs. <br>
Mitigation: Review payloads before submission and avoid sending or logging private content unless the use case permits sharing it with PoYo. <br>
Risk: The skill can submit live asynchronous jobs to an external PoYo API when used with a prepared payload. <br>
Mitigation: Make live API calls only after the user explicitly asks to submit the payload and confirms use of a safe server-side environment. <br>


## Reference(s): <br>
- [PoYo Model Page](https://poyo.ai/models/upload-and-cover-audio) <br>
- [PoYo Upload and Cover Audio API Docs](https://docs.poyo.ai/api-manual/music-series/upload-and-cover-audio) <br>
- [PoYo Upload and Cover Audio OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/upload-and-cover-audio.json) <br>
- [PoYo Query Music Detail Docs](https://docs.poyo.ai/api-manual/music-series/query-music-detail) <br>
- [PoYo Music Webhook Docs](https://docs.poyo.ai/api-manual/music-series/music-webhook) <br>
- [Skill API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coolhackboy/skills/poyo-upload-and-cover-audio) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payloads and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model id, source audio URL handling notes, mode choice, prompt/style/title settings, task_id after submission, and the next retrieval or webhook step.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
