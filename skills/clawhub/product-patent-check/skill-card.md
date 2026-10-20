## Description:

Resolves a brand’s company-name variants and searches product and component patents, organizing inventions, utility models, and designs into a component-grouped list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

面向采购、竞品分析及电商选品人员，用于查询某品牌产品的相关专利并按部件整理结果；不作侵权判断，也不保证专利对应某一具体型号。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential protection weaknesses may put API keys at risk.

Mitigation: Ask the publisher to fix credential protections before supplying a funded key, and do not paste keys into chat.

Risk: Cache containment and file-isolation weaknesses warrant review.

Mitigation: Ask the publisher to fix cache containment before supplying a funded key.

Risk: Timed-out paid requests or reliance on the client budget may result in unexpected spending.

Mitigation: Check billing before retrying timed-out paid requests; the client budget is not a guaranteed spending cap.

Risk: Queries may expose confidential invention details.

Mitigation: Keep confidential invention details out of queries.

## Reference(s):

- [ClawHub release](https://clawhub.ai/ip930/skills/product-patent-check)
- [PatentMax API reference](artifact/references/api-reference.md)
- [Patent search workflow](artifact/references/search-workflow.md)
- [Query syntax reference](artifact/references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance]

**Output Format:** [UTF-8 CSV (Excel-readable), grouped by component, with concise findings in chat.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The list includes patent identifiers, titles, types, applicants, dates, legal status, and a brief protection summary; it is not an infringement opinion and may not identify patents tied to a specific product model.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
