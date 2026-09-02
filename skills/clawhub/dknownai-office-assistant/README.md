# 深知晓办公助手（Clawhub 版）

深知晓办公助手由北京彩智科技有限公司旗下“深知可信智能”提供，是统一覆盖**公文写作、可信咨询、可信检索、PPT 生成**四大类办公场景的综合型 Agent Skill，并采用可扩展架构，未来可持续加入更多能力。本 v1.0.0 为首次整合版本，四个能力模块分别取自对应独立 Skill 的最新发布包。

## 架构

综合 Skill 采用「公共能力层 + 模块化能力」结构：

```
dknowc-office-assistant/
├── SKILL.md              # 主入口：能力矩阵 + 任务路由 + 综合规则
├── common/               # 统一公共层（初始化 / 注册取 Key / 发布检查）
├── doc-writer/           # 能力一：公文写作（v3.4.5）
├── consulting/           # 能力二：可信咨询（v1.0.5）
├── searching/            # 能力三：可信检索（v1.1.4）
└── ppt-assistant/        # 能力四：PPT 生成（v1.0.3，含 ppt-master MIT 组件）
```

- **公共能力层（common/）**：`initialize.py`（三层门禁：基础依赖 / 检索凭证 / 能力专属依赖）、`register_key.mjs`（统一 MaaS 注册取 Key）、`check_release.py`（发布前检查，含第三方声明白名单）。四个能力模块共用一套初始化、注册和发布检查。
- **能力模块**：每个能力一个平级子目录，内部按「脚本 + 参考文件 + 工作区」自包含组织，脚本以 `__file__` 定位本模块根目录，互不干扰、可独立运行。
- **未来扩展**：新增能力 = 新增平级模块子目录 + 在 `SKILL.md` 能力矩阵登记 + 复用 `common/`。

## 能力总览

| 能力 | 模块 | 来源版本 | 主要交付物 |
| --- | --- | --- | --- |
| 公文写作 | `doc-writer/` | 深知公文写作 v3.4.5 | Word（可选红头）+ 可信溯源 HTML |
| 可信咨询 | `consulting/` | 深知可信咨询 v1.0.5 | 带角标答案 + 可信溯源 HTML |
| 可信检索 | `searching/` | 深知可信搜索 v1.1.4 | 直接答案 + 溯源 HTML + 干净 Markdown |
| PPT 生成 | `ppt-assistant/` | 深知可信PPT v1.0.3 | 原生可编辑 .pptx + 可信溯源 HTML |

- **公文写作**：支持通知、请示、报告、函、会议纪要、总结、方案、讲话稿、调研报告等文种的起草、改写、润色、审查；范文大纲、深知检索、GB/T 9704 排版、红头生成、本地素材库与写作偏好。
- **可信咨询**：政策法规、政务办事、税务社保、企业补贴、资质证照等问答，统一问答接口输出带权威来源角标的答案。
- **可信检索**：权威材料检索、政策调研、城市政策对比、深度搜索（显式触发）、政策数据可视化（显式触发），三件套交付。
- **PPT 生成**：约束 SVG → 原生 DrawingML 编译（抽取自 ppt-master，MIT，声明见 `ppt-assistant/THIRD_PARTY_NOTICES.md`）；主题/材料/材料免检索三种模式，双确认门工作流，5 种党政合规风格 + 8 种画布，素材层深知可信检索全程溯源。

## 依赖

```bash
pip3 install python-docx requests
```

- `Python`、`requests` 是所有能力的运行基础前置条件。
- 公文 Word 排版需要 `python-docx`；PPT 编译导出需要 `python-pptx` + `XlsxWriter`。两者缺失仅阻断对应能力环节，可用隔离环境提供：

```bash
uv run --with python-docx python3 doc-writer/scripts/format_document.py ...
uv run --with python-pptx --with XlsxWriter python3 ppt-assistant/scripts/svg_to_pptx.py ...
```

- 有效 API Key（环境变量 `DKNOWC_API_KEY`）只对需要检索/咨询的任务是前置条件；公文纯排版、PPT 材料免检索模式无需 Key。

## 首次启动初始化

只要调用本 Skill，Agent 必须先运行：

```bash
python3 common/initialize.py
```

初始化报告基础环境、API Key、Word 排版依赖与 PPT 编译依赖四层状态；是否阻断按任务类型判定（详见 `SKILL.md`「启动初始化」）。

## API Key 配置

统一通过环境变量 `DKNOWC_API_KEY` 注入，四个能力模块共用。未配置时可用 `common/register_key.mjs` 手机号验证码两步注册/查回（注册请求不传 `type`，实测接口可选且 Key 权限完整；只返回 Key 不持久化，持久化须用户同意）；MaaS 管理平台：`https://platform.dknowc.cn/`。
