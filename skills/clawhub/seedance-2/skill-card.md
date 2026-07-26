## Description: <br>
Use PoYo AI Seedance 1.5 Pro to help agents prepare, submit, and track image-to-video generation jobs through PoYo's submit endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to assemble PoYo Seedance image-to-video payloads, submit authenticated generation requests, and preserve task IDs for status polling or webhook follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generation prompts, image URLs, and callback URLs are sent to PoYo. <br>
Mitigation: Use the skill only when sharing that content with PoYo is acceptable, and avoid submitting private images, secrets, internal URLs, or sensitive personal content. <br>
Risk: Passing the PoYo API key on the command line can expose it through shell history or process listings. <br>
Mitigation: Set POYO_API_KEY as an environment variable instead of passing the key as a command-line argument. <br>


## Reference(s): <br>
- [PoYo Seedance model page](https://poyo.ai/models/seedance-1-5-pro) <br>
- [PoYo Seedance API docs](https://docs.poyo.ai/api-manual/video-series/seedance-1-5-pro) <br>
- [PoYo Seedance OpenAPI JSON](https://docs.poyo.ai/api-manual/video-series/seedance-1-5-pro.json) <br>
- [PoYo task status docs](https://docs.poyo.ai/api-manual/task-management/status) <br>
- [Local API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON payload examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include chosen model id, payload summaries, reference-image notes, returned task IDs, and polling or webhook next steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
