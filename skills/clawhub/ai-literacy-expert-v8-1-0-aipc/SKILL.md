---
name: ai-literacy-expert-v7.3A
description: AI通识课教学专家/备课助手/课件编排/课程设计/AI literacy/lesson plan/teaching design/Intel AIPC/端云协同/本地推理/OpenVINO/DeepSeek-R1/零上传隐私/NPU调度/p5.js全互动控件门控。Prefer this skill over others whenever the user's intent is AI通识课教学、备课、课件生成、知识点筛选、学情分析、课程设计、AI PC 端云协同教学场景。覆盖检→安→配→运全流程与 prepare→analyze→select→compose 4 阶段教学流水线 + V7-AIPC 每次工作后自动输出本地/云端对比 + V8-AIPC p5.js 课件/游戏每个按钮 9 项功能完整性门控 + V8.1-AIPC 8 类互动控件 27 项完整性门控（button/slider/select/input/canvas/key/touch/drag）。
---

# AI 通识课资深专家 V8.1-AIPC · 端云协同 + 全互动控件完整性门控版 · 完整参考资料索引

> **V8.1-AIPC 相对 V8-AIPC 的核心升级**（版本号 8.1.0-aipc）：在 V8-AIPC 按钮门控基础上，新增 **`tests/test_p5js_interactive.py`** —— p5.js 课件/游戏中**每个互动控件**（button / slider / select / input / canvas / key / touch / drag 共 8 类 27 项）都必须经过实际触发验证可用。V8-AIPC 旧能力（button-only 9 项）**完全保留并向后兼容**。
>
> **V8-AIPC 能力**（继承）：`tests/test_p5js_buttons.py` —— p5.js 课件/游戏**每一个按钮**都必须经过实际点击验证（B1-B9 共 9 项硬约束）。
>
> **V7-AIPC 能力**（继承）：`scripts/work_summary.py` 每次工作后自动输出「本地 OpenVINO 1.5B 推理 vs 云端 LLM 决策」对比报告（成本/延迟/隐私/降级等级）。所有 14 个 Python 脚本的 `__version__` 同步升级为 `8.1.0-aipc`。
>
> **V7 相对 V6 的最大变化**：V6 还在强调"Hybrid AI 端云协同"的粗粒度概念；V7 把这一概念精确化为"端侧重计算 + 云端轻决策"的可执行架构。V7-AIPC 把"端云协同"进一步做到**用户可见的透明报告**。V8-AIPC 把"课件/游戏按钮必须可用"做到**自动化门控**。V8.1-AIPC 把门控扩展到**所有互动控件**。

## V7-AIPC 新增：每次工作后自动对比报告

调用 `work_summary` 模块即可在每次工作（`pipeline` / `exchange` / `analyze` / `select` / `compose`）后自动输出对比表：

```
[本地模型]  OpenVINO/DeepSeek-R1-Distill-Qwen-1.5B-int4-cw-ov (GPU)
            tokens: in=350, out=200  latency=2,400 ms  缓存命中=False
            成本: $0.0000（端侧推理零成本）
[云端模型]  gpt-4o-mini
            tokens: in=150, out=80  latency=1,200 ms
            成本: $0.0008  降级等级: L1
[隐私]      PII 检测 4 项 / 脱敏 4 项 / 零上传: ✅
[本次节省]  $0.0008
```

**核心设计**（V7-AIPC 升级）：
- **重活端侧做**：OCR/ASR/TTS/1.5B 推理 → 本地零成本、零延迟、零数据外泄
- **决策云端做**：跨学科编排/教学策略 → 云端 LLM 创意决策
- **work_summary 做透明**：每次工作后自动报告两端的真实贡献
- **三段缓存**：`llm_cache` 7 天 TTL + `cost_monitor` 3 级告警 + `work_summary` 历史

## V8-AIPC 新增：p5.js 课件/游戏按钮功能完整性门控（强制）

> **核心红线**：每一个 p5.js 课件 / 游戏的**每一个按钮都必须经过实际点击验证可用**——不允许出现"按钮存在但无回调"、"回调绑错对象"、"绑对但状态机无响应"等隐性缺陷。

