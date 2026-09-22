## Description:

浙江工程招投标合同公示的供应商视角整理，按公司查中标项目、时间、金额与同类报价区间。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Zhejiang public works tender contract history for a supplier, including won projects, signing dates, contract amounts, and peer amount ranges. It is scoped to collected Zhejiang engineering tender records and should not be used as a company credit evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to the skill provider's HTTPS service.

Mitigation: Install and run the skill only when sending supplier or project search terms to the provider is acceptable for the user's workflow.

Risk: Subscription credentials and session cookies are stored locally in the user's home directory.

Mitigation: Protect ~/.odf/zj-tender-history.json like other API credentials and avoid sharing it in logs, support tickets, or repositories.

Risk: The dataset covers only collected public contract batches, so missing results do not prove that a supplier has no tender history.

Mitigation: Present returned coverage and boundary notes with the answer, and avoid using the output as a company credit evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-tender-history)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text returned by a Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes project names, signing dates, contract amounts, peer amount ranges, coverage notes, and explicit boundary statements when data is unavailable or out of scope.]

## Skill Version(s):

1.0.3 (source: server release evidence, skill frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
