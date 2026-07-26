## Description: <br>
Helps agents prepare, submit, and retrieve PoYo Create Music Video API tasks using source task and audio identifiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare PoYo Create Music Video payloads, submit server-side curl requests when explicitly confirmed, and retrieve asynchronous task status or webhook results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: POYO_API_KEY or authorization headers could be exposed through client-side code, chat output, screenshots, repositories, or logs. <br>
Mitigation: Keep POYO_API_KEY in server-side environment variables or a backend secret manager and avoid printing authorization headers. <br>
Risk: Task IDs, audio IDs, callback URLs, and generated media URLs may disclose private workflow or media details if logged. <br>
Mitigation: Review payloads before submission and avoid logging identifiers, callback URLs, and generated media URLs unless product policy permits it. <br>
Risk: A live request to PoYo can create an external asynchronous generation task. <br>
Mitigation: Submit only after explicit user confirmation from a trusted server-side shell with the intended payload. <br>


## Reference(s): <br>
- [PoYo Create Music Video API Reference](artifact/references/api.md) <br>
- [PoYo Create Music Video Model Page](https://poyo.ai/models/create-music-video) <br>
- [PoYo Create Music Video API Docs](https://docs.poyo.ai/api-manual/music-series/create-music-video) <br>
- [PoYo Create Music Video OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/create-music-video.json) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON payload examples and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POYO_API_KEY and user confirmation before live PoYo API submission.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
