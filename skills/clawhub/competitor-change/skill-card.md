## Description:

基于已授权竞品的商品快照、确定性 diff 和已有评论计数，按周或日周期摘要可观察变化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators use this skill to manage authorized Amazon competitor watches and read deterministic daily or weekly digests of observable product snapshot changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI includes paid analysis, exports, setup/configure, and account-changing operations outside the advertised watch workflow.

Mitigation: Use only the documented watch commands for this skill; treat setup/configure, paid --confirm commands, exports, and account-changing commands as separate high-impact actions requiring explicit review.

Risk: Authenticated requests could be sent to a custom ARI base URL if a user intentionally enables the override.

Mitigation: Do not set ARI_BASE_URL or ARI_ALLOW_CUSTOM_BASE unless the destination is controlled and intended; clear unexpected overrides before use.

Risk: Watch digests may be mistaken for real-time market data or business-ground-truth metrics.

Mitigation: Limit conclusions to observable snapshot changes and existing review counts; do not present the output as sales, inventory, advertising, order, or true return-rate data.

Risk: The artifact documents planned availability and requires the current CLI to expose watch subcommands.

Mitigation: Run python scripts/ari.py watch --help before use and stop with an upgrade prompt if the watch commands are unavailable.

## Reference(s):

- [Amazon 竞品变化监控 专用监控参考](artifact/references/reference.md)
- [Amazon 竞品变化监控 专用监控工作流](artifact/references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; watch digests are documented as zero-credit deterministic summaries limited to supported daily or weekly schedules.]

## Skill Version(s):

1.4.3 (source: server release evidence, SKILL.md frontmatter, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