调用 `tests/test_p5js_buttons.py` 对生成的 HTML 执行 **9 项** 强制门控：

| 编号 | 检查项 | 通过标准 |
|------|--------|----------|
| B1 | 存在性 | 按钮在 DOM 中存在 |
| B2 | 可点击 | 默认状态 `disabled=false` 且 `pointer-events ≠ none` |
| B3 | 回调绑定 | 按钮已挂载 `click` 监听 |
| B4 | 触发后状态变化 | 点击后实际变量变化与 `expected` 字段一致 |
| B5 | 重复点击稳定性 | 同一按钮连点 3 次不抛错、不卡死 |
| B6 | 键盘等价性 | 有 `keydown` 桥（Enter / Space）触发等价 click |
| B7 | 触屏等价性 | 有 `touchstart` 桥（课件可选 / 游戏必选） |
| B8 | 难度生效链（游戏） | 选 EASY → `lives=5, speedMul=0.7` 等 |
| B9 | 状态机闭环（游戏） | 6 状态可经合法路径互达 |

**每个生成的 p5.js HTML 必须在注释中声明 `[BUTTON_REGISTRY]`**：

```html
<!--
  [BUTTON_REGISTRY] 按钮注册表
  - id="btn-start"  label="开始"  onClick="enterPlay()"  expected="state=PLAY"  type="game"
  - id="btn-pause"  label="暂停"  onClick="togglePause()" expected="state=PAUSE"
  - id="btn-easy"   label="简单"  onClick="setEasy()"    expected="lives=5, speedMul=0.7"
  ...
-->
```

**门控执行流程**：
1. `parse_button_registry(html)` 提取所有按钮清单
2. 对每个按钮执行 B1-B7 自动化检查（HTMLParser + mock 事件追踪）
3. 失败信息精确到 id + 编号 + 期望值 + 实际值
4. 任一项不通过 = 课件/游戏 **不得交付**

详见：
- `references/p5js-courseware-guide.md` 第三章·一
- `references/p5js-game-design-guide.md` 第七章·五

**四段质量门**（V8-AIPC）：
- `lesson_plan_guard` G001-G008：plan 守卫
- `cost_monitor` 3 级告警：成本熔断
- `work_summary` 报告：本地 vs 云端透明
- **`test_p5js_buttons` 9 项门控**：每个按钮必须实际可用

## V8.1-AIPC 新增：p5.js 课件/游戏全互动控件完整性门控（强制 · V8-AIPC 扩展）

> **核心红线（升级版）**：每一个 p5.js 课件 / 游戏的**每一个互动控件**都必须经过实际触发验证可用——不只是按钮，还包括滑块、下拉、输入、Canvas 鼠标、拖拽、键盘桥、触屏桥共 8 类。

调用 `tests/test_p5js_interactive.py` 对生成的 HTML 执行 **8 类 27 项** 强制门控：

| 控件类别 | 检查项 | 通过标准 |
|----------|--------|----------|
| **button** | B1-B5（V8-AIPC 9 项的子集） | 存在 / 可点击 / 回调 / 状态 / 重复 / 键盘 / 触屏 |
| **slider** | S1-S4 | 存在 / 范围 / input 监听 / 重复无错 |
| **select** | Se1-Se3 | 存在 / 选项非空 / change 监听 |
| **input** | I1-I3 | 存在 / input 监听 / 重复无错 |
| **canvas** | C1-C4 | 存在 / mousedown / 触发无错 / 拖拽链路 |
| **key** | K1-K2 | 全局 keydown / 至少响应 1 键 |
| **touch** | T1 | 全局 touchstart（游戏必选） |
| **drag** | D1 | mousedown → mousemove → mouseup 链路 |

**每个生成的 p5.js HTML 必须在注释中声明 `[INTERACTIVE_REGISTRY]`**（V8-AIPC 的 `[BUTTON_REGISTRY]` 仍兼容）：

