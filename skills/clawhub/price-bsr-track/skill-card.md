## Description:

Summarizes deterministic changes in saved Amazon product snapshot prices and primary BSR fields, including the sampling time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and marketplace operators use this skill to review price and BSR changes from previously saved product snapshots. It is for deterministic watch digests and watch management, not real-time pricing, sales prediction, inventory operations, advertising, ordering, or automatic repricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package is marketed for price and BSR watch digests, while evidence.security reports broader authenticated CLI capabilities including paid analysis, export, and account-state changes.

Mitigation: Use a watch-scoped ARI API key or a dedicated watch-only build, and review available commands before installation or execution.

Risk: A custom ARI server configuration could expose authenticated requests if set unintentionally.

Mitigation: Keep ARI_BASE_URL and ARI_ALLOW_CUSTOM_BASE unset unless the custom ARI server is intentional and trusted.

Risk: Autoconfirm can allow paid analysis or collection workflows to proceed with less explicit review.

Mitigation: Disable autoconfirm or closely review it before using workflows outside watch digest and watch management.

## Reference(s):

- [Amazon 价格与 BSR 变化追踪 专用监控参考](references/reference.md)
- [Amazon 价格与 BSR 变化追踪 专用监控工作流](references/watch-workflow.md)
- [ARI service](https://ari.funewa.com)
- [ClawHub skill page](https://clawhub.ai/funewa/skills/price-bsr-track)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and summarized watch digest results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and uses the watch/price_bsr workflow with the watch_digest output template.]

## Skill Version(s):

1.4.7 (source: SKILL.md frontmatter, _meta.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
