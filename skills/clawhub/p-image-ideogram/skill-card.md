## Description:

Use when photo generation needs more control: photoreal results, text in the image, or structured JSON with hex colors and bounding boxes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and agents use this skill to prepare controlled Pruna image-generation requests for photoreal outputs, in-image typography, and structured Ideogram-style JSON layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to Pruna's hosted API for image generation.

Mitigation: Use the skill only when Pruna-hosted processing is acceptable for the prompt content and account data-handling expectations.

Risk: Prompts may contain secrets, private personal data, or confidential business material.

Mitigation: Do not include sensitive material in prompts unless that disclosure is approved for the user's Pruna account and workflow.

Risk: PRUNA_API_KEY is required for authenticated API calls.

Mitigation: Treat PRUNA_API_KEY as a secret and avoid exposing it in prompts, logs, command history, or shared artifacts.

Risk: Referenced companion skills affect generation workflow and supply-chain confidence.

Mitigation: Prefer pinned or verified install flows for referenced Pruna skills before use.

Risk: Premium and paid API paths can incur cost.

Mitigation: Confirm high-cost settings such as very high thinking and 2K output before submitting paid generation requests unless the user explicitly requested maximum quality.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-ideogram)
- [P-Image-Ideogram API documentation](https://docs.api.pruna.ai/guides/models/p-image-ideogram)
- [Domain configurations](references/domain-configurations.md)
- [Ideogram JSON prompting](references/ideogram-json-prompting.md)
- [Ideogram 4.0 JSON prompting guide](https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with JSON request bodies and curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PRUNA_API_KEY for authenticated calls to Pruna's hosted image-generation API.]

## Skill Version(s):

1.0.11 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
