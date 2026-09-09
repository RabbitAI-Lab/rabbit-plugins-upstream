## Description:

Combines Amazon product details and review evidence to diagnose bullet-point selling points, buyer questions, and copy gaps; it is limited to bullet-point diagnosis and suggestions and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operations teams use this skill to turn ARI-collected product details and review evidence into bullet-point optimization suggestions. It helps identify selling points, buyer concerns, and copy gaps while keeping paid collection and operations runs behind pricing and confirmation flows.

### Deployment Geography for Use:

Global, for supported Amazon marketplaces.

## Known Risks and Mitigations:

Risk: The security evidence flags a broader ARI platform surface than the narrow bullet-point description, including account, monitoring, paid analysis, export, and persistent-setting capabilities.

Mitigation: Install only when the broader ARI operations platform is intended, and review API-key storage, credit auto-confirm rules, monitoring and schedule behavior, competitor/watch changes, and export destinations before authorizing.

Risk: Paid collection, analysis, operations, and some auto-confirm flows can spend account credits.

Mitigation: Use quote-only paths when the user asks only for pricing, require the documented confirmation or requestId flow before paid operations, and set auto-confirm off or to an explicit limit when predictable approval is needed.

Risk: API-key handling and custom endpoint settings can expose credentials if misconfigured.

Mitigation: Use browser setup or ARI_API_KEY without pasting keys into chat, and clear unexpected ARI_BASE_URL values unless the user intentionally pairs them with ARI_ALLOW_CUSTOM_BASE=1 for a trusted environment.

Risk: Monitoring, competitor/watch changes, and exports can create persistent account effects or local files beyond a single bullet-point recommendation.

Mitigation: Confirm the exact ASIN, watch identifier, schedule, cost, and export destination before making those changes, and pause or delete monitoring when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/bullet-writer)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [Dedicated Operations Workflow](artifact/references/operation-workflow.md)
- [Usage Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and CLI JSON responses, with inline shell commands when setup or advanced operation is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid actions may require quote and confirmation, and some account auto-confirm settings can allow small paid operations to run immediately.]

## Skill Version(s):

1.4.8 (source: server release evidence, frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
