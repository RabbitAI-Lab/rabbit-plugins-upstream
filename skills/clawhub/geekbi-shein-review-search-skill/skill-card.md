## Description:

Searches and analyzes real SHEIN product reviews for a specific product ID, summarizing ratings, strengths, complaints, specification differences, risks, and improvement actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product researchers use this skill to query GeekBI's SHEIN review data for a known product ID and turn the returned reviews into grounded product feedback, risk, and improvement guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Login state may be shared through a Temu-named local auth namespace, which can confuse credential boundaries across GeekBI skills or accounts.

Mitigation: Review account separation before installation; use separate user or workspace configuration for different GeekBI accounts, or wait for the publisher to fix the auth namespace.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-shein-review-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shein-review-search-skill)
- [README](artifact/README.md)
- [SHEIN review search method](artifact/references/SHEIN评论搜索.md)
- [SHEIN review search interface](artifact/references/SHEIN评论搜索接口.md)
- [Query pause and resume flow](artifact/references/查询暂停与恢复流程.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with JSON command outputs used as evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state product ID, site, filters, pagination range, total-count basis, unique review count, sample limits, and confidence boundaries.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
