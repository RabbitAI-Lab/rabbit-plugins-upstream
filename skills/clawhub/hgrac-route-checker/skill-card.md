## Description:

hgrac-route-checker is a zero-dependency decision-support CLI that classifies human genetic resource compliance routes under TH-BIO-001 rules and returns JSON IR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance reviewers, and life sciences teams use this skill to run a narrow CLI check for human genetic resource collection, storage, use, transfer, or international cooperation routing. Results are decision support only and should be verified against current official regulations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the CLI result for legal or regulatory approval.

Mitigation: Treat outputs as decision support only and verify them with current official regulations or qualified counsel before acting.

Risk: Regulatory source text may change after the skill release.

Mitigation: Check the cited human genetic resource regulation and implementation-rule articles before relying on a route determination.

Risk: The interface and detailed documentation are primarily in Chinese.

Mitigation: Use reviewers who can understand the Chinese inputs, outputs, and source-rule labels when assessing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/hgrac-route-checker)
- [LGD theory ledger](https://medxpert.cn/theory)
- [LGD-Powered badge](https://medxpert.cn/badge/powered/svg/lgd-powered-cn.svg)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON IR from a command-line interface, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rc status codes, warnings, evidence clause labels, and AIGC metadata; no external dependencies are required.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
