## Description:

按企业名称交叉核验浙江省科技型中小企业名录收录情况与工程中标记录，并给出四类结论和建议动作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售、招投标和供应商尽调人员可用它按企业名称查询浙江供应商的资质名录命中情况和工程中标业绩，辅助入围筛选、投标对手摸底和公开记录复核。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried company names are sent to the skill's HTTPS service, and the skill stores a product-specific credential/session file in the user's home directory.

Mitigation: Avoid confidential supplier research unless the user trusts the service operator, and review the local credential/session file expectations before installation.

Risk: Roster data covers collected batches and contract-award data covers a historical interval, so a missed result may not prove the supplier lacks the qualification or award history.

Mitigation: Treat results as public-record screening support and verify important decisions with the supplier's unified social credit code and authoritative sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-supplier-profile)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text response from a Node.js command-line script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns public-record summary text, including qualification evidence, contract-award evidence, amount ranges, conclusion category, and suggested next actions.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
