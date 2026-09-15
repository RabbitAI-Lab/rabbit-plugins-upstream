## Description:

拆解用户已提供或已授权竞品商品页的标题、要点、图片和评论证据，整理可借鉴结构与风险；仅用于商品页静态拆解，不证明真实热销，不用于销量、库存、广告、订单或退货率结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and agents use this skill to compare an authorized Amazon product page with competitor pages, summarize page structure and evidence, and identify reusable listing patterns while respecting limits on unsupported sales, inventory, advertising, order, and return-rate claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI can initiate paid ARI collection or analysis workflows.

Mitigation: Require a quote first, confirm the quoted cost explicitly, and run paid actions only with the documented confirmation step.

Risk: The skill stores and uses a local ARI API key.

Mitigation: Install only for users who intend to use ARI's paid remote service and are comfortable keeping an ARI API key on the local machine.

Risk: The security summary flags that the CLI can run product-operation workflows beyond the promised fixed teardown workflow.

Mitigation: Constrain agent use to the documented page_compare/teardown workflow and reject custom workflow or focus parameters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/bestseller-teardown)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [Amazon 热销商品页拆解 专属运营工作流](references/operation-workflow.md)
- [Amazon 热销商品页拆解 API 参考](references/reference.md)
- [ARI Service Endpoint](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with optional inline shell commands for setup, quoting, running, and status checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis actions.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
