## Description:

从安装工程 DWG 或扫描索引生成概算清单底稿与物资计划草稿，供出量、备料、图纸复核和专业软件交叉核对。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

安装工程师和施工预算人员可从 DWG 图纸或已有扫描索引整理管线、设备及材料数量，用于概算底稿、物资计划和图纸复核；结果需人工核验，不用于结算或计价。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may execute helper programs that have not been independently verified.

Mitigation: Review and verify helper programs before running setup.

Risk: The documented SKILL_NO_BASE=1 opt-out does not prevent installed runtime execution during setup.

Mitigation: Do not rely on SKILL_NO_BASE=1 as an execution safeguard; review setup behavior before installing or running it.

Risk: Optional synchronization can use an untrusted bus client, and shared results may be stale or incomplete.

Mitigation: Select a trusted bus client explicitly or leave synchronization unused; check shared-result freshness and review all quantities before relying on the drafts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Publisher profile](https://clawhub.ai/user/lisong2003-lgtm)
- [Quantity and loss rules](artifact/references/loss_rules.json)
- [Standard rules](artifact/references/standard_rules.json)
- [Dual-caliber mapping rules](artifact/references/dual_caliber_rules.json)

## Skill Output:

**Output Type(s):** [Spreadsheet, JSON, Shell commands]

**Output Format:** [XLSX workbooks and JSON scan or plan files; command-line scripts are provided for scanning and planning.]

**Output Parameters:** [Installation DWG drawings or existing scan JSON indexes, plus optional system and trunk scans.]

**Other Properties Related to Output:** [Draft quantities for estimating and material planning; no prices or settlement quantities. Review flagged, inferred, duplicate, and unmatched items before use.]

## Skill Version(s):

0.4.22 (source: server-resolved release metadata and artifact CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
