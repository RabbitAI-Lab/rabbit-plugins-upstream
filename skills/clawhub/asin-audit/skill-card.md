## Description:

Amazon ASIN 运营体检综合商品详情与评论证据，输出问题、证据和运营优先级。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to audit one ASIN at a time, combining product-detail and review evidence into prioritized operational actions. It is not intended for advertising bid management, inventory planning, profit accounting, order accounting, or unsupported real-time marketplace metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can read or export review and report data.

Mitigation: Install only when the user is comfortable granting ARI access; keep API keys out of reports, screenshots, and command examples.

Risk: Some commands can spend credits or change monitoring, competitor bindings, alert state, and workbench statuses.

Mitigation: Require fresh explicit user confirmation before paid, monitoring, export, or account-state actions.

Risk: The skill exposes broader account management, monitoring, export, and state-changing commands than its narrow ASIN audit description suggests.

Mitigation: Use the fixed audit/full workflow for normal ASIN audits and review broader commands before installation or execution.

Risk: Custom ARI base URLs could redirect API-key-bearing requests if misconfigured.

Mitigation: Keep ARI_BASE_URL unset unless intentionally using a trusted self-hosted environment, and require ARI_ALLOW_CUSTOM_BASE=1 for any custom base URL.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/asin-audit)
- [README](artifact/README.md)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Amazon ASIN operations workflow](artifact/references/operation-workflow.md)
- [使用说明](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with CLI command references and structured operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report URLs, ASIN/site identifiers, sample counts, reporting windows, credit usage, and account balance when returned by the ARI service.]

## Skill Version(s):

1.4.3 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