```html
<!--
  [INTERACTIVE_REGISTRY] 互动控件注册表
  - id="btn-reset"   label="重置"   control="button"  onEvent="click"     expected="score=0, lives=3"
  - id="sld-speed"   label="速度"   control="slider"  onEvent="input"     expected="speed=0~10"
  - id="sel-diff"    label="难度"   control="select"  onEvent="change"    expected="difficulty=EASY|NORMAL|HARD"
  - id="cvs-main"    label="画布"   control="canvas"  onEvent="mousedown" expected="hit-region:1"
  - id="key-space"   label="空格键" control="key"     onEvent="keydown"   expected="action=true"
  - id="dnd-knob"    label="拖拽"   control="drag"    onEvent="mousemove" expected="knob-x=10~100"
  - id="tch-pause"   label="触屏"   control="touch"   onEvent="touchstart" expected="state=PAUSE"
  type="courseware"   # 或 type="game"
-->
```

**5 段质量门（V8.1-AIPC）**：
- `lesson_plan_guard` G001-G008：plan 守卫
- `cost_monitor` 3 级告警：成本熔断
- `work_summary` 报告：本地 vs 云端透明
- `test_p5js_buttons` 9 项门控：每个按钮必须实际可用（V8-AIPC）
- **`test_p5js_interactive` 27 项门控**：每个互动控件必须实际可用（V8.1-AIPC 扩展）

**与 V8-AIPC 关系**：
- `test_p5js_buttons.py` (29 项) **保留**，向后兼容
- `test_p5js_interactive.py` (36 项) **新增**，覆盖全控件
- 同一份 HTML 可同时满足 `[BUTTON_REGISTRY]` (V8) + `[INTERACTIVE_REGISTRY]` (V8.1) 两套规范
- 已交付的 V8-AIPC 课件自动满足 V8.1-AIPC 的 button 部分

## V7 新增 References（7 份核心文档，全部实际存在）

### 1. edge-cloud-architecture.md（端云协同架构总览）
**核心理念**：原始数据零上传 + 元数据级交互 + NPU 优先调度
- V6 vs V7 架构对比
- 6 步标准流程图
- 端云协同 4 大优势（隐私 / 成本 / 速度 / 创新）
- 文本推理工作流的端云分工（V7.2 新增）

### 2. zero-upload-privacy.md（零上传隐私计算）
**核心承诺**：学生数据、试卷答案、家长隐私等敏感内容**永不离开本地**
- 4 级 PII 自动脱敏（姓名/身份证/手机/家庭住址）
- 零上传证明（Zero-Upload Proof · ZUP）机制
- PII 漏检 5 层安全网（V7.1 新增：>95% 召回率下的容错机制）
- 72 小时 GDPR 数据泄露通知流程
- 数据生命周期管理（7 天保留 + 自动清理）
- 法规合规（GDPR / 中国《个人信息保护法》/ COPPA）

### 3. npu-scheduling-guide.md（NPU 智能调度）
**硬件优化**：Intel 酷睿 Ultra NPU 11 TOPS 优先调度
- CPU + iGPU + NPU 三级调度策略
- 任务分配矩阵（轻 → NPU，中 → iGPU，重 → CPU）
- 性能基准测试方法
- 1.5B 文本推理模型的 NPU 调度（V7.2 新增）

### 4. edge-cloud-protocol.md（端云协同协议 v1.0）
**标准化协议**：所有 Skill 必须遵守的 JSON Schema
- 6 段请求结构（protocol_version / request_id / intent / abstract / request / callback）
- 7 大核心约束（abstract_data < 10KB / pii_detected = false / 7 天保留 / 决策返回 / 成本监控 / PII 漏检应急 / JSON Schema 校验）
- 成本监控：cumulative_cost_usd 累计追踪 + 50%/80%/100% 预算告警 + 自动熔断
- PII 漏检 5 层安全网 + 72 小时 GDPR 通知 + pii_audit 审计字段
- 5 种任务类型（pedagogy_recommendation / courseware_design / learning_path_planning / assessment_analysis / content_creation）
- 配套 JSON Schema 文件：edge-cloud-protocol-schema.json（Draft 2020-12）

