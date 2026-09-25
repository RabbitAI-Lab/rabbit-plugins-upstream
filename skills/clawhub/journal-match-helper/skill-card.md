## Description:

投稿选刊助手，按同类已发表工作的实际去向推荐期刊，并给出样本依据与开放获取信息，供科研人员投稿前参考。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers and authors use this skill to choose candidate journals for a manuscript title or abstract by comparing where similar published work appeared. It returns journal candidates, sample evidence, recent activity, citation totals, ISSN, publisher, and open-access or DOAJ status for submission planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paper titles or abstracts sent to the skill may be sensitive and are queried against a third-party service.

Mitigation: Review manuscript sensitivity before use and avoid submitting confidential or restricted text unless the service is approved for that content.

Risk: The skill may store an API key, cookies, and an install identifier under ~/.odf for future runs and quota or payment handling.

Mitigation: Inspect and manage the local credential file according to the user's security policy, and remove stored credentials when they are no longer needed.

Risk: Journal recommendations are based on similar published work and do not represent acceptance likelihood, impact factor, or official journal guidance.

Mitigation: Use the output as planning evidence only, then verify scope, indexing, fees, and submission requirements with the journal's official sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/journal-match-helper)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown-style text with a journal table, sample evidence, status messages, and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries a third-party journal-matching service and may persist API key, cookies, and an install identifier under ~/.odf.]

## Skill Version(s):

1.0.6 (source: server release evidence, frontmatter, and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
