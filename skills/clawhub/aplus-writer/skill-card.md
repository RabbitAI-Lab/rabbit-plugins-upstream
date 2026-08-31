## Description:

Plans Amazon A+ content modules, information hierarchy, and buyer-question responses from Amazon product details and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and operators use this skill to turn product details and review evidence into A+ content plans, listing recommendations, and review-backed operational next steps. It is not intended for ad buying, image creation, or automatic Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises narrow A+ content planning while bundling broader review intelligence, paid analysis, monitoring, exports, and account-state changes.

Mitigation: Install only when the broader ARI review-operations integration is acceptable, and review requested actions before enabling paid or state-changing workflows.

Risk: The skill requires an ARI API key and can initiate paid workflows after user confirmation.

Mitigation: Keep the API key in environment or user-local configuration, avoid exposing it in prompts or reports, and verify quoted costs before confirmation.

Risk: Exports, schedules, competitors, watches, and workbench status changes can save data locally or alter account state.

Mitigation: Limit use to intended accounts and review export, schedule, competitor, watch, and workbench actions before execution.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/aplus-writer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and service links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses quote-and-confirm flows before paid operations.]

## Skill Version(s):

1.4.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