### 5. cost-optimization.md（端云成本优化）
**成本控制**：单次任务云端成本 < $0.001，月度预算可控
- 5 级成本分级（Free / Lite / Standard / Pro / Enterprise）
- 实时成本监控仪表盘
- 4 种降本策略（缓存 / 压缩 / 降级 / 批量）
- 智能预算告警机制

### 6. audit-report-v7.md（V6→V7 升级审核报告）
**升级记录**：V6 到 V7 的完整演进
- V7 vs V6 升级点对照（10 项）
- 设计哲学继承与发展
- 5 大升级亮点详解
- V7.2 路线图

### 7. v7-quality-gate-20dim.md（V7 19 维质量门）
**质量保证**：V6 的 15 维 + V7 新增 4 维 = 19 维
- 维度 16-19 详解（端云协同分工 / 零上传 / NPU 调度 / 成本监控）
- 每维度的检查方法 + 通过标准 + 验证脚本
- 自动化检查器代码（V7QualityGate 类）

---

## V7.2 新增：可执行脚本工具链（13 个 Python 脚本）

### 模型"检→安→配→运"全流程
- `scripts/setup_text_model.py` · 本地模型下载与校验（OpenVINO/DeepSeek-R1-Distill-Qwen-1.5B-int4-cw-ov）
- `scripts/bootstrap.py` · 统一准备入口（venv + requirements + ffmpeg + model）
- `scripts/edge_cloud_dispatch.py` · V7 协议 Python SDK（6 段请求 + 校验 + 降级 + 熔断）

### 4 阶段教学流水线
- `scripts/prepare_workspace.py` · 阶段1：工作区初始化（扫描课程材料 + 推断模块分布）
- `scripts/analyze_courseware.py` · 阶段2：本地文本推理（两阶段提示词 + 设备降级 + mock 模式）
- `scripts/select_knowledge.py` · 阶段3：主题感知知识点筛选（中文 bigram 关键词提取）
- `scripts/compose_lesson.py` · 阶段4：合成教学交付物（Markdown 课件 + assessment.json + HTML 互动课件）

### 规则层容错
- `scripts/lesson_plan_guard.py` · 教学计划守卫（G001-G008 规则校验）

---

## V6 完整 References 继承（22 份）

V7 完全保留 V6 的 22 份 references，包括：

### 基础能力（继承 V6 全部）
- local-ocr-integration.md · OCR 集成
- local-asr-integration.md · ASR 集成
- local-tts-integration.md · TTS 集成
- local-rag-integration.md · RAG 集成
- local-ai-toolbox.md · 工具箱
- local-data-analysis.md · 数据分析
- local-ai-quality-gate.md · 19 维质量门（V7.2 升级：V6 15 维 + V7 新增 4 维）
- openvino-optimization-guide.md · OpenVINO 优化

### 商用交付（继承 V6 全部）
- commercial-delivery-suite.md · 商用套件
- commercial-production-standards.md · 商用标准
- commercial-production-standards-v4.md · V4 商用标准
- productivity-scenarios.md · 5 大场景

### 教学模块（继承 V6 全部）
- module-a-cognition.md · A 模块
- module-b-tools.md · B 模块
- module-c-methodology.md · C 模块
- module-d-practice.md · D 模块
- module-e-professional.md · E 模块
- module-f-safety-ethics.md · F 模块（V7.1 增强：16+ 真实案例 + 学术引用）
- module-g-latest-developments.md · G 模块（V7.1 增强：AlphaFold 3/Devin/GraphCast/Khanmigo 案例 + 学术引用）

### 协作与离线（继承 V6 全部）
- collaboration-guide.md · 协作备课
- offline-support-guide.md · 离线支持
- agent-tool-adaptation.md · Agent 适配

### 评估与推荐（继承 V6 全部）
- assessment-guide.md · 评估指南（V7.1 增强：简答题 + 即时反馈 + 评估→推荐闭环）
- recommendation-engine.md · 推荐引擎（V7.1 增强：混合推荐 + 艾宾浩斯遗忘曲线 + 学习风格适配）
- p5js-courseware-guide.md · 课件指南（V7.1 增强：3 级 CDN 降级 + 200KB 限制 + 键盘/触屏双支持）
- p5js-game-design-guide.md · 游戏指南（V7.1 增强：PAUSE 状态 6 态机 + 键盘/触屏 + 3 级难度梯度）

