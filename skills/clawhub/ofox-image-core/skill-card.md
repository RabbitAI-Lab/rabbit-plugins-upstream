## Description:

Provides a shared execution layer for the Ofox image generation API that validates parameters, sends synchronous text-to-image requests, decodes image results, saves files, and reports usage and cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT

## Use Case:

Developers and scenario-skill authors use this library skill to call the Ofox image generation API with validated low-level parameters, pre-flight cost estimates, and saved image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Ofox API key could be sent to an unintended endpoint if OFOX_API_BASE_URL is set to a replacement service.

Mitigation: Use a least-privileged Ofox API key, keep OFOX_API_BASE_URL unset unless the endpoint is intentionally trusted, and inspect any dotenv file before sourcing it.

Risk: Advanced JSON overrides can change request fields after normal parameter validation and approval.

Mitigation: Avoid allowing untrusted callers or scenario skills to pass --extra-json values that override core request fields.

Risk: Image generation is a paid API call and estimates can vary by model, quality, and size.

Mitigation: Run the skill in dry-run mode and obtain approval for the displayed cost before submitting a generation request.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ofoxai/skills/ofox-image-core)
- [Publisher Profile](https://clawhub.ai/user/ofoxai)
- [Skill Homepage](https://github.com/ofoxai/skills/tree/main/skills/ofox-image-core)
- [API Parameters](references/api-params.md)
- [Pricing Reference](references/pricing.md)
- [Model Snapshot](references/models-snapshot.json)
- [Token Anchors](references/token-anchors.json)
- [Execution Script](references/ofox-image.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, and jq for live generation; dry runs can estimate cost before submitting a paid request.]

## Skill Version(s):

1.10.3 (source: frontmatter, metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
