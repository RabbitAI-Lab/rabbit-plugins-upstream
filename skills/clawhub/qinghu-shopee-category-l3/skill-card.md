## Description:

按站点、语言和二级类目 ID 查询 Shopee 三级类目的 ID 与名称。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts use this skill to find the leaf categories under a specified second-level category for a chosen site and language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Category lookups can incur Qinghu API charges.

Mitigation: Show the estimated cost and obtain the user's consent before making paid calls.

Risk: Automatic installation or upgrades can change the local Node and qhkit environment.

Mitigation: Preinstall and review a pinned qhkit version rather than allowing automatic setup or upgrades.

Risk: Persisted service credentials may expose access to the Qinghu account.

Mitigation: Provide credentials through a scoped environment variable instead of storing tokens automatically.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-category-l3)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise category results in text or Markdown; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes category IDs and names; reports credits used for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