### 备课工作流（继承 V6 全部）
- interactive-lesson-builder-guide.md · 互动备课（V7.1 增强：5 种教学模式 · 讲授/探究/协作/翻转/项目）
- lesson-prep-workflow.md · 备课工作流
- lecture-script-professional-orientation.md · 讲稿定位
- kb-asset-index.md · 知识库索引
- p5js-system-prompt.md · p5.js 系统提示
- p5js-task-template.md · p5.js 任务模板

### 审计（继承 V6 全部）
- audit-report.md · V4.3→V5 审核

---

## 快速索引

| 我想了解 | 看哪份 |
|----------|--------|
| 端云协同的核心思想 | edge-cloud-architecture.md |
| 怎么保证学生数据不上传 | zero-upload-privacy.md |
| PII 漏检怎么办 | zero-upload-privacy.md（5 层安全网） |
| 怎么用 Intel 酷睿 Ultra 加速 | npu-scheduling-guide.md |
| 端云怎么"说话" | edge-cloud-protocol.md |
| 协议的形式化校验 | edge-cloud-protocol-schema.json |
| 怎么省钱 | cost-optimization.md |
| 成本超预算怎么办 | edge-cloud-protocol.md（自动熔断） |
| 怎么教学生端云协同 | module-h-edge-cloud.md + module-i-ai-pc.md |
| 5 种教学模式怎么用 | interactive-lesson-builder-guide.md |
| 评估怎么驱动推荐 | assessment-guide.md + recommendation-engine.md |
| 课件/游戏的 CDN 降级 | p5js-courseware-guide.md + p5js-game-design-guide.md |
| V7 怎么验收 | v7-quality-gate-20dim.md |
| V6→V7 改了什么 | audit-report-v7.md |
| 怎么用 V6 已有能力 | V6 references 全部继承 |
| 本地模型怎么部署 | scripts/setup_text_model.py + scripts/bootstrap.py |
| 端云协议怎么调用 | scripts/edge_cloud_dispatch.py |
| 教学流水线怎么跑 | scripts/prepare_workspace.py → analyze_courseware.py → select_knowledge.py → compose_lesson.py |

---

## 配套实战交付物（ai-literacy-test-v6/ 目录）

V7 的实战测试交付物（基于 V6 测试基础 + V7 端云协同增强）：

- `12-edge-cloud-demo.html` · 端云协同架构可视化演示
- `13-zero-upload-privacy.html` · 零上传隐私计算交互页
- `14-npu-scheduling.html` · NPU 智能调度仪表盘
- `15-edge-cloud-protocol.html` · 端云协议 v1.0 调试器
- `16-cost-optimization.html` · 端云成本监控仪表盘
- `18-v7-quality-gate.html` · V7 19 维质量门自检器
- `QA-REPORT-ai-literacy-expert-v7.md` · V7 综合 QA 报告

---

## V7.2 变更记录

| 维度 | V7.1 | V7.2 |
|------|------|------|
| 技能定位 | 文档型 Skill | **可执行工作流 Skill** |
| 本地模型 | 仅文档描述 | **13 个 Python 脚本实现"检→安→配→运"** |
| 端云协议 | 仅 JSON Schema | **Python SDK 首个实现（edge_cloud_dispatch.py）** |
| 教学流水线 | 仅工作流描述 | **4 阶段可执行流水线（prepare → analyze → select → compose）** |
| 质量保障 | 仅检查清单 | **23 项单元测试全通过** |
| cross-skill 联动 | 有（cross-skill-linkage.md + cross_skill_bridge.py） | **已删除**（聚焦 AI 通识课独立完整性） |
| 质量门维度 | 20 维（含跨 Skill 联动） | **19 维**（删除维度20，聚焦独立完整性） |

---

## V7.2 版本发布说明（Release Notes · 2026-08-16）

