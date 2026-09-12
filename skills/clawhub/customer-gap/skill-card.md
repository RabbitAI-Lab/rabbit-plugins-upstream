## Description:

Amazon 消费者预期差距 helps an agent compare Amazon product-page promises with customer review evidence to identify expectation gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and analysts use this skill to audit whether listing promises match real customer review experience. The agent can check product readiness, quote paid ARI operations, generate promise-audit reports, and summarize evidence-backed gaps, trends, and next actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI actions can spend credits, including cases where account auto-confirm rules allow immediate execution.

Mitigation: Use quote and status flows before paid work, preserve explicit user confirmation boundaries, and disable or lower auto-confirm when the user wants approval before each paid action.

Risk: The skill requires an ARI API key and can export review or report data to local files.

Mitigation: Keep API keys out of chat and generated reports, prefer browser authorization or environment variables, and review exported files before sharing them.

Risk: Monitoring and product workflow commands can change account-side product state.

Mitigation: Run read-only checks first, explain costs and target ASIN or watch IDs, and require clear user intent before creating, pausing, resuming, deleting, or running paid workflows.

## Reference(s):

- [ARI CLI and API Reference](references/reference.md)
- [Dedicated Operations Workflow](references/operation-workflow.md)
- [Usage Guide](使用说明.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/customer-gap)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with optional JSON snippets, local file exports, and inline shell commands for advanced use]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report URLs, report IDs, credit usage, data ranges, review evidence, CSV/Markdown/HTML export paths, and confirmation guidance for paid actions.]

## Skill Version(s):

1.4.8 (source: frontmatter, _meta.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
