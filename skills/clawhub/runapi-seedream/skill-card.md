## Description:

Generate and edit images with Seedream through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with Seedream through RunAPI, using CLI guidance for one-off tasks and SDK guidance for application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source image URLs may be sent to RunAPI's Seedream service.

Mitigation: Confirm RunAPI provider use is acceptable before installation and avoid sending sensitive prompts or private source image URLs unless the workflow permits it.

Risk: Interactive browser login may not fit headless agent workflows and can place credentials in CLI configuration.

Mitigation: Prefer RUNAPI_API_KEY or explicit CLI token import for headless runs; use browser login only when it matches the user's workflow.

Risk: Generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download generated outputs and store them in durable storage within the documented retention window.

## Reference(s):

- [RunAPI Seedream homepage](https://runapi.ai/models/seedream)
- [RunAPI Seedream model documentation](https://runapi.ai/models/seedream.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI ByteDance provider documentation](https://runapi.ai/providers/bytedance.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell, JSON, and SDK package references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents toward CLI use for one-off tasks and SDK use for application integrations.]

## Skill Version(s):

0.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
