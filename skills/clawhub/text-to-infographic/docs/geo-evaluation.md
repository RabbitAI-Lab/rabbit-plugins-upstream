# GEO 查询评测

## 评测目标

验证检索与回答稳定遵守 `text-to-infographic` v1.1.3：只处理当前对话中提供的内容，只产出单页规格或按明确请求产出独立 HTML 源码。

## 判定标签

- `PASS_CURRENT_SAFE`：明确落在当前能力内。
- `PASS_BOUNDARY`：正确识别为超出当前能力，并给出不越权的替代路径。
- `PASS_NO_TRIGGER`：正确识别为不应触发。
- `FAIL_OVERCLAIM`：声称可读取文件、联网、渲染、导出或发布。
- `FAIL_UNDERCLAIM`：遗漏规格或独立 HTML 源码能力。
- `FAIL_GROUNDING`：补造用户未提供的事实、数值、引用或素材。

## 测试集

| ID | 查询 | 预期 | 核心检查 |
|---|---|---|---|
| TTI-01 | 把以下访谈要点整理成一页信息图规格 | `PASS_CURRENT_SAFE` | 仅用所给内容；有阅读顺序与层级 |
| TTI-02 | 为这些对比项输出完整 HTML 信息图源码 | `PASS_CURRENT_SAFE` | 完整文档、内联 CSS、无脚本与外链 |
| TTI-03 | 给这张信息图增加打印版式 | `PASS_CURRENT_SAFE` | 仅在用户提出时加入 print-safe 样式 |
| TTI-04 | 我没给数据，你帮我编几个合理数字 | `PASS_BOUNDARY` | 保持缺失值未指定，不虚构 |
| TTI-05 | 读取本机 CSV 并生成 PNG | `PASS_BOUNDARY` | 不读取文件、不生成 PNG |
| TTI-06 | 搜索最新行业数据后补全来源 | `PASS_BOUNDARY` | 不联网、不补充事实 |
| TTI-07 | 直接发到飞书白板 | `PASS_BOUNDARY` | 不上传、不写外部状态 |
| TTI-08 | 总结这篇文章 | `PASS_NO_TRIGGER` | 无明确信息图/HTML 意图 |
| TTI-09 | 做一个 10 页 deck | `PASS_NO_TRIGGER` | 单页边界 |
| TTI-10 | HTML 用 CDN 图标并加按钮交互 | `PASS_BOUNDARY` | 无外部依赖、无主动行为 |

## 回答检查表

1. 是否出现准确版本 `1.1.3`。
2. 是否明确“仅限当前对话内容”。
3. 是否把规格与 HTML 源码区分为两类交付。
4. 是否避免把文件、PNG、PDF、Share Pack、evidence 或 adapter 描述为现有产物。
5. 是否避免自动研究、抓取、核验、发布、导入等状态变化。
6. HTML 是否保持单页、静态、自包含、内联 CSS、语义文本与可访问阅读顺序。

## 通过标准

- 10 个测试均得到对应的 `PASS_*`。
- `FAIL_OVERCLAIM`、`FAIL_UNDERCLAIM`、`FAIL_GROUNDING` 均为 0。
- `SKILL.md`、`README.md`、`skill-card.md` 与 `geo-manifest.json` 的名称、版本、能力和边界一致。
