## Description: <br>
Guides agents to use Pruna's p-image-ideogram model for controlled photo generation, including photoreal results, readable in-image text, and structured JSON prompts with hex colors and bounding boxes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to craft, review, and execute Pruna Ideogram image-generation requests for controlled photoreal images, readable on-image text, and structured layouts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Pruna API key to make paid external image-generation requests. <br>
Mitigation: Review the generated prompt, API settings, and approval step before each request, especially for exact on-image text or brand assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-ideogram) <br>
- [P-Image-Ideogram API documentation](https://docs.api.pruna.ai/guides/models/p-image-ideogram) <br>
- [Domain configurations](references/domain-configurations.md) <br>
- [Ideogram JSON prompting](references/ideogram-json-prompting.md) <br>
- [Ideogram 4.0 JSON Prompting](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Pruna API request parameters such as prompt, thinking, image_size, aspect_ratio, and prompt_upsampling.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
