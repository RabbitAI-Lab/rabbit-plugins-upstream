# KLS 模板资源清单

本目录存放知识循环定位策略师的输出模板，含占位符，按需复制填充，不加载全文。

| 模板文件 | 用途 | 使用方式 |
|---------|------|---------|
| KLS-diagnosis-report-template.md | KLS1 循环诊断报告（环节定位/分档/时钟/资产/结论） | 复制后按节填充 |
| KLS-moveup-roadmap-template.md | KLS2 上移路线图（目标匹配/等价转化/路线/死路排除/退路） | 复制后按节填充 |
| KLS-verifier-checklist-template.md | KLS3 领域验证器（直觉图景/裁决点/三态清单/覆盖边界/闭环方案） | 复制后按节填充 |
| KLS-question-asset-template.md | KLS4 问题资产卡格式契约（数据文件表头由此派生） | 作为格式契约参照 |
| KLS-digestion-package-checklist-template.md | KLS5 八件套交付检查单（可裁剪项标注） | 复制后逐项核对 |

## 填充说明

1. 占位符统一为 `{{名称}}` 形式，填充后删除占位符与行内注释；
2. 表格字段顺序为契约，不得调整列序；
3. 裁决类字段必须使用三态取值：已裁决/已校验/待裁决；
4. 无法给出依据的时间估计标注"待验证"；
5. 填充完成后运行校验：`python scripts/KLS_validate_position.py <产物> --type <diagnosis|roadmap|verifier|question>`。

## 运行时数据（不在技能包内）

问题资产目录文件由使用者随时指定路径（多册并存；禁止指向技能包内部）；文件不存在时按 KLS-question-asset-template.md 的骨架懒创建；追加只增行不改骨架。数据路径协议详见 references/knowledge-loop-strategist-requirements.md 中 KLS4 域级说明。
