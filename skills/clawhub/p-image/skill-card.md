## Description:

Use when someone explicitly wants the fastest, cheapest photo generation -- mood boards, bulk panels, or quick iterations -- not when controlled photoreal or in-image text is needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to route simple photo-generation requests to Pruna's hosted p-image model, draft faithful prompts, choose aspect ratios, and produce API calls for image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts are sent to Pruna's hosted API using PRUNA_API_KEY.

Mitigation: Avoid including secrets, private documents, or sensitive personal data in prompts, and install only if sending prompts to Pruna is acceptable.

Risk: The optional full-suite install may add additional Pruna-related skills.

Mitigation: Review the optional full-suite install before running it and install only the needed skills when minimizing scope matters.

## Reference(s):

- [p-image on ClawHub](https://clawhub.ai/pruna-ai/skills/p-image)
- [Pruna Predictions API](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with bash/curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY and sends prompts to Pruna's hosted API.]

## Skill Version(s):

1.0.11 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
