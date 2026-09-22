## Description:

投稿选刊助手按同类已发表工作的实际去向推荐期刊，并给出样本依据与开放获取信息，供科研人员投稿前参考。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and paper authors use this skill to compare a manuscript title or abstract against similar published work and identify journals that have recently published related papers. It provides candidate journals, sample matching publications, citation totals, ISSN, publisher, open-access status, and DOAJ status for submission planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manuscript titles or abstracts are sent to a hosted service at runtime.

Mitigation: Use the skill only for content you are comfortable sharing with that service, and avoid sending confidential manuscript details unless the user has approved that disclosure.

Risk: The skill stores service credentials and cookies under the user's home directory.

Mitigation: Review and manage the local credential file before and after use, especially on shared systems or when changing accounts.

Risk: The skill can present subscription or payment prompts when free quota is exhausted.

Mitigation: Do not let an agent initiate payment or subscription actions unless the user explicitly requested that action and trusts the provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/journal-match-helper)
- [Hosted journal matching service](https://110.40.221.75:13479/factory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown-style text with a candidate journal table, sample evidence, and status messages from a Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The runtime output is derived from a hosted service response and may include subscription, credential, or network status messages.]

## Skill Version(s):

1.0.4 (source: frontmatter, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