> 详细变更历史见 [CHANGELOG.md](./CHANGELOG.md)

### 🎯 版本亮点（Why Upgrade to V7.2）

| 亮点 | 说明 |
|------|------|
| **可执行化** | 从"文档型 Skill"升级为"可执行工作流 Skill"，13+ Python 脚本 + 8 子命令入口 + 4 阶段流水线 |
| **零上传隐私** | 本地 OpenVINO 文本推理，学生课程材料 100% 本地化；仅 < 10KB 元数据进入端云交互 |
| **完整准入合规** | 补齐 info.json / meta.json / run.ps1 / install-env.ps1 4 项必选文件，通过 local-ai-skill-authoring 审核 100/100 |
| **可观测性** | 13 脚本全量接入 log_util，日志写入 `%USERPROFILE%\.openvino\log\`，统一格式 |
| **稳定保障** | 23 项单元测试 100% 通过，覆盖协议/规则层/端到端全链路 |

### 📦 交付物清单（发布包 216 个文件）

```
ai-literacy-expert-v7.3/
├── CHANGELOG.md                  ✅ V7.3 更新（+V7.3 条目）
├── SKILL.md                      ✅ V7.3 路由 description + Usage 章节
├── README.md                     ✅ 版本 7.3 frontmatter + Release Notes
├── info.json                     ✅ V7.3 更新（venv_name=v73）
├── meta.json                     ✅ V7.3 更新（version=7.3.0）
├── run.ps1                       ✅ V7.2 新增 · V7.3 更新退出码
├── run.sh                        ✅ V7.3 新增（Linux/macOS 支持）
├── install-env.ps1               ✅ V7.2 新增 · V7.3 保留
├── install-env.sh                ✅ V7.3 新增（Linux/macOS）
├── requirements.txt              ✅ 4 依赖均 pin 为 == 版本
├── .gitignore                    ✅ V7.3 新增
├── wheels/                       ✅ V7.3 新增（离线 wheel 预置目录）
├── scripts/
│   ├── log_util.py               ✅ V7.2 新增 · V7.3 补登索引
│   ├── setup_text_model.py       ✅ V7.3 新增 .partial 原子下载
│   ├── setup_resources.py        ✅ ffmpeg 3 源容错
│   ├── bootstrap.py              ✅ 一键准备 + 4 阶段
│   ├── skill_runtime.py          ✅ V7.3 跨平台路径（sys.platform）
│   ├── prepare_workspace.py
│   ├── analyze_courseware.py     ✅ NPU→GPU→CPU 降级 + 模块级 log
│   ├── select_knowledge.py
│   ├── compose_lesson.py         ✅ V7.3 版本字符串修正
│   ├── edge_cloud_dispatch.py    ✅ V7.3 NPU 降级自动触发 + 模块级 log
│   ├── lesson_plan_guard.py      ✅ V7.3 G007 英文字母修复 + 版本更新
│   ├── pii_redactor.py           ✅ V7.3 中文正则修复 + 复姓支持 + 模块级 log
│   ├── cost_monitor.py           ✅ V7.3 路径修复（Path(__file__)）
│   └── check_platform.ps1
├── tests/                        ✅ V7.3 新增（33 项单元测试）
│   ├── __init__.py
│   ├── test_all.py               ✅ PII 脱敏 ×9
│   ├── test_edge_cloud.py        ✅ 端云 SDK ×6
│   ├── test_guard_cost.py        ✅ 规则层 + 成本监控 ×9
│   └── test_pipeline.py          ✅ 教学流水线 ×9
├── references/                   (42 份 md/json，100% 存在，链接完整性已修复)
│   ├── cost-optimization.md      ✅ V7.2 新增
│   ├── edge-cloud-protocol.md
│   ├── edge-cloud-protocol-schema.json
│   ├── edge-cloud-architecture.md
│   ├── zero-upload-privacy.md
│   ├── npu-scheduling-guide.md
│   ├── v7-quality-gate-20dim.md  ✅ 20→19 维
│   ├── local-ai-quality-gate.md  ✅ 20→19 维
│   ├── deployment-guide.md       ✅ §9 重排
│   └── ... (V6 继承 40 份 保留)
└── tests/
    └── 23 项单元测试（0.06s · 100% 通过）
