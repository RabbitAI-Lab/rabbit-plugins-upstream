## Description:

Uses Amazon review frequency, experience impact, and product information to prioritize product feature improvements with evidence; it is not for sales forecasting, budget approval, or purchasing execution and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to turn ARI-collected review data into prioritized product improvements for an ASIN. It supports quoting and confirmed execution of the fixed product/priorities workflow, with monitoring and competitor context available when relevant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI operations and scheduled monitoring can consume credits or create ongoing collection costs.

Mitigation: Review quotes, auto-confirm settings, and monitoring schedules before use; require explicit user confirmation for paid operations unless the ARI service has already applied auto-confirm.

Risk: The skill requires an ARI API key for a third-party service.

Mitigation: Use a dedicated, revocable ARI API key and avoid exposing the key in reports, examples, or shared outputs.

Risk: The security evidence says the skill can perform broader Amazon review operations than the narrow feature-priority description suggests.

Mitigation: Deploy it only when broader ARI-connected review operations are acceptable, and keep normal use scoped to the fixed product/priorities workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/feature-priority)
- [README](artifact/README.md)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and ARI report links or exported files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish direct data, inferred analysis, and recommendations; paid operations require quote and confirmation unless ARI auto-confirm applies.]

## Skill Version(s):

1.4.5 (source: server release evidence, target metadata, frontmatter, _meta.json, script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
