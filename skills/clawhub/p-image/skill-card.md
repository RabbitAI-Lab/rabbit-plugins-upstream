## Description:

Use when someone explicitly wants the fastest, cheapest photo generation, such as mood boards, bulk panels, or quick iterations, and not when controlled photorealism or in-image text is needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route simple, quick photo-generation requests through Pruna's p-image model, draft faithful prompts, choose aspect ratios, and issue Pruna API calls after confirming required inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install multiple external skills with auto-confirmation, and those dependencies may be unreviewed or unpinned.

Mitigation: Review external skills before installation, prefer pinned versions or verified commits, and avoid auto-confirmed installs in environments with sensitive credentials.

Risk: Photo-generation requests send prompts and reference details to Pruna's API.

Mitigation: Use a dedicated Pruna API key and send only prompts or reference details that are appropriate to share with Pruna.

## Reference(s):

- [p-image ClawHub listing](https://clawhub.ai/pruna-ai/skills/p-image)
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Pruna API key and a user prompt; optional fields include aspect ratio, seed, LoRA settings, Hugging Face API token, and safety checker control.]

## Skill Version(s):

1.0.12 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
