## Description: <br>
Helps agents prepare and submit PoYo GPT Image 2 generation and editing requests, including text-to-image, reference-guided generation, and multi-image edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolhackboy](https://clawhub.ai/user/coolhackboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create PoYo GPT Image 2 payloads, choose generation or editing modes, and optionally submit requests with a PoYo API key. It is appropriate when users intend to send prompts, image URLs, and optional callback URLs to PoYo's external API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coolhackboy/skills/poyo-gpt-image-2) <br>
- [PoYo GPT Image 2 model page](https://poyo.ai/models/gpt-image-2) <br>
- [PoYo GPT Image 2 API docs](https://docs.poyo.ai/api-manual/image-series/gpt-image-2) <br>
- [PoYo API key page](https://poyo.ai/dashboard/api-key) <br>
- [PoYo GPT Image 2 OpenAPI JSON](https://docs.poyo.ai/api-manual/image-series/gpt-image-2.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON payload examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May submit requests to PoYo when POYO_API_KEY is available; submitted requests return a task_id for callback handling or status polling.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
