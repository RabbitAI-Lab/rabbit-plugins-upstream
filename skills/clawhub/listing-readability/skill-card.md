## Description:

检查 Amazon Listing 的结构、术语、重复表达和评论反映的理解障碍，给出可读性建议；仅用于页面可读性诊断，并需要 ARI API key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce operators use this skill to review product listing readability, buyer comprehension barriers, terminology, repeated wording, and review-derived listing improvement opportunities. It is intended for listing readability diagnosis, not ad bidding, legal certification, translation certification, or automatic Amazon page publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the package is presented as a narrow readability checker while exposing broader paid analysis, monitoring, export, competitor, advertising-keyword, and account-setting workflows.

Mitigation: Review it as a broad ARI Amazon review and product-operations client before installation, and enable only workflows the user explicitly asks to use.

Risk: The skill requires an ARI API key and can read or export collected review and report data.

Mitigation: Grant an ARI API key only in an environment where that access is acceptable, avoid placing keys in reports or examples, and confirm export requests before producing files or links.

Risk: Some workflows may consume paid credits or change monitoring and account settings.

Mitigation: Use the quoted cost and request identifiers returned by the service, require explicit user confirmation for paid or state-changing actions, and check status before retrying interrupted paid operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/listing-readability)
- [Operation Workflow Reference](artifact/references/operation-workflow.md)
- [ARI API Reference](artifact/references/reference.md)
- [ARI Products](https://ari.funewa.com/zh/products)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report URLs, cost quotations, account or credit status, review summaries, exported report guidance, and user-confirmed monitoring or analysis steps.]

## Skill Version(s):

1.4.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
