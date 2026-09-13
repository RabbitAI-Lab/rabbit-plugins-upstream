## Description:

Use when photo generation needs more control - photoreal results, text in the image, or structured JSON with hex colors and bounding boxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to route complex still-image generation requests to Pruna's P-Image-Ideogram model, especially when prompts need photorealism, readable in-image text, exact colors, or structured JSON layout control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned remote skill install commands can retrieve unexpected dependency versions.

Mitigation: Review the documented npx install commands and prefer pinned commits or verified releases before installation.

Risk: Prompts and image-generation requests are sent to Pruna's API using PRUNA_API_KEY.

Mitigation: Use the skill only when the prompt content can be shared with Pruna, and keep PRUNA_API_KEY protected.

Risk: Premium image-generation settings can increase usage cost.

Mitigation: Confirm high-cost settings such as very high thinking or 2K output before making API calls unless the user already requested maximum quality.

## Reference(s):

- [P-Image-Ideogram API documentation](https://docs.api.pruna.ai/guides/models/p-image-ideogram)
- [Ideogram JSON Prompting](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0)
- [domain-configurations.md](references/domain-configurations.md)
- [ideogram-json-prompting.md](references/ideogram-json-prompting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with curl commands, API parameter settings, and optional JSON prompt structures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May prepare Pruna P-Image-Ideogram API requests and prompt configurations that require PRUNA_API_KEY.]

## Skill Version(s):

1.0.12 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