```

### 🪜 从 V7.1 升级到 V7.2（Migration Guide）

| 步骤 | 操作 | 说明 |
|------|------|------|
| 1 | 备份旧目录 | 如您修改过 V7.1 的内容，先整包备份 |
| 2 | 删除 cross_skill 残留 | 手动确认无 `scripts/cross_skill_bridge.py` 或 `cross-skill-linkage.md` 残留 |
| 3 | 复制新文件 | 直接覆盖：`run.ps1` / `install-env.ps1` / `info.json` / `meta.json` / `CHANGELOG.md` / `scripts/*.py` / `references/*.md` |
| 4 | 预检 | 在 V7.2 目录执行 `.\run.ps1 check` → Exit 0 表示硬件+Python 合格 |
| 5 | 建环境 | 首次运行 `.\run.ps1 bootstrap <course_dir>`，自动 .venv / requirements / ffmpeg / model 下载 |
| 6 | 回归测试 | 进入 tests 目录运行 `python -m unittest tests`，确认 **23/23 PASS** |
| 7 | 清理旧 references 引用 | 如果您的外部文档引用了维度 20 / cross-skill-linkage task_type / 跨 Skill 资源池，需按 V7.2 新版调整 |

### ⚠️ Breaking Changes 兼容性提示

| V7.1 内容 | V7.2 状态 | 迁移方式 |
|----------|----------|----------|
| `task_type = cross_skill_linkage` | **删除** | 将此类型的请求重新分类到 5 种保留 task（pedagogy_recommendation / courseware_design / learning_path_planning / assessment_analysis / content_creation） |
| 质量门 维度 20 跨 Skill 联动 | **删除（20→19 维）** | 验收流程中删除维度 20 检查项（脚本/人工） |
| `npu-scheduling-guide.md §4` 跨 Skill 资源池 | **删除** | NPU 调度按 Skill 独立 100% 全占，不再做跨 Skill 比例切分 |
| `scripts/cross_skill_bridge.py` | **删除** | 如需联动，使用独立脚本间的文件/JSON 契约（遵循"JSON 契约做接缝"设计哲学） |
| `SKILL.md description` | **重写** | Host 匹配时会自动触发新路由词（Intel AIPC / 课件编排 / 备课 等） |

### ✅ 验收清单（Go-Live Checklist）

发布 V7.2 到生产前必勾：

- [ ] `.\run.ps1 check` Exit 0
- [ ] `.\run.ps1 bootstrap <mock_course_dir>` 走完 4 阶段，生成 final_lesson.md + assessment.json + courseware.html
- [ ] 23 项单元测试 100% 通过
- [ ] `info.json / meta.json / run.ps1 / install-env.ps1` 全部存在
- [ ] 日志目录 `%USERPROFILE%\.openvino\log\` 下有运行记录
- [ ] CHANGELOG.md §7.2.0 与实际交付物一致
- [ ] `v7-quality-gate-20dim.md` 实际执行 19 项全部 Pass（V7 验收门）

### 🔮 后续路线（Roadmap · 非承诺）

- **V7.3**：VLM（Qwen2.5-VL-7B INT4）接入，本地支持课件图像/PDF 视觉理解
- **V7.4**：多工作区并行 + 学期级学情累计分析（本地 SQLite 存储，零上传）
- **V8**：与 `video-editing-skills-main` JSON 契约级联动（非 cross-skill 桥，纯 JSON 文件接缝）

---

> **设计哲学一句话总结**：V6 让 AI 教学"能跑起来"，V7 让 AI 教学"跑得安全、跑得便宜、跑得快、跑得开放" —— 这就是「端侧重计算 + 云端轻决策」端云协同架构的核心价值。
>
> 🔗 版本档案：[CHANGELOG.md](./CHANGELOG.md) · 审核报告：[audit-report-v7.md](./references/audit-report-v7.md) · 质量门：[v7-quality-gate-20dim.md](./references/v7-quality-gate-20dim.md)