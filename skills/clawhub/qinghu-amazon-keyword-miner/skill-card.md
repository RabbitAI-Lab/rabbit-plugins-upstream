## Description:

围绕种子词挖掘亚马逊关键词，并评估搜索量、购买表现、竞争程度、PPC 竞价、点击集中度和 SPR。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

亚马逊卖家和运营人员使用此技能拓展种子词，筛选具有潜力的长尾关键词，并结合搜索、购买和竞争指标制定选词策略。

### Deployment Geography for Use:

Global (supported Amazon marketplaces)

## Known Risks and Mitigations:

Risk: Automatic installation or upgrade of unpinned Node and qhkit packages can persistently change the host environment.

Mitigation: Review installation steps first; prefer a preinstalled, pinned qhkit version and avoid installing or upgrading on shared or sensitive machines without approval.

Risk: Saving an API token with qhkit config can expose a persistent credential.

Mitigation: Use an ephemeral QHKIT_TOKEN instead of storing the token with qhkit config set.

Risk: Keyword queries may incur usage-based charges that increase with returned results.

Mitigation: Confirm the Amazon scope and estimated credit use with the user before paid calls, especially large batches.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-keyword-miner)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API key management](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Concise text or Markdown findings; spreadsheet file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports marketplace, period, sample size and credits consumed when applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
