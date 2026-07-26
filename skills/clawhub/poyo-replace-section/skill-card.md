## Description: <br>
Helps agents prepare PoYo Replace Section music-editing payloads, submit async requests to PoYo when explicitly authorized, and explain result retrieval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to replace a time range in an existing PoYo-generated music track by preparing the required task, audio, prompt, timing, lyric, and callback parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PoYo API credentials could be exposed if placed in frontend code, logs, screenshots, public repositories, or chat output. <br>
Mitigation: Store POYO_API_KEY in a server-side secret store and avoid printing authorization headers or credentials. <br>
Risk: Private prompts, lyrics, task IDs, audio IDs, callback URLs, or generated URLs could be unintentionally logged during music editing workflows. <br>
Mitigation: Review payloads before submission and avoid logging sensitive request or result details unless product policy allows it. <br>
Risk: A live PoYo request sends user-provided music-editing content and identifiers to an external API. <br>
Mitigation: Submit only after the user explicitly confirms the payload and the execution environment is trusted. <br>


## Reference(s): <br>
- [PoYo Replace Section model page](https://poyo.ai/models/replace-section) <br>
- [PoYo Replace Section API documentation](https://docs.poyo.ai/api-manual/music-series/replace-section) <br>
- [PoYo Replace Section OpenAPI JSON](https://docs.poyo.ai/api-manual/music-series/replace-section.json) <br>
- [Local API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-replace-section) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON payloads and bash curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a returned PoYo task_id when the user explicitly authorizes submission.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
