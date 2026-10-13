## Description:

按关键词批量查询 Shopee 热搜词的销量、销售额、搜索指数和类目信息，每次最多查询 10 个关键词。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use the skill to compare keyword demand, sales, revenue and categories for a selected site and reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Host software installation or upgrade may run broad, unpinned commands before the lookup.

Mitigation: Preinstall a reviewed, pinned qhkit version and avoid automatic changes to shell startup files.

Risk: A lookup needs an API token and may incur paid credits.

Mitigation: Configure the token securely and confirm the estimated charge with the user before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-keyword-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise findings with supporting figures; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify the Shopee site and reporting period; queries accept up to 10 keywords.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
