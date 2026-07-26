## Description: <br>
Use PoYo AI Flux 2 through the https://api.poyo.ai/api/generate/submit endpoint to prepare PoYo-compatible payloads, submit image generation or editing jobs, and poll task status for the Flux 2 model family. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to generate or edit media with PoYo Flux 2 models by choosing a supported model, preparing request payloads, submitting authenticated API jobs, and tracking returned task IDs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, image URLs, and generated-media requests are sent to PoYo's external API. <br>
Mitigation: Use this skill only when third-party processing by PoYo is intended, and avoid submitting secrets, confidential prompts, private internal URLs, sensitive images, or regulated data unless approved under PoYo's policies. <br>
Risk: API keys could be exposed if passed directly on a command line or included in shared transcripts. <br>
Mitigation: Set POYO_API_KEY as an environment variable and avoid echoing, logging, or committing credentials. <br>


## Reference(s): <br>
- [PoYo Flux 2 model page](https://poyo.ai/models/flux-2) <br>
- [PoYo Flux 2 API docs](https://docs.poyo.ai/api-manual/image-series/flux-2) <br>
- [PoYo Flux 2 OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/flux-2.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include selected model IDs, payload summaries, reference-image notes, returned task IDs, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
