## Description:

安装出概算与物资计划；不出金额、不替代结算。触发词：安装算量、桥架、喷淋。

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Developers and engineering teams use this skill to prepare installation rough-quantity takeoffs and material-plan drafts from CAD scan data, then review the assumptions and flagged items before relying on the results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a mismatch between the stated estimating purpose and some behavior, automatic dependency installation, and other scope concerns.

Mitigation: Review the skill and its setup behavior before installation, and confirm its requested capabilities and dependency setup fit your needs.

Risk: ClawScan could not match one referenced path-like item to bundled content, so its coverage is incomplete.

Mitigation: Check referenced files against the full release contents and review the scan coverage before relying on it.

Risk: Quantity and material-plan outputs are drafts and can contain estimated or unresolved items.

Mitigation: Review flagged quantities against source drawings and applicable project requirements before using them for planning.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Base contract and workflow boundaries](references/base-contract.md)
- [Quantity rules and standards mapping](references/standard_rules.json)
- [Loss and reserve rules](references/loss_rules.json)
- [Skill bus integration](docs/bus-integration.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON, CSV, XLSX spreadsheets]

**Output Format:** [XLSX workbooks and Markdown, JSON, or CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities and material plans include assumptions and review flags; they do not provide pricing or settlement quantities.]

## Skill Version(s):

0.4.35 (source: frontmatter, changelog, released 2026-11-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
