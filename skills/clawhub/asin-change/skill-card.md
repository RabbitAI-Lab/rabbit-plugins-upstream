## Description:

Monitors saved Amazon product snapshots on supported daily or weekly schedules and returns a deterministic change digest for a single ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators and Amazon sellers use this skill to manage configured ASIN watches and review concise summaries of product-field changes from saved snapshots. It is intended for deterministic watch digests, not real-time price, sales, inventory, advertising, order, or true return-rate monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is presented as a narrow no-paid-LLM ASIN watch monitor, but evidence.security says it ships an authenticated general-purpose ARI CLI with paid analysis, exports, account mutation, and server-side auto-confirmed billing paths.

Mitigation: Review before installing, keep auto-confirm off unless intentionally enabled, and limit use to the documented watch commands unless the broader CLI effects have been reviewed.

Risk: The skill requires an ARI API key, so running broader CLI commands can affect account data or billing.

Mitigation: Grant the key only in an environment where the user accepts those permissions, and require explicit confirmation before invoking paid analysis, export, account, or workflow-changing commands.

Risk: The watch workflow is marked planned and depends on the local CLI exposing the watch subcommands.

Mitigation: Run the watch help check before use and stop with an upgrade message if the watch commands are unavailable.

## Reference(s):

- [Amazon ASIN 变化监控 专用监控参考](references/reference.md)
- [Amazon ASIN 变化监控 专用监控工作流](references/watch-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-change)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and deterministic watch digest data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Watch digests are described as zero-credit deterministic summaries; paid AI weekly reports and non-watch operations are outside this skill's intended workflow.]

## Skill Version(s):

1.4.7 (source: SKILL.md frontmatter, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
