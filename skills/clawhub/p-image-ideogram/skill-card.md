## Description:

Use when photo generation needs more control - photoreal results, text in the image, or structured JSON with hex colors and bounding boxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to guide agents through controlled Pruna image generation when prompts need photoreal detail, readable in-image text, structured JSON captions, brand colors, or bounding-box layout control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image prompts, on-image text, and API credentials are used with Pruna services.

Mitigation: Confirm PRUNA_API_KEY handling through the companion pruna-api skill and avoid sending confidential prompt content unless that external processing is approved.

Risk: The skill can guide installation or use of companion Pruna skills.

Mitigation: Review the companion skills, especially pruna-api, before deploying the workflow.

Risk: Premium generation settings can increase API cost for complex or maximum-quality jobs.

Mitigation: Confirm with the user before using the very high thinking plus 2K premium path unless they explicitly requested top quality.

Risk: Generated images with dense text, panels, or layout constraints may require visual selection and retry.

Mitigation: Use JSON captions or locked literal strings where appropriate, run parallel seeds for text-heavy layouts, and visually inspect outputs before downstream use.

## Reference(s):

- [P-Image-Ideogram API documentation](https://docs.api.pruna.ai/guides/models/p-image-ideogram)
- [Domain configurations](references/domain-configurations.md)
- [Ideogram JSON prompting](references/ideogram-json-prompting.md)
- [Ideogram 4.0 JSON prompting guide](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0)
- [Ideogram 4.0 JSON prompting Markdown mirror](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, Guidance]

**Output Format:** [Markdown guidance with JSON prompt structures and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Pruna API request payloads and generated image-prompt specifications; actual image outputs come from the Pruna API.]

## Skill Version(s):

1.0.10 (source: server release, SKILL.md frontmatter, parsed metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
