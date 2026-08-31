## Description:

Combines Amazon product-detail and review evidence to diagnose buyer decision barriers and recommend page conversion copy improvements; it is not intended for conversion-rate prediction, advertising, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and operators use this skill to turn Amazon product details and review samples into evidence-based listing copy, VOC, competitive, monitoring, and operations recommendations. The skill is scoped to listing/conversion output and requires explicit confirmation before paid analysis or persistent account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can make authenticated API calls, including export operations.

Mitigation: Configure the key only through the documented local setup or environment variable path, do not include the key in reports or examples, and use the official ARI base URL unless a custom endpoint is intentionally enabled.

Risk: Paid analysis, collection, leaderboard, and advice operations can spend ARI credits.

Mitigation: Require the agent to quote costs first and execute paid commands only after explicit user confirmation using the same quoted request or command.

Risk: Monitoring, watch, competitor, and workflow-state commands can change persistent account state.

Mitigation: Confirm the exact ASIN, watch ID, schedule, competitor, or workflow state before changes, and prefer read-only status or list commands when intent is unclear.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Dedicated Operations Workflow](references/operation-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/conversion-copy)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and recommendations with inline shell commands and JSON-style CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, report IDs, credit usage, sample windows, and saved export paths when returned by the service.]

## Skill Version(s):

1.4.3 (source: server release evidence, skill frontmatter, _meta.json, and ari.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
