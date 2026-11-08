## Description:

装饰算量：按房间类型、建筑/结构图、装修表、做法表和节点详图出装饰概算与物资计划；可导入 cad-file-reader 测量候选作待核对输入。做法映射、洞口扣减、损耗、材料台账和清单量仍由本技能算。

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

建筑装饰造价人员和项目团队可用它按房间或明细部位生成装饰概算、物资计划及待核对项。结果用于计划和复核；正式清单、结算、报价及项目规则仍需以合同、设计文件和现行规范为准。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence rates the release suspicious with medium confidence: setup may download, install, and run a separate CAD tool, and the documented skip route may still run setup.

Mitigation: Before installation, review setup and the skip route; proceed only if the download, code execution, and persistent file writes are acceptable.

Risk: The security scan was partial because one referenced path was missing, so that reference was not covered.

Mitigation: Review the missing referenced content before installation.

## Reference(s):

- [ClawHub release](https://clawhub.ai/lisong2003-lgtm/skills/zhuangshi-suanliang)
- [Base contract and CAD measurement boundary](references/base-contract.md)
- [Waterproofing standards references](references/waterproof-standards.md)
- [Skill bus integration](docs/bus-integration.md)

## Skill Output:

**Output Type(s):** [Files, CSV, Markdown, Guidance]

**Output Format:** [XLSX workbook, CSV tables, and a Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes calculation bases, estimates, material quantities, references, and items requiring confirmation; project review is required.]

## Skill Version(s):

0.9.32 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
