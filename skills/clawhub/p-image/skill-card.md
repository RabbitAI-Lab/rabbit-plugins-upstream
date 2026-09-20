## Description:

Use when someone explicitly wants fast, low-cost photo generation for mood boards, bulk panels, or quick iterations, rather than controlled photoreal output or in-image text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to route simple photo-generation requests to Pruna's p-image model, craft faithful prompts, choose aspect ratios, and call the Pruna API for quick still-image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, private images, or sensitive tokens may be sent to Pruna's API.

Mitigation: Do not submit confidential prompts, private images, or sensitive tokens unless the user accepts sharing them with Pruna's API.

Risk: Installer commands load Pruna skills from an external source.

Mitigation: Confirm the Pruna skill source is trusted and prefer pinned or otherwise verified installer commands before installation.

## Reference(s):

- [ClawHub p-image skill page](https://clawhub.ai/pruna-ai/skills/p-image)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and sends prompt and aspect-ratio inputs to Pruna's API.]

## Skill Version(s):

1.0.13 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
