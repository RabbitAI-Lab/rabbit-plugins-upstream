## Description:

从 Amazon 评论中的重复疑问和商品字段中提炼商品页 FAQ 主题与回答证据，仅用于 FAQ 主题建议，并需要 ARI API key（ari_live_*）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to turn collected Amazon reviews and product fields into FAQ topic suggestions and evidence-backed draft answers for product pages. It is not intended for buyer support automation, legal or policy conclusions, or automatic Amazon page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broader paid ARI review-analysis operations than its FAQ-focused name suggests, and some workflows may spend credits or change account behavior.

Mitigation: Install only when ARI account access is intended; use quote-only requests for estimates, set autoconfirm off when every charge should be approved, and avoid broader monitoring, export, workbench, advise, or leaderboard workflows unless deliberately requested.

Risk: The skill stores and uses a local ARI API key.

Mitigation: Use browser authorization or the ARI_API_KEY environment variable as documented, do not paste keys into chat or reports, and revoke or recreate keys from the ARI user center if access should end.

Risk: FAQ suggestions can be misleading when the collected review sample, time window, or variant coverage is limited.

Mitigation: Review the stated data range, sample size, and review evidence before using suggestions, and treat small samples or unclear variant coverage as directional rather than definitive.

Risk: Outputs could be misused as automatic customer replies, legal conclusions, or direct product-page updates.

Mitigation: Use the output as proposal material only and require human review before customer-facing replies, compliance decisions, or Amazon listing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/faq-generator)
- [README](artifact/README.md)
- [User Guide](artifact/使用说明.md)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports and concise text responses, with JSON or shell-command snippets when troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ASIN and site, sample size, review evidence, report links, credit usage, and account or authorization status when available.]

## Skill Version(s):

1.4.8 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
