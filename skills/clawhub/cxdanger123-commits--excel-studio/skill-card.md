## Description:

从零生成或美化已有 Excel 工作簿，自动统一主题配色、列宽、数字格式、冻结筛选与打印设置，交付前自动质检。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cxdanger123-commits](https://clawhub.ai/user/cxdanger123-commits)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和业务人员可用此技能创建新工作簿，或统一已有工作簿的版式、格式和打印设置，并在交付前检查常见质量问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A helper script may run attacker-controlled Python if its path can be influenced.

Mitigation: Before installing, verify the helper resolves to trusted package content and review its execution scope.

Risk: The security scan was partial because referenced paths were missing, so its evidence is incomplete.

Mitigation: Check that referenced files are present and review the complete package before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cxdanger123-commits/skills/excel-studio)
- [美化改造手册](references/beautify_playbook.md)
- [设计系统](references/design_system.md)
- [版式模式](references/layout_patterns.md)
- [openpyxl 注意事项](references/openpyxl_gotchas.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Excel workbooks (.xlsx), with optional JSON quality and risk reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multiple worksheets, formulas, formatting, print settings, and quality notes.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
