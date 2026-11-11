## Description:

Openrouter Models Pricing fetches and analyzes the OpenRouter model catalog for pricing, context length, modalities, provider families, and free or specialized model comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzfly256](https://clawhub.ai/user/zzfly256)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to compare OpenRouter models by price, context length, provider family, input and output modalities, cache pricing, reasoning pricing, and free availability. It is for OpenRouter catalog analysis and does not perform model generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplying OPENROUTER_API_KEY when fetching the public catalog can identify or attribute the request to the user's OpenRouter account.

Mitigation: Unset OPENROUTER_API_KEY or omit --api-key when an anonymous public catalog request is preferred.

Risk: The cached catalog includes descriptions of router and web-enabled models whose privacy implications may differ if users invoke those models separately.

Mitigation: Use this skill for catalog analysis only and review individual OpenRouter model and provider terms before sending prompts to a model.

## Reference(s):

- [OpenRouter Model Catalog API](https://openrouter.ai/api/v1/models)
- [Major OpenRouter model families](references/model_families.md)
- [OpenRouter pricing field reference](references/pricing_fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands, aligned text tables, JSON output, and coverage statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a cached OpenRouter model catalog; rerun fetch_models.py to refresh pricing and capability data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
