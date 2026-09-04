## Description:

Summarizes deterministic price and main BSR changes from saved Amazon product snapshots and shows the sampling time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon product operators and developers use this skill to manage saved product watches and generate deterministic price and BSR digests from stored snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release presents a narrow price and BSR tracker but includes a broader ARI CLI with paid analysis, collection, export, account, and monitoring controls.

Mitigation: Review available commands before use, install only when the broader ARI CLI is intended, and run only explicit user-requested watch actions.

Risk: API keys and account state may be exposed or changed through custom endpoints, watch schedules, autoconfirm behavior, exports, or credit-spending commands.

Mitigation: Keep ARI_API_KEY scoped to this service, avoid ARI_ALLOW_CUSTOM_BASE unless the endpoint is controlled, and confirm costs or state changes before executing management or paid commands.

## Reference(s):

- [Amazon 价格与 BSR 变化追踪 专用监控参考](artifact/references/reference.md)
- [Amazon 价格与 BSR 变化追踪 专用监控工作流](artifact/references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and deterministic watch digest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; digest output is described as zero-credit, while watch creation and schedule changes can alter persistent monitoring state.]

## Skill Version(s):

1.4.5 (source: server evidence release, SKILL.md frontmatter, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
