---
name: 明日DMP智能组合圈人
description: 基于用户自然语言投放需求，按"需求解析→标签召回→画像补全→质量排序→用户选择→Overlap（仅MUST vs 可选）→递进组合→创建组合人群"的循序渐进流程，输出可直接用于明日DMP组合人群（audienceType=2）的标签组合规则与人群包创建参数。
metadata:
  version: 1.0.0
  author: mingri26
  tags:
  - dmp
  - 人群圈选
  - 组合人群
  - 标签组合
  - 语义召回
---

# 明日DMP智能组合圈人（Skill 用户手册）

## 概述

本技能基于明日DMP开放平台，通过自然语言理解+标签语义召回+画像分析+Overlap计算，按14步循序渐进流程，帮您精准圈选组合人群（audienceType=2）。

核心特点：
- 多Query确定性TF-IDF标签语义召回（零依赖可复现）
- 标签画像补全（四级匹配策略JOIN指标表）
- 按需求维度分组推荐（语义主排序+工程门槛过滤）
- Overlap重叠率计算（仅MUST vs 可选标签）
- 递进组合方案生成（精准/扩展/综合2~3条）
- 用户逐步确认后才创建最终人群包

⚠️ **重要声明**：
1. **凭证安全责任**：您的 Access Key（AK）和 Secret Key（SK）是访问明日 DMP API 的唯一凭证，属于您的敏感私密信息。您对凭证的妥善保管负全部责任。因凭证泄露、遗失或不当使用导致的一切损失，均由您自行承担。
2. **数据合法性责任**：使用本技能进行人群圈选操作时，您须保证所使用的数据来源合法合规，并已取得必要的用户授权。因数据来源违法、侵权或违反相关法律法规所引发的一切法律责任与纠纷，均由您自行承担。
3. **操作结果责任**：本技能的所有 API 调用结果均由明日DMP平台提供，本技能开发者对 API 返回内容的准确性、完整性不作任何保证，对因此产生的业务损失不承担责任。
4. **使用即视为同意**：继续使用本技能，即表示您已阅读并同意上述免责声明。

---

## 🔑 前置准备

使用本技能前，您需要先获取明日DMP API凭证：

**📧 申请方式（二选一）：**

**方式一：邮件申请**
- 发送至：product@mingdata.com
- 邮件主题：【明日DMP API开通申请】
- 邮件内容：请注明公司名称、联系人、联系方式及使用场景

**方式二：在线表单申请**
- 填写申请表单：https://doc.weixin.qq.com/forms/ANEAJwfLAAoADMAHwbhAPICNUE0vDRd8f#/fill
- 提交后等待审核通过（通常1-3个工作日）

**🔒 凭证格式：**
- Access Key：`xxxxxxxxxxxxxxxx`
- Secret Key：`xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

**💡 温馨提示**：首次使用时，我会自动引导您完成鉴权技能安装和凭证配置，无需担心！

---

## 一、核心能力与脚本清单

> 本技能同时具备"规范文档 + 可执行脚本"。脚本负责取数与过滤输出，references 负责规则说明。
> SKILL.md 不写"如何调用具体接口参数细节"。

### 1.1 核心脚本（按流程顺序使用）

| 脚本 | 用途 | 调用步骤 |
|------|------|---------|
| scripts/query_tag_list.py | 拉取 tag/list 并按“可用于组合”的标签条件过滤（已验证：isDirectory=1 为“可用于组合定向”的标签；isDirectory=0 为“纯分类目录/维度节点”，不可用） | Step 3 |
| scripts/build_queries.py | 根据Schema确定性生成query列表和boost-words（同Schema→同queries→同召回结果） | Step 4 |
| scripts/tag_semantic_search.py | 标签语义召回（确定性TF-IDF + cosine；核心词boost；稳定tie-break） | Step 4 |
| scripts/fallback_key_dimensions.py | Step 4.5 关键维度兜底召回（自动检测性别/年龄/城市级别缺失并补齐，赋予合理相似度，输出recall_source） | Step 4.5 |
| scripts/tag_profile_enrich.py | 标签画像补全（四级匹配策略；输出dimension/category/eng_score） | Step 5 |
| scripts/rank_candidates.py | 候选标签分组排序（按维度分组；组内确定性排序；核心维度保留明略+合作双来源标签供用户选择；支持markdown/box/card三种输出格式；末尾输出强制交互提示防止AI跳步） | Step 6 |
| scripts/match_third_party_tags.py | 三方标签离线表精确匹配（基于Schema关键词精确匹配OTT/剧目/OTA/京东4类三方标签，带噪声过滤和城市精确匹配） | Step 6.5 |
| scripts/confirm_execution_params.py | Step 8.5执行口径确认提示（输出强制交互提示，防止AI跳过trackType/idTypes询问直接创建人群） | Step 8.5 |
| scripts/tag_hierarchy.py | 标签层级工具（父子/互斥检测、维度分组、OR分组构建） | Step 8-12 |
| scripts/create_must_baseline.py | 创建MUST基准人群（仅MUST标签，自动维度分组OR+父子去重），严格轮询status=1 | Step 9 |
| scripts/analyze_overlap.py | Overlap分析：必建M∩Optional（渗透率r）；按需计算同维度OR候选对（1-3对）；互斥/父子逻辑判定不建包；标注exact/estimated | Step 10 |
| scripts/analyze_scale.py | 扩缩量分析报告（独立输出）：哪些标签收窄弱/适中/强、同维度OR增量、冗余/建议 | Step 11 |
| scripts/generate_plans.py | 生成4种组合方案（扩展/精准/综合/扩量），不生成跨维度OR方案 | Step 12 |
| scripts/create_combined_crowd.py | 创建最终组合人群（用户确认后才调用） | Step 14 |
| scripts/query_crowd_task.py | 查询人群任务状态（taskList），带状态中文说明 | Step 9/10/14 |

> ⚠️ 旧脚本 `calc_overlap.py`/`build_combinations.py` 已移至 `scripts/_legacy/`，不再使用。

### 1.2 基础脚本

| 脚本 | 用途 |
|------|------|
| scripts/dmp_api_client.py | DMP API客户端（通过鉴权技能subprocess调用；默认timeout=1800秒适配长时轮询） |
| scripts/auth.py | 鉴权参数通用解析（add_auth_args） |
| scripts/preflight_check.py | 前置环境校验（Python版本/鉴权技能/凭证/资产/脚本完整性/API连通性） |
| scripts/setup_credentials.py | 凭证配置（AK/SK写入本地文件 ~/.mingdata_dmp_credentials） |
| scripts/find_auth_skill.py | 鉴权技能路径查找（mingdata-dmp-auth） |
| scripts/check_task_logger.py | 任务记录技能（skill-logger）安装检查 |

> ⚠️ `scripts/_legacy/` 目录保留早期实验/废弃脚本（semantic_search_v2 / rank_refined / run_full_recall / expand_by_dimension / calc_overlap / build_combinations 等），仅供参考，主流程不调用。
| scripts/find_auth_skill.py | 鉴权技能查找与安装检查 |
| scripts/check_task_logger.py | 任务记录技能检查 |

### 1.3 零依赖声明

所有脚本仅使用Python标准库（≥3.8），无需pip install任何包；HTTP用urllib、TF-IDF纯手写、Excel用zipfile+xml解析。

---

## 二、输出语言与强制交付物（硬约束）

- **所有对用户的展示必须为中文字段/中文表头**。
- **结构化信息一律用表格呈现**：需求解析确认、默认推荐、标签分组、Overlap报告、方案对比、参数确认等所有结构化信息，必须使用表格格式展示，禁止用纯文字罗列。
- **每次执行必须同时展示：相似度评分 + 标签画像指标**（不得只给tagId或只给画像）。
- 若未完成以下任一"强制交付物"，视为流程未完成，**不得跳到组合方案（Step 12）**。

**强制交付物清单（每次必出）**：
1) **候选标签画像表（Step 5 输出）**：至少输出 Top20（或全部候选TopK中的可用部分），字段必须包含：
   - 标签ID(tagId)、标签名称(tagName)、来源（明略/合作伙伴）
   - 相似度（similarity，0~1，保留6位小数）
   - 维度（dimension）、类目（category）
   - 填充率（fill_rate）、覆盖率（coverage_rate）、工程分（eng_score）
   - 画像状态（profile_status：OK/MISSING）
2) **按维度分组推荐表（Step 6 输出）**：每组至少 Top5，字段同上（含相似度+画像）。

> 说明：相似度来自 Step 4 语义召回；画像指标来自 Step 5 指标表补全。两者必须同屏呈现。

### ✅ Step 6 展示格式强制规范
- **硬约束**：Step 6 的所有“分组推荐/缺口提示/补召回说明”必须以**表格**形式呈现，禁止纯文本罗列。
- **表格格式统一**：默认使用 **Markdown 表格（|---|）**。
  - 若用户当前渠道对 Markdown 表格渲染不稳定，可切换为 **Unicode 框线表格（┌─┬─┐）** 作为备用展示形式（字段与内容不变）。
- **字段硬约束（每行必须包含）**：
  - 标签ID(tagId)、标签名称(tagName)、来源（明略/合作伙伴）
  - 相似度(similarity，0~1，保留6位小数)
  - 维度(dimension)、类目(category)
  - 填充率(fill_rate)、覆盖率(coverage_rate)、工程分(eng_score)
  - 画像状态(profile_status：OK/MISSING)
  - 召回来源(recall_source：semantic / fallback_dict)
- **兜底标签也必须出表格**：即使画像缺失，也必须以 profile_status=MISSING 输出在表格中，不得省略。
- **缺口提示也必须表格化**：输出“缺口维度/诊断结论(gap_reason)/建议动作”。

**Step 6 表格模板（示例）**：

━━━ 📊【性别】（互斥维度；Step 6 仅展示候选，不做勾选）━━━
┌──────┬────────┬──────────┬────────┬────────┬────────┬────────┬────────┬──────────┐
│ 序号 │ 标签ID  │ 标签名称   │ 来源   │ 相似度 │ 填充率 │ 覆盖率 │ 工程分 │ 召回来源  │
├──────┼────────┼──────────┼────────┼────────┼────────┼────────┼────────┼──────────┤
│  1   │ 10701  │ 女        │ 明略   │ 0.000000│ 0.9580 │ 0.4700 │ 0.7140 │ fallback_dict │
└──────┴────────┴──────────┴────────┴────────┴────────┴────────┴────────┴──────────┘

**缺口卡片模板（示例）**：

┌──────────┬──────────────────────────────┬──────────────────────────┐
│ 缺口维度  │ 诊断结论(gap_reason)           │ 建议动作                 │
├──────────┼──────────────────────────────┼──────────────────────────┤
│ 活跃度    │ 标签池无该维度可用标签         │ 仅能按兴趣/城市/圈层等定向 │
│ 性别      │ 标签池存在但语义召回未命中     │ 触发 Step 4.5 兜底并补展示 │
└──────────┴──────────────────────────────┴──────────────────────────┘

---

## 三、使用前提与边界（防幻觉）

1) **本技能只做组合人群**（audienceType=2）。
2) **禁止编造**：tagId、标签名、量级、Overlap、覆盖度、填充率。
3) **候选标签来源硬约束**：候选标签必须来自 DMP `tag/list` 返回，且仅允许使用 **`isDirectory=1`** 的标签用于组合定向。
   - 已验证语义：`isDirectory=1` = 可用于组合定向（覆盖大类→叶子）；`isDirectory=0` = 纯分类目录/维度节点，不可用于组合。
4) **画像指标来源硬约束**：覆盖度/填充率/量级等不来自 `tag/list`，必须从项目提供的《标签指标表》或画像表中补全；缺失则标注缺口并降级处理。
5) **必须按流程逐步执行**：不得跳步输出最终组合；用户未确认不得创建最终人群包。

---

## 四、前置鉴权检查（每次执行前必做）

> 在执行任何圈人步骤前，必须先完成鉴权检查。
> 鉴权通过独立鉴权技能（mingdata-dmp-auth）完成，不在本技能内自行实现签名逻辑。

### 3.1 检查鉴权技能是否已安装

- **检查路径**：`~/.skills/mingdata-dmp-auth/`
- **如果已安装** → 跳到 3.2（凭证检查）
- **如果未安装** → 向用户展示以下提示并等待回复：

```
⚠️ 检测到您尚未安装【明日DMP鉴权技能】

该技能负责管理 API 凭证（AK/SK）、生成签名，是使用本功能的必要前提。

是否自动下载并安装？

是 - 立即安装
否 - 取消本次操作

请回复：是/否
```

**等待用户回复，按以下逻辑执行：**

- **用户回复"是"**：
  - 执行命令：`openclaw skills install mingdata-dmp-auth`
  - **安装成功**：提示 `✅ 鉴权技能安装成功` → 继续 3.2
  - **安装失败**：展示以下内容后**终止流程**：
    ```
    ❌ 鉴权技能自动安装失败

    请前往 ClawHub 手动安装：
    👉 https://clawhub.ai/mingri26/mingdata-dmp-auth

    手动安装步骤：
    1. 打开上方链接
    2. 点击「Download」按钮
    3. 安装完成后重新发起本次请求
    ```
- **用户回复"否"**：提示 `已取消操作。如需继续，请先安装鉴权技能。` → 终止流程

### 3.2 检查凭证是否存在

鉴权技能安装完成后，检查API凭证配置状态：

- **凭证文件路径**：`~/.mingdata_dmp_credentials`
- **如果凭证不存在或不完整** → 展示凭证获取指引：

```
🔑 明日DMP API凭证获取指南

您需要先获取明日DMP的API访问凭证（Access Key 和 Secret Key），才能使用人群圈选功能。

📧 申请方式（二选一）：

方式一：邮件申请
- 发送开通申请至：product@mingdata.com
- 邮件主题：【明日DMP API开通申请】
- 邮件内容：请注明公司名称、联系人、联系方式及使用场景

方式二：在线表单申请
- 填写在线申请表单：https://doc.weixin.qq.com/forms/ANEAJwfLAAoADMAHwbhAPICNUE0vDRd8f#/fill
- 提交后等待审核通过（通常1-3个工作日）

🔒 凭证格式：
- Access Key：xxxxxxxxxxxxxxxx（约20位字符）
- Secret Key：xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx（约32-36位字符）

获取凭证后，请按以下格式提供给我：
Access Key: xxxxxxxxxxxxxxxxxxxx
Secret Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

- 用户提供AK/SK后，调用：`python3 scripts/setup_credentials.py <AK> <SK> [BASE_URL]`
- 再次运行 `python3 scripts/preflight_check.py` 验证凭证有效
- **如果凭证有效** → 进入 Step 1（需求解析）

### 3.3 凭证加载优先级

脚本自动按以下顺序查找凭证：
1. 命令行参数 `--ak/--sk/--base-url`（最高优先）
2. 环境变量 `DMP_AK/DMP_SK/DMP_BASE_URL`
3. 配置文件 `~/.mingdata_dmp_credentials`（与批量打通/批量圈包/人群投放等技能共用）

> 注意：本技能**不通过逐条追问**收集AK/SK；缺失时引导用户运行scripts/setup_credentials.py一次性配置。

---

## 五、可跳过项与默认值（不阻塞产出）

以下信息**不是必填**。用户不提供时，仍继续输出候选标签、分组推荐与组合方案；只是在交付中标记为 `defaulted=true`。

- **最近活跃窗口**：默认 **近30天活跃**（PREFERRED）
- **城市层级**：默认 **优先一二线**（PREFERRED；含"一线/新一线/二线"，不做"只要一二线"的硬排除）
- **拉新排除口径**：默认 **不排除已有用户/已触达**（若后续提供排除包，再进入局部重算/重建）

> 注：只有在进入"计算量级/Overlap/创建人群包"等执行层动作时，才需要再确认执行口径（trackType/idTypes）。

---


## 六、端到端工作流（严格按Step 1→14顺序执行）

> 接口细节与结构约束请在执行前先阅读：references/api_reference.md（避免凭空猜参数）。
>
> 每一步都包含：产出物 + 下一步输入。
>
> **请求类型分流**：在进入工作流前，先判断请求类型：
> - 技能咨询（"有哪些功能""怎么圈人"）：展示概述和流程简介，不进入圈人流程
> - 标签查询（"有哪些美妆标签"）：执行Step 3+4召回标签，展示标签列表后询问是否创建人群
> - 任务状态查询（"查人群123456"）：调用scripts/query_crowd_task.py查询并展示结果
> - 创建人群请求：进入完整Step 1→14流程

### 执行口径确认（trackType / idTypes｜延后询问）

> **不要在一开始就问**。仅在你准备执行以下任一步时再询问并确认：
> - 计算 MUST 基准量级 |M|（Step 9）
> - 计算 Overlap（MUST∩可选）（Step 10）
> - 创建最终组合人群（Step 14）
>
> 询问时需说明用途：用于"计算量级/Overlap，并创建最终人群包"。
>
> 默认推荐（用户可一键确认）：
> - trackType：MOBILE（默认）
> - idTypes：**MD5_OAID**（默认勾选），可选加 MD5_IMEI、MD5_IDFA
>
> 若用户选择 PC/OTT：
> - PC：MZID（默认勾选）
> - OTT：MD5_MAC（默认勾选）

---

### Step 1：需求解析 → 10维 Schema

- **目标**：把用户自然语言映射到 10维 Schema（解析框架，不是问卷）。
- **10维口径（统一术语）**：行业、品类、人口属性（性别/年龄）、地域、兴趣、行为、场景、生活方式、活跃度、KOL-KOC
- **产出字段要求**：Schema JSON 只填用户明确表达的维度；未提及的不填；模糊词无法稳定转译则留空并标注 defaulted=true/false。
- **产出**：Schema JSON（只填用户说过的；模糊词转译失败则留空）。
- **规则**：用户没说的不填；objective 缺失可默认但需标记 defaulted=true。

详见：references/03_Schema解析规范.md

---

### Step 2：需求确认（READY / NEED_CLARIFICATION / BLOCKED）

- **目标**：向用户确认需求解析结果，判断信息是否足以进入召回。
- **动作**：
  - READY：展示已匹配到的维度概要，询问用户是否展开详情，确认后进入 Step 3
  - NEED_CLARIFICATION：展示已匹配维度+需确认的模糊维度，用户确认后进入 Step 3
  - BLOCKED：停止后续，要求用户补充基本人群描述

**展示原则**：
- ✅ **展示已匹配到的维度概要**：用简洁列表列出已解析到的维度（如"性别: 女、兴趣: 美妆个护、城市: 一线/二线"），让用户快速确认解析是否正确
- ✅ **提供展开选项**：用户可选"展开"查看详细的10维Schema解析，或"确认"直接进入下一步
- ❌ 禁止默认展开完整Schema表格
- ❌ 禁止重复展示用户原话

**READY话术模板**：
```
📋 需求解析完成，已匹配到以下维度：
• 性别: 女
• 核心兴趣: 美妆个护
• 城市级别: 一线/二线
• 年龄: 18-34（默认推荐）
• 活跃度: 近30天（默认推荐）

是否需要展开查看详细解析？
- 回复"确认" → 直接进入标签召回
- 回复"展开" → 查看完整维度解析
```

**NEED_CLARIFICATION话术模板**：
```
📋 需求解析完成，已匹配到以下维度：
• 性别: 女
• 核心兴趣: 美妆个护
• 城市级别: 一线/二线

🤔 以下维度需要您确认：
• 年龄: 推荐18-34岁（"精致女孩"行业常用口径）
• 活跃度: 推荐近30天活跃（"最近比较活跃"默认理解）

| 选项 | 操作 |
|------|------|
| **A** | 采用推荐，继续 |
| **B** | 修改 → 告诉我调整方向 |
| **C** | 不采用 → 仅保留已明确条件 |

请回复A/B/C~
```

详见：references/04_完整性判断与追问规范.md（含默认推荐机制）

---

### Step 3：获取可用标签池（统一为在线）

**统一方式（在线）：每次都调用 tag/list 接口获取标签池**

- **默认行为（已更新）**：同时拉取 **明略标签(tagType=1)** + **合作伙伴标签(tagType=3)** 并合并为一个 tag_pool，用于后续统一召回与分组推荐。
- 如需只拉取单一标签源，可在执行脚本时指定 tagType（单选或多选均可）。
- **脚本**：`python3 scripts/query_tag_list.py` 调用 DMP `tag/list` 接口
- **硬约束（已验证）**：候选标签必须来自 `tag/list` 且仅保留 **`isDirectory=1`** 的标签用于组合定向。
- **isDirectory 语义（已验证）**：
  - `isDirectory=1`：可用于组合定向的标签（覆盖“大类→叶子”）
  - `isDirectory=0`：纯分类目录/维度节点（不可用于组合定向）
- **说明**：不再使用离线标签池作为候选来源（避免租户权限/标签下线/口径差异导致创建失败）
- **产出**：tag_pool（tagId/tagName/parentId/tagType/isDirectory）

> 《标签指标表/画像表》仅用于后续 Step 5 的画像补全与工程质量过滤，不再作为候选标签池。

**⚠️ 错误处理**：如果tag/list接口调用失败，立即向用户说明：
```
❌ 无法连接DMP标签服务（可能是网络问题或凭证权限不足）

您可以选择：
- A. 我重试一次
- B. 如果您有离线标签指标表，可以提供给我使用
- C. 取消本次操作

请回复A/B/C：
```
禁止跳过标签池获取直接编造标签。

---

### Step 4：标签召回与相似度匹配（确定性TF-IDF，零依赖可复现）

- **目标**：在 tag_pool 内高召回候选标签（TopK），并为每个候选打 similarity_score（0~1，round6）。

**⛔ 查询词构造强制规范（保证端到端确定性）**：
AI助手**禁止手动构造query列表和boost-words**，必须通过 scripts/build_queries.py 脚本根据Step 1解析出的Schema确定性生成：

1. 将Step 1解析的Schema（含demographics/location/interest/activity及_raw_text）写入schema.json
2. 调用：`python3 scripts/build_queries.py --schema schema.json --synonyms references/synonyms_map.json --out queries.json`
3. 使用输出的queries.json作为scripts/tag_semantic_search.py的输入：
   `python3 scripts/tag_semantic_search.py --tags tag_pool.json --query-file queries.json --boost-words-json queries.json --boost-value 0.03 --top-k 60 --threshold 0.15 --out data/run/candidates.json`
4. scripts/tag_semantic_search.py现已支持直接读取scripts/build_queries.py输出的JSON格式（--query-file和--boost-words-json参数）

**确定性保证**：
- scripts/build_queries.py内置了维度值→标签查询词的确定性映射表（GENDER_MAP/AGE_MAP/CITY_MAP/ACTIVE_MAP/INTEREST_EXPAND）
- references/synonyms_map.json中定义的模糊词（如"精致女孩""宝妈""高净值"）也会自动扩展
- queries和boost_words按固定规则排序（长度降序→字典序升序）
- 输出包含query_hash和schema_hash，用于版本追踪
- **同Schema + 同synonyms_map → 同query_hash → 同召回结果**，字符串级一致

### Step 4.5：关键维度兜底召回（ensure_key_dimensions）

> 目的：防止“性别/年龄/城市级别”等**关键互斥维度**因语义召回TopK截断、短标签相似度劣势等原因被漏召回/漏展示。

**执行方式（自动化脚本）**：

```bash
python3 scripts/fallback_key_dimensions.py \
  --candidates data/run/candidates.json \
  --tag-pool data/run/tag_pool.json \
  --schema data/run/schema.json \
  --out data/run/merged_candidates.json
```

脚本自动完成：
1. 从Schema中检测目标性别/年龄段/城市级别
2. 检查Step 4召回结果中是否已包含这些维度的标签
3. 缺失时从tag_pool（仅isDirectory=1）按配置化规则（关键词+正则）兜底召回
4. 给兜底标签赋予合理similarity（性别0.95/城市0.88-0.90/年龄0.82-0.88）
5. merge去重，为所有标签补充`recall_source`字段

**执行顺序（强制，不得跳步）**：

```text
Step 4 语义召回 candidates.json
→ Step 4.5 fallback_key_dimensions.py → merged_candidates.json
→ Step 5 统一画像补全（兜底标签同样补fill_rate/coverage_rate/eng_score/dimension/category）
```

**硬约束**：
1) **真值源不变**：兜底召回只允许基于 Step 3 的 tag_pool（来自 tag/list），禁止引入离线标签池作为兜底候选来源。
2) **可用性不变**：兜底召回只允许使用 `isDirectory=1` 的标签（可用于组合定向）。
3) **无硬编码tagId**：使用配置化规则（关键词/正则/名称白名单）匹配标签。
4) **兜底≠自动选中（红线）**：fallback_dict 召回的标签只进入候选池与展示层，**不得自动加入 MUST/PREFERRED/OPTIONAL，也不得在 Step 6 默认勾选**。
5) **兜底标签必须补全similarity**：禁止similarity=0的标签进入排序脚本（会被阈值过滤丢弃），应根据匹配意图赋予0.82~0.95的合理值。

**字段要求（合并后必须保留）**：
- 为所有候选标签补充 `recall_source` 字段：
  - `semantic`：来自 Step 4 TF-IDF 召回
  - `fallback_dict`：来自 Step 4.5 兜底召回

> 注意：短词归一化（如“女性→女”）只用于提升召回命中率，不决定最终分组归类；最终进入“性别组”必须以维度字段/层级规则为准。


- **TF-IDF方法（确定性保证：同输入→同输出，字符串级一致）**：
  1. 多Query并行检索（多路query覆盖不同表述，合并取max similarity）
  2. TF-IDF char n-gram(1~3) + cosine相似度（零依赖，纯Python实现）
  3. **核心词命中boost**：build_queries生成的boost_words命中标签名时加固定小增益（默认+0.03，上限1.0），缓解短大类词被细分标签压制
  4. **稳定特征选择**：按df降序→gram字典序升序，消除Counter.most_common()并列不稳定
  5. **稳定排序tie-break**：(-similarity, tagId)，tagId保证同分标签顺序永远一致
  6. **文本归一化统一**：统一_normalize()函数，固定正则保留中文/字母/数字/下划线
  7. **tag_pool版本化**：输出tag_pool_hash（MD5前12位），同一hash下结果完全可复现

**确定性验收标准**：同一Schema + 同一tag_pool + 同一脚本版本，连续运行3次，每个tagId的similarity必须完全一致（精确到6位小数）。

详见：references/05_标签召回与语义匹配.md

---


### Step 5：标签画像补全（查《标签指标表》，四级匹配策略）

- **目标**：为候选标签补齐填充率、覆盖度、维度(dimension)、类目(category)、工程分(eng_score)等，用于工程质量过滤与分组排序。
- **输入**：Step 4 语义召回 + Step 4.5 兜底召回 merge 去重后的 `merged_candidates.json`（兜底候选也必须补画像，禁止出现“兜底标签缺画像”的展示）。
- **方法**：按四级匹配策略与《标签指标表》LEFT JOIN：
  1. **id_exact**：tagId精确匹配（优先级最高）
  2. **name_exact**：标签名完全相等
  3. **norm_exact**：归一化名称匹配（去括号内容/去标点/去"岁"字后缀后相等或互为子串，解决"美妆个护"≠"美妆个护（大类）"问题）
  4. **fuzzy**：TF-IDF字符n-gram模糊匹配（低于threshold标记MISSING）
- **自动处理**：百分比默认转为0~1（无需手动加参数）；audience_size若Excel数据截断标记None。
- **eng_score 降级计算规则**（按可用指标自动降级，不等强依赖双指标齐全）：
  - fill_rate 和 coverage_rate 都有 → `eng_score = 0.5 × fill_rate + 0.5 × coverage_rate`
  - 只有 coverage_rate（如指标表仅提供大盘占比）→ `eng_score = coverage_rate`
  - 只有 fill_rate → `eng_score = fill_rate`
  - 都没有 → `eng_score = None`
- **profile_status 判定规则**：
  - 四级匹配命中且分数≥threshold → `profile_status = OK`（即使只有部分字段，如仅有大盘占比也标记为OK）
  - 未匹配到（fuzzy分数低于threshold）→ `profile_status = MISSING`，fill_rate/coverage_rate/eng_score/dimension/category 全部置 None
- **dimension/category 缺失兜底**：若指标表中无维度/类目字段，dimension、category 留空，Step 6 分组排序时通过标签名称关键词+category路径自动归类。
- **MISSING标签排序**：profile_status=MISSING 的标签在分组排序时降级到同语义分桶内OK标签之后，但仍正常展示供用户选择，不得剔除。
- **脚本**：`python3 scripts/tag_profile_enrich.py`（支持--match-threshold/--pct-to-decimal等参数）
- **产出**：candidate_tags_enriched（含fill_rate/coverage_rate/dimension/category/eng_score/profile_match_type）。

**⚠️ 错误处理**：画像指标表缺失时：
```
⚠️ 无法获取标签的填充率/覆盖率等画像指标（未找到标签指标表）
影响：排序将仅基于语义相似度，无法做工程质量过滤，可能包含低质量标签。

您可以选择：
- A. 继续（仅语义排序）
- B. 上传标签指标表后重新执行
- C. 取消

请回复A/B/C：
```

详见：references/06_标签画像补全与质量排序.md

---

### Step 6：质量过滤与分组推荐（按用户需求维度分组，不混排）

- **目标**：按用户的每个需求维度分别分组，组内独立排序，让用户清楚看到"每个需求点有哪些标签可选、质量如何"。
- **核心原则**：**语义决定"相不相关"，工程决定"能不能用"；标签按需求维度分组展示，不做MUST/PREFERRED/OPTIONAL大杂烩分层。**
- **规则（严格按顺序）**：
  1. **硬门槛过滤（仅可剔除以下三类标签，禁止扩大范围）**：
     - ❌ 不满足“可用于组合”条件的标签（isDirectory语义以接口定义为准；项目确认后在此处全篇统一为 isDirectory≠1 或 isDirectory≠0）
     - ❌ 明显矛盾标签（用户要女则排除男，用户要一二线则排除三四线/四线及以下）——仅限互斥对立标签，不包括"相关性偏弱"的标签
     - ❌ 通用无关标签（如纯父级目录标签"兴趣爱好""人口属性"等无实际定向意义的大类目录节点）
     - ⛔ **禁止剔除规则**：不得因为"看起来不相关"或"和核心需求有偏差"就剔除标签（如运动消费、房产消费等消费力标签，即使语义分不高也属于消费力维度候选，应保留展示让用户选择）。只有上述三类可以剔除，其他一律保留展示。
  2. **按需求维度分组**：性别/年龄/城市级别/核心兴趣/消费力/职业/活跃度/其他兴趣（基于画像表dimension字段+category路径+名称关键词自动归类）。**子类目归并规则**：如果某标签的category路径包含核心兴趣大类名（如category包含"美妆个护"），则该标签及其子标签（↳）必须归入"核心兴趣"组，不得归入"其他兴趣"。
  3. **组内确定性排序**：语义分桶(±0.05)→有画像(OK)优先于MISSING→大类标签优先于细分标签(↳)→工程分降序→精确语义分→tagId升序兜底
  4. **核心维度缺口检测**：性别/年龄/城市级别/核心兴趣若候选为空，输出⚠️缺口提示；同时需检查标签池中是否真的不存在该维度标签（如活跃度标签可能整个标签池都没有），并在缺口提示中说明原因（"标签池中无该维度标签" vs "有标签但相似度未达阈值"）
  5. **细分标签标记(↳)**：品牌线(-欧美/-日韩/-大众)、价格段、高兴趣度后缀(-高)、具体子品类/功效词
- **脚本**：`python3 scripts/rank_candidates.py`（支持--core-interest/--core-group-name/--required-dims/--exclude/--top-per-group/--table-format等参数）
- **--table-format 参数说明**：
  - `markdown`（默认）：输出Markdown `|---|` 表格，适合支持Markdown的渠道
  - `box`：Unicode框线表格（┌─┬─┐），适合Markdown渲染不稳定的文本渠道
  - `card`：输出适合 Octo Display Card 消费的JSON（精简列+短来源名+自动名称简化），同时打印框线表格到stdout。AI解析CARD_DATA JSON后应使用 `octo_send_display_card` 发送真正的表格卡片。
- **--core-interest参数规范**：必须传入核心兴趣的**大类名+主要子类名**（逗号分隔），如 `"美妆个护,护肤,彩妆"`，不能只传大类名。因为标签池中部分兴趣标签的category路径是二级类目名（如"彩妆品类""护肤调性"）而非一级大类名（"美妆个护"），需要同时传入子类关键词才能正确归组。
- **--exclude参数使用规范**：只允许传入真正互斥矛盾的标签ID（如男/低消费/三四线），禁止传入"相关性弱但不矛盾"的标签ID。不确定是否矛盾时，宁可保留展示也不要排除。
- **缺口检测验证规范**：如果required_gaps提示某维度缺口，必须额外查询tag/list确认该维度标签是否真的不存在，区分"标签池无该维度"和"召回阈值过高未命中"两种情况，并在展示时如实告知用户原因。
- **展示格式**：

**渠道适配原则**：
  - **Octo 渠道使用 Display Card**：在Octo中Step 6/7/10/12/13等所有结构化展示环节，必须使用 `octo_send_display_card` 发送展示卡片，禁止用纯文本框线表格或大段Markdown表格（Octo对Markdown表格渲染不稳定，且长表格可读性差）。
  - **非Octo渠道（普通文本/IM）**：使用**带序号的简洁文本列表**呈现，禁止使用Markdown表格或Unicode框线表格，格式示例：
    ```
    【Overlap结果】MUST基准2722万
    1. +彩妆 → 780万（留28.7%）✅推荐
    2. +高消费 → 538万（留19.8%）✅可选
    3. +白领 → 92万（留3.4%）❌太小
    
    【方案选择】
    A. 扩展型（MUST only）→ 2722万，大曝光拉新
    B. 精准型（+彩妆）→ 780万 ⭐推荐
    D. 高价值型（+高消费）→ 538万，高ROI
    ```

**Octo卡片展示硬规则**：
  - ❌ **禁止把多个方案糅杂在一张卡片中**：每个方案必须独立发送一张卡片（heading+group+facts），避免信息堆砌导致可读性差
  - ❌ **禁止在卡片中使用Markdown表格**：Display Card的table组件在部分客户端渲染效果差，优先用 `facts`（key-value列表）代替表格呈现数据
  - ✅ **标签数据用facts组件**：每个标签/维度一个fact条目（label=标签名, value=量级/渗透率/建议），不要用table
  - ✅ **方案卡片独立发送**：推荐方案用good样式（绿色），其他方案用emphasis样式（灰色），每个方案单独发一张卡片
  - ✅ **Overlap总览先发一张**：用facts列所有可选标签的叠加效果，再逐张发方案卡片
  - 表格列精简：如需展示候选标签表，卡片中只保留核心字段（标签ID/名称/来源/相似度/填充率/覆盖率），来源简写「明」「合」
  - 合作标签名称简化："基本属性_居住城市级别_一线城市"→"一线城市"，"基础属性_年龄_25-34"→"25-34岁"（card格式自动处理）
  - 基础属性维度标签（性别/年龄/城市/消费/职业）不加↳；兴趣子类别（彩妆-大众、中国-护肤等）加↳
  - 分组分卡片：Step 6推荐分3张卡片：①标签叠加效果总览(facts) ②推荐方案(good) ③其他方案(emphasis)

**所有展示格式的必选字段**：标签ID/标签名称/来源（简写）/相似度/填充率/覆盖率。召回来源（recall_source）在卡片中不单独列列，但用于诊断。
  - 每组单独展示，大类在前↳细分在后。

> ⚠️ 禁止用工程分覆盖语义排序。覆盖率高的泛标签不应挤掉语义精准的窄标签。工程分仅在语义分桶内做微调。

**Step 6展示规则**：

**默认不展开候选标签表**。Step 6完成后，只向用户输出简要确认+是否展开的选择：

```
✅ 已从DMP标签库中召回{N}个候选标签，覆盖性别/年龄/城市级别/核心兴趣等维度。

是否需要查看候选标签详情？
- 回复"展开"：查看按维度分组的候选标签列表
- 回复"跳过"或"确认"：直接进入下一步，使用推荐组合
```

> ⚠️ **双来源标签展示**：核心维度（性别/年龄/城市级别）如果明略和合作伙伴都有对应标签，两个都会展示，标注来源（明略/合作），让用户自行选择。例如性别可能同时展示明略"女"和合作"基础属性_性别_女"两个标签。

**如果用户回复"展开"**：按维度分组展示候选标签（使用上述展示格式，标注明略/合作来源），展示完毕后附带三方标签推荐（调用match_third_party_tags.py脚本，见下方Step 6.5的「展开模式展示」），然后进入Step 7。
**如果用户回复"跳过"/"确认"**：跳过展开，但需检查是否匹配到三方标签：
- 匹配到三方标签 → 输出一句轻量提示（见下方Step 6.5的「快速模式提示」），然后进入Step 7
- 未匹配到 → 直接进入Step 7

> ⚠️ 展开候选标签的目的是让用户看到"有哪些标签可选"，不是让用户在此步骤选择标签。标签选择在Step 7进行。

### Step 6.5：三方标签推荐

> **目的**：DMP接口标签（tag/list）并非全部可用标签。还有一些三方标签（秒针OTT/剧目、OTA出行旅游、京东品类等）暂不在接口标签池中，但可通过申请开通使用。
> 根据用户是否展开候选标签，采用两种展示模式：
> - **展开模式**：用户主动看标签详情，直接在候选表下方列出匹配到的三方标签+申请链接
> - **快速模式**：用户跳过标签详情，如果有匹配三方标签只给一句提示，感兴趣可再展开；没匹配则不提

**执行规则**：
1. **接口标签匹配不变**：Step 3-6的标签召回、画像补全、分组推荐仍然只基于 DMP `tag/list` 接口返回的标签，三方标签**不参与**接口标签的召回/排序/组合。
2. **三方标签数据源**：读取 `assets/third_party_tags.json`（结构化目录）和 `assets/三方标签.xlsx`（原始文件）。三方标签共4类来源：
   - **秒针OTT标签**：OTT端家庭结构（独居/老两口/三代同堂等7类）、OTT行业偏好（食品饮料/美妆/3C/母婴/汽车等）、OTT媒体偏好（电视媒体/硬件厂商）、OTT城市等级
   - **秒针剧目偏好标签**：动漫（11类）、电视剧（23类）、综艺节目（37类）的内容偏好
   - **出行旅游类标签（OTA）**：去哪儿/艺龙/同程/携程/途牛的酒店、民宿、海外酒店、跟团游等浏览/下单/付费/取消行为
   - **京东品类标签**：57个一级品类、数百个二级品类、数千个三级品类，支持浏览/加购/购买等行为+品牌/店铺/价格/时间/频次维度
3. **匹配逻辑**：
   - **必须使用脚本**：调用 `python3 scripts/match_third_party_tags.py --tp-tags assets/third_party_tags.json --schema data/run/schema.json --out data/run/third_party.json` 获取匹配结果，禁止手动遍历third_party_tags.json匹配
   - 脚本会自动从Schema的结构化字段（gender/city_tier/interest/consumption/industry/category）和raw_text提取关键词，精确匹配4类三方标签
   - OTT相关需求（家庭场景/大屏/智能电视等）→ 推荐秒针OTT标签
   - 内容/影视/节目偏好需求 → 推荐秒针剧目偏好标签
   - 旅游/酒店/出行/OTA需求 → 推荐出行旅游类标签
   - 电商购物/具体商品品类需求 → 推荐京东品类标签
   - 若脚本返回 total_matches=0（未匹配到任何三方标签），则**不展示**三方标签推荐区块（避免无效推荐）

#### 快速模式提示（用户回复"跳过"/"确认"且匹配到三方标签时）

在Step 7推荐组合之前，输出一句话：

```
💡 根据您的需求还匹配到了一些三方标签，如有需要可回复"查看三方标签"展开了解~
```

- 用户回复"查看三方标签"/"展开三方标签"等 → 切换到展开模式展示（下方详细列表+申请链接）
- 用户直接回复"确认"/"继续"等 → 忽略，进入Step 7

#### 展开模式展示（用户回复"展开"或快速模式下回复"查看三方标签"时）

在候选标签分组表格的**最下方**追加（不插入到接口标签分组中间），展示文案（固定模板，不得修改）：

```
📎 除了上述可供圈选的标签，以下三方标签也符合您的需求，如有需要请填写链接申请哦~
https://doc.weixin.qq.com/forms/ANEAJwfLAAoADMAHwbhAPICNQGdo8H7Gf#/fill

【匹配到的三方标签】
• 【{来源名}】{推荐标签描述}
• 【{来源名}】{推荐标签描述}
...
```

**Octo渠道展示**：使用 `octo_send_display_card` 发送一张独立卡片（style=emphasis），heading为"📎 更多三方标签推荐"，text为固定文案+链接，facts列匹配到的三方标签来源和描述。

**硬约束**：
- ❌ 三方标签**不得**带入Step 7-14的组合流程（不得作为MUST/PREFERRED/OPTIONAL/EXCLUDE，不得参与Overlap计算，不得创建人群包）
- ❌ 不得把三方标签和接口标签混在同一张表格中展示
- ❌ 未匹配到需求相关三方标签时，禁止强行推荐不相关的三方标签（包括快速模式下也不提示）
- ✅ 三方标签仅作为信息告知+申请入口，不影响主流程
- ✅ 推荐描述要具体到能满足用户需求的细分类目，不要只说"有京东标签"

详见：references/06_标签画像补全与质量排序.md

---

### Step 7：用户选择（MUST / PREFERRED / OPTIONAL / EXCLUDE）

- **目标**：在Step 6方向对齐的基础上，让用户基于完整画像指标，逐维度确定最终入选的标签集合。
- **与Step 6的区别**：Step 6是"方向对不对"（展示候选+画像，问方向是否正确），Step 7是"具体选哪些"（在带画像指标的标签表上加✅推荐/☐可选标记，让用户勾选）。**Step 7不得只列标签ID+名称让用户盲选，必须保留相似度/填充率/覆盖率/工程分等画像指标**。
- **交互方式**：按维度展示带勾选列的画像表，预标记AI推荐项（✅推荐/☐可选）；用户可以确认一键推荐、加选、去掉某些标签。
- **产出**：must_tags、preferred_tags、optional_tags、exclude_tags。

- **重要说明（避免误解）**：
  - Step 7 的选择会产出四类标签：MUST / PREFERRED / OPTIONAL / EXCLUDE。
  - **进入 Step 9 时，会先“仅用 MUST”创建基准人群 M（锚点）并计算 |M|**；PREFERRED/OPTIONAL 暂不并入基准。
  - 随后在 Step 10 的 Overlap 中，将 PREFERRED/OPTIONAL 作为候选条件逐个计算 |M∩x|，用于生成“精准/扩展/综合”方案；最终在 Step 14 再按你确认的方案把 PREFERRED/OPTIONAL 组合进最终人群。

| 分层 | Step 9 基准M是否生效 | Step 10 Overlap是否参与 | Step 14 最终创建是否可能生效 |
|---|---|---|---|
| MUST | 是 | 作为锚点 | 是（必然） |
| PREFERRED | 否 | 是（逐个评估） | 是（按方案/确认） |
| OPTIONAL | 否 | 是（逐个评估） | 可能（按方案/确认） |
| EXCLUDE | 否 | 视口径 | 是（最终生效） |

- **展示规则**：
  - ❌ **禁止默认展开逐维度画像表**：不要一上来就列出所有维度的标签表让用户勾选
  - ✅ **直接给出推荐组合**：AI根据用户需求和标签画像，自动生成推荐组合，简洁展示给用户确认
  - ✅ **推荐组合展示格式**：用简洁文本列出MUST/PREFERRED分层，附标签ID和名称，不列画像指标表
  - 如果用户想看详细画像指标，可以回复"展开标签详情"查看

**一键推荐话术模板**：
```
📋 基于您的需求，推荐以下组合：

【MUST（必须满足）】
• 女(15705) AND 美妆个护(15564)
• (18-24岁(126143) OR 25-34岁(126141))
• (一线城市(34080) OR 二线城市(34082))

【PREFERRED（建议满足，可调整）】
• 无 / 或可加选：彩妆(15653)、高消费(34062)等

回复：
• "确认" → 采用推荐组合继续
• "加选xxx" → 加选某个标签
• "去掉xxx" → 去掉某个标签
• "展开标签详情" → 查看所有候选标签的画像指标
• "自定义" → 告诉我您要的具体组合
```

> **关键设计原则**：
> 1. Step 7默认只展示推荐组合（标签ID+名称+分层），不展示完整画像表
> 2. 用户可以回复"展开标签详情"查看画像指标，但不作为默认行为
> 3. 用户确认推荐组合后直接进入Step 8（冲突检测），不需要逐维度勾选
> 4. 如果用户在Step 6已展开过候选标签，Step 7仍只给推荐组合，不重复展示画像表
> 5. MUST/PREFERRED分层遵循「用户明确度优先」原则（详见references/07）：用户明确要求的维度（城市/年龄/育儿状态等）必须进MUST，禁止按维度类型硬编码

详见：references/07_用户选择与优先级.md

---

### Step 8：标签冲突检测（用户选择后必做，静默执行）

- **目标**：检测明显互斥/矛盾选择（例如"一线城市"AND"三线城市"），避免创建后量级为0。
- **展示规则**：
  - ✅ **默认静默执行**：冲突检测在后台完成，不向用户展示检测过程和结果
  - ✅ **仅在发现冲突时才通知用户**：如果检测到互斥标签或父子冗余，才输出提示并询问用户如何处理
  - ❌ 禁止默认展示"无冲突"的确认信息（如"性别互斥✅/年龄OR✅"等）
  - 如果没有冲突 → 直接静默进入Step 9

- **动作**：检测互斥/矛盾/父子冗余；仅在发现问题时才提示用户
- **产出**：conflict_report（如有冲突才展示，无冲突则静默通过）

详见：references/13_标签冲突检测.md

---

### Step 8B：标签逻辑处理（静默执行，仅冲突时展示）

- **目标**：检测逻辑矛盾，处理父子标签，确认标签组合逻辑正确。
- **展示规则**：同Step 8，默认静默执行，仅发现问题时才提示用户。
- **动作**：
  1. **父子标签处理**：检测父类已覆盖子类的冗余情况，仅在发现时才建议用户处理
  2. **EXCLUDE与INCLUDE冲突**：检测排除标签和必选标签的矛盾
  3. **OR组合不冲突**：同维度多标签OR是正常扩量，不标记为冲突
  4. **仅提示，不擅自修改MUST**
- **产出**：处理后的must_tags/preferred_tags/optional_tags + conflict_report（仅冲突时展示）

---

### Step 8.5：执行口径确认（⛔强制，禁止跳过）

- **目标**：在调用创建人群API前，必须向用户确认终端类型(trackType)和设备ID类型(idTypes)
- **⛔强制规则**：
  - ❌ 未询问用户trackType/idTypes，**禁止**调用 create_must_baseline.py / create_combined_crowd.py
  - ❌ 不得擅自用默认值直接创建人群
  - ✅ 必须先执行 `python3 scripts/confirm_execution_params.py` 读取输出提示，然后向用户询问
  - ✅ 用户明确回复口径后（或回复"确认"采用默认），才可进入Step 9
- **默认推荐**（用户回复"确认"时使用）：
  - trackType: MOBILE
  - idTypes: IDFA, OAID, MD5_IDFA, MD5_OAID, MD5_IMEI
- **其他端口径**：PC→MZID；OTT→MD5_MAC
- **脚本**：`python3 scripts/confirm_execution_params.py`（输出强制交互提示+默认参数JSON）

---

### Step 9：创建 MUST 基准人群 |M|

- **目标**：计算用户最终确认的 MUST 标签集合所构成的基准人群量级，得到 audienceId_M 与 |M|。
- **MUST定义（v2）**：MUST 由用户确认，**可来自任意维度**（不做"性别+兴趣"硬编码）。PREFERRED/OPTIONAL 不进入本步骤的基准人群创建（除非用户把它们提升为 MUST）。
- **逻辑规则**：同维度 OR、跨维度 AND；EXCLUDE 不进入基准人群 M（EXCLUDE 在最终创建/或单独排除逻辑中生效）。
- **前置**：此步骤前需确认执行口径（trackType/idTypes），见"执行口径确认"章节。

**创建方式选择（支持多组）：**

根据MUST标签的组合逻辑判断使用哪种创建方式：

| 场景 | 条件 | 创建方式 | 说明 |
|------|------|---------|------|
| 单组AND/NOT | 所有MUST标签之间只有AND/NOT关系（无组间OR） | MCP工具 `create_combined_audience` | 旧格式兼容，直接传rules_json |
| 多组AND/OR/NOT | MUST标签需要分组，组间有OR/NOT关系（如"(女 AND 美妆) OR (女 AND 护肤)"） | 批量圈包脚本 `create_combine_batch.py --groups-json` | v1.4 group层级格式 |

**单组创建（MCP工具）：**
- 直接调用 `DMP_MCP__create_combined_audience`，传旧格式 rules_json
- 格式：`[{"audiences":[],"tags":[标签1]}, {"op":"and"}, {"audiences":[],"tags":[标签2]}, ...]`
- 适用于：所有标签跨维度AND、同维度OR的场景（覆盖90%的MUST基准创建）

**多组创建（脚本）：**
- 调用批量圈包脚本：
```bash
cd ~/.openclaw/skills/明日dmp批量圈包 && python3 scripts/create_combine_batch.py \
  --audience-name "{人群名称}" \
  --track-type MOBILE \
  --id-types MD5_OAID \
  --groups-json '[{"tags":[15705,15564],"audiences":[],"op":"or"},{"tags":[15652],"audiences":[],"op":"noop"}]'
```
- 适用于：组间OR并集、组间NOT差集等v1.4多组场景
- 脚本内部会构建v1.4的 `data:[{op, group:[{op, rule}]}]` 格式

- **严格状态码**：轮询等待status=1（成功）才读取audienceAmount；status=0/2/3均不读取量级。
- **产出**：audienceId_M、|M|（精确值）。

**⚠️ 错误处理**：如果MUST量级为0或极小（<1000），提示调整标签选择。

---

### Step 9.5：是否需要Overlap分析？（关键判断节点）

M基准创建成功后，**根据用户意图决定是否进入Overlap分析**，不是默认必做：

| 用户意图 | 是否需要Overlap | 下一步 |
|---------|----------------|-------|
| 明确"就要MUST only，直接创建" | ❌ 不需要 | 进入 Step 9.5.1 生成 data.json（MUST）→ Step 13 确认 → Step 14 创建 |
| 明确"全部/部分PREFERRED都加上，直接创建" | ❌ 不需要 | 进入 Step 9.5.1 生成 data.json（MUST+PREFERRED）→ Step 13 确认 → Step 14 创建 |
| 需要推荐方案/看可选标签效果/做扩缩量决策 | ✅ 需要 | 进入Step 10 |
| 需要做同维度OR扩量 | ✅ 需要（M∩Optional必做+按需OR对） | Step 10 + 按需Step 10B |

**询问话术（仅当用户意图不明确时）**：
```
MUST基准人群已创建：{M_audienceId}，量级{M_amount}。

您希望：
- A. 直接创建人群（就用MUST标签/已选全部标签）
- B. 看Optional标签效果和组合方案推荐（需要计算Overlap）

请回复A/B：
```

---

### Step 9.5.1：直接创建分支的数据生成（补齐 Step 14 输入）

> 适用场景：用户明确选择“仅用 MUST 直接创建”或“把全部/部分 PREFERRED 加上直接创建”，且不进入 Overlap。

- **目标**：在不进入 Step 10–12 的情况下，生成可用于创建最终组合人群的 `data.json`（组合规则数据结构），并进入 Step 13 进行强制确认。
- **输入**：用户确认的 MUST /（可选）PREFERRED / EXCLUDE。
- **规则**：
  - 同维度 OR、跨维度 AND。
  - EXCLUDE 必须生效。
  - 不得把“系统默认推荐”当作用户确认结果；以 Step 7 用户最终选择为准。
- **产出**：`data.json`（或等价结构），以及可读逻辑表达式。

> 说明：该步骤只负责生成创建所需数据与规则表达，不做 Overlap、不做扩缩量分析、不做方案推荐。

- **下一步**：进入 Step 13（参数确认卡点）→ 用户确认后进入 Step 14 创建。


分两层：

#### 10A：MUST vs Optional 渗透分析（进入 Overlap 分支时必做）
- **目标**：计算每个Optional标签x在M中的渗透率 r_x = |M∩x|/|M|，回答"加这个标签会剩多少人"
- **脚本**：`python3 scripts/analyze_overlap.py --audience-id-m <id> --amount-m <amt> --optional optional.json --track-type MOBILE --id-types MD5_OAID --out overlap.json`
- **临时包数量**= Optional标签数（通常5-10个），可接受
- **产出**：每个x的r_x（渗透率）、交集量级，标注exact
- **不创建包的对（仅限可逻辑判定者）**：
  - 互斥对：r=0（无需建包）
  - 父子/祖先对：必须区分方向（禁止统一写 r=100%）：
    - 若 Optional 是 MUST 的父类/祖先（Optional 覆盖 MUST）→ M∩x = M，r=100%（可逻辑判定，无需建包）
    - 若 Optional 是 MUST 的子类/后代（Optional 收窄 MUST）→ r<100%，通常需按需建包计算（exact）或在项目允许时做保守估算（estimated）

#### 10B：同维度OR候选对（按需，1-3对）
- **触发条件**：当扩缩量分析（Step 11）或用户提出同维度OR扩量需求时，才额外计算
- **通过--or-pairs参数指定**：`--or-pairs "15689:15690,34080:34083"`

---

### Step 10：标签关系分析与 Overlap 计算（仅在进入 Overlap 分支时执行）

> 说明：仅当 Step 9.5 选择进入 Overlap 分支时，才执行 Step 10。
> 若 Step 9.5 选择“直接创建”，则跳过 Step 10–12。

- **不默认全量计算**，只算实际要OR的那几对
- **产出**：指定对的交集量级，用于判断OR增量

#### 不计算
- **跨维度标签对**：不建包（改变人群方向，不自动推荐）
- **冗余判断对**：用覆盖率/相似度/父子逻辑判断，不建包

**Overlap报告展示格式**：

**Octo渠道**：先发一张Overlap总览卡片（facts组件列所有标签叠加效果），再逐张发方案卡片（每方案独立一张）

**非Octo渠道**：用带序号简洁文本：
```
📊 MUST基准：|M| = {XXX}万

标签叠加效果：
1. {标签名} → {XX}万（留{XX%}）{建议✅/⚠️/❌}
2. {标签名} → {XX}万（留{XX%}）{建议}

关键发现：
- {洞察1}
- {洞察2}
```

详见：references/08_Overlap计算.md

---

### Step 11：扩缩量分析报告（独立）

- **目标**：基于Overlap数据输出分析结论，不直接生成方案。回答：
  - 哪些标签高度重合（AND后几乎不缩量）
  - 哪些标签收窄适中（适合AND精准化）
  - 哪些标签收窄强烈（人群过小需谨慎）
  - 同维度OR扩量能增多少（如有10B数据）
- **脚本**：`python3 scripts/analyze_scale.py --overlap overlap.json --out scale_report.json --text scale_report.txt`
- **产出**：结构化分析JSON + 可读文本报告，供Step 12生成方案使用

---

### Step 12：生成组合方案（4种）

- **目标**：基于MUST/PREFERRED/OPTIONAL分层+Overlap+扩缩量分析，生成4套方案供选择。
- **脚本**：`python3 scripts/generate_plans.py --must must.json --preferred preferred.json --optional optional.json --overlap overlap.json --amount-m <M> --out plans.json`
- **4种方案定义（v2，术语一致、无维度硬编码）**：
  - **扩展型（MUST-only）**：仅使用“用户确认的全部 MUST”生成方案；同维度 OR、跨维度 AND；量级=|M|（exact）。
  - **精准型（MUST + PREFERRED）**：MUST + 用户确认要加入的 PREFERRED；其中同维度 OR、跨维度 AND（不是“全部 AND”）；量级优先给出 estimated，若已做 Overlap 可结合结果给更精细判断。
  - **综合型（MUST + 核心 PREFERRED + 少量 OPTIONAL）**：在 MUST 基础上加入关键 PREFERRED，并按 Step 10A/Step 11 的收窄强度选择 1–2 个 OPTIONAL（通常收窄适中）加入 AND。
  - **扩量型（同维度 OR 扩量）**：在 MUST + 少量关键 PREFERRED 的基础上，通过同维度 OR 扩量（如年龄段 OR、城市级别 OR）；如已做 Step 10B，则引用其增量判断；禁止自动生成跨维度 OR（会改变人群方向）。
- **⛔ 不自动生成跨维度OR方案**（会改变人群方向；若用户手动要求需确认业务语义）
- **产出**：可读逻辑 + API data JSON + 预测量级（标注exact/estimated）

---

### Step 13：用户确认/修改

- **目标**：用户确认最终方案。
- **⚠️ 参数确认卡点（强制执行）**：在Step 12生成方案后，必须展示方案对比+参数确认表格，等待用户明确确认后才能进入Step 14。

**方案展示与确认话术**：

**Octo渠道**：每个方案独立发一张Display Card（推荐方案用good样式绿色，其他用emphasis灰色），卡片内含：
- heading：方案编号+名称+推荐标记
- group：组合逻辑描述（用text）
- facts：量级（精确/estimated标注）、适合场景、推荐理由
- copy按钮：快速回复“选择方案X”

最后发一张参数确认卡片，列出平台类型/ID类型/人群名称等。

**非Octo渠道**：用带序号的简洁文本：
```
【方案选择】
A. 扩展型（MUST only）→ 2722万 | 大曝光拉新
B. 精准型（+彩妆）⭐→ 780万 | 核心用户精准拉新
D. 高价值型（+高消费）→ 538万 | 高ROI投放

【执行参数】
平台：MOBILE | ID：MD5_OAID,OAID | 名称：自动生成

请回复A/B/D或自定义组合：
```

**🔴 强制规则**：
- 必须等待用户回复明确的"确认"、"创建"、"用方案X"等词
- 未确认前**禁止**调用创建API
- 用户要求修改某参数 → 修改后重新展示
- 用户说"随便起个名字" → AI自动生成名称（格式：`TP组合_{维度简述}_{YYYYMMDD}`），展示给用户确认

**修改规则**：
- 改需求 → 回到 Step 1/2
- 改单标签 → 局部重算（尤其 MUST 变化需重算 |M| 与所有 overlap）

详见：references/10_异常回退与局部重算.md

---

### Step 14：创建最终组合人群（执行层）

- **目标**：输出最终人群包创建参数（name/trackType/idTypes/data），并调用 DMP 创建。
- **前置条件**：用户已在Step 13明确确认参数。

**创建方式选择（支持多组）：**

与Step 9相同的逻辑，根据最终方案判断使用哪种创建方式：

| 场景 | 创建方式 | 说明 |
|------|---------|------|
| 单组AND/NOT | MCP工具 `create_combined_audience` | 旧格式兼容 |
| 多组AND/OR/NOT | 批量圈包脚本 `create_combine_batch.py --groups-json` | v1.4 group层级 |

**单组创建（MCP工具）：**
```python
DMP_MCP__create_combined_audience(
    name="人群名称",
    track_type="MOBILE",
    id_types="MD5_OAID,OAID",
    rules_json='[{"audiences":[],"tags":[15705]},{"op":"and"},{"audiences":[],"tags":[15564]},...]'
)
```

**多组创建（脚本）：**
```bash
cd ~/.openclaw/skills/明日dmp批量圈包 && python3 scripts/create_combine_batch.py \
  --audience-name "人群名称" \
  --track-type MOBILE \
  --id-types MD5_OAID,OAID \
  --brands "" \
  --groups-json '[{"tags":[15705,15564],"audiences":[],"op":"and"},{"tags":[126143,126141],"audiences":[],"op":"and"},{"tags":[34080,34082],"audiences":[],"op":"noop"}]'
```

- **注意**：combine/create 的 data 结构与上限必须校验（rule≤50、单rule≤100、最后一组op必须为noop、组数≤10）。
- **创建成功后立即检查任务记录技能（必须检查，禁止跳过）**：

  检查 `~/.skills/skill-logger/` 或 `~/.skills/skill-logger-v2-global/`：
  - **已安装** → 自动记录任务信息，告知用户"✅ 任务已自动记录到历史"
  - **未安装** → 提示：
  ```
  💡 检测到您尚未安装【任务记录技能（skill-logger）】
  该技能可自动记录每次任务的ID、名称、时间和参数，方便后续查询追溯。

  是否自动下载并安装？
  - 是 - 立即安装并记录
  - 否 - 本次跳过（不影响主流程）

  请回复是/否：
  ```

**成功结果展示话术**：
```
✅ 组合人群创建任务已提交！

┌──────────┬──────────────────┐
│ 任务ID    │ {audienceId}     │
│ 人群名称  │ XXX              │
│ 人群类型  │ 组合人群          │
│ 状态      │ 计算中            │
└──────────┴──────────────────┘

⏱️ 预计5-30分钟完成计算。您可以：
1. 稍后告诉我"查询人群任务{audienceId}"查看状态
2. 人群计算成功后，可以继续：
   📊 人群洞察 - 对该人群做多维度画像分析
   📢 人群同步/投放 - 将人群包同步到广告平台
```

**失败结果展示话术**：
```
❌ 人群创建失败

| 项目 | 详情 |
|------|------|
| 错误信息 | {error_msg} |
| 可能原因 | {根据错误码给出原因} |
| 建议操作 | {对应修复建议} |

是否需要调整后重试？
```

详见：references/09_组合策略与API规则落地.md

---


## 七、前置规范（必须内嵌遵循）

- **鉴权**：通过调用鉴权技能（mingdata-dmp-auth）完成，URL query拼接ts/randStr/accessKey/sign；sign=MD5(ts+randStr+secret_key).upper；ts有效3分钟。
- **任务记录**：创建成功后必须检查skill-logger技能安装状态，并记录时间、环境、接口路径、关键输入（脱敏）、返回ID、状态、错误信息。
- **导出**：候选标签表、Overlap报告、最终规则JSON使用统一命名与导出入口（按项目规范）。

---

## 八、参考文档（references/）

| 文件 | 内容 |
|------|------|
| references/api_reference.md | DMP API端点、鉴权签名、请求/响应结构细节 |
| references/01_输入字段规范.md | 必填/可选输入字段定义 |
| references/03_Schema解析规范.md | 10维Schema结构与解析规则（以本技能v2口径为准） |
| references/04_完整性判断与追问规范.md | READY/NEED_CLARIFICATION/BLOCKED状态机与默认推荐机制 |
| references/05_标签召回与语义匹配.md | TF-IDF参数、boost策略、确定性保证细则 |
| references/06_标签画像补全与质量排序.md | 四级匹配策略、工程分计算、分组排序规则细节 |
| references/07_用户选择与优先级.md | MUST/PREFERRED/OPTIONAL/EXCLUDE分层规则 |
| references/08_Overlap计算.md | 重叠率/收窄率计算方法与批量创建策略 |
| references/09_组合策略与API规则落地.md | data JSON构造规则（noop/and/not、上限校验） |
| references/10_异常回退与局部重算.md | 用户修改后的最小影响范围回退策略 |
| references/12_量级预估.md | 基于fill_rate/coverage_rate的量级估算方法 |
| references/13_标签冲突检测.md | 互斥标签检测规则与提示策略 |
| references/synonyms_map.json | 模糊词→标准词映射表（用于默认推荐） |
| references/凭证获取指南.md | AK/SK申请方式与配置步骤 |
| references/技能安装与环境检查.md | 环境依赖与常见安装问题排查 |

---

## 九、常见问题

**Q: 和"明日dmp人群圈选"技能有什么区别？**
A: 明日dmp人群圈选覆盖6种圈选方式（组合/广告行为/APP/LBS/拓展/打通），适合快速创建、参数已知的场景。本技能专注于**组合人群**，提供更深入的标签探索：语义召回→画像补全→分组推荐→Overlap分析→多方案推荐，适合精细挑选标签、探索目标人群的场景。

**Q: 为什么要先展示候选标签让我确认方向？**
A: 自然语言和DMP标签之间存在语义鸿沟，AI的理解可能有偏差。先展示候选标签确认方向，可以避免后续方案建立在错误的标签基础上。

**Q: Overlap为什么只算MUST vs 可选，不计算所有标签两两之间？**
A: MUST是核心锚点（不可删除），所有可选标签都是在MUST基础上的收窄条件。计算M∩x就足够判断"加上这个标签后人群会收窄多少"，两两计算开销大且信息冗余。

**Q: MUST基准量级为0怎么办？**
A: 说明核心标签之间没有交集（矛盾条件）或标签权限问题。建议放宽MUST条件，将部分标签从MUST降级为PREFERRED/OPTIONAL，或回到Step 8检查冲突。

**Q: 创建任务后多久能完成？**
A: 组合人群通常5-30分钟计算完成。复杂组合（多标签+Overlap批量计算）可能更久。

---

## 十、禁止行为清单（AI助手必读——违反即视为执行错误）

1. ❌ **禁止编造tagId/标签名/量级/Overlap/覆盖度/填充率**——所有数据必须来自API或脚本输出
2. ❌ **禁止跳步**——必须严格按Step 1→14顺序执行，不得跳过任何步骤
3. ❌ **禁止跳过用户确认直接调用创建API**——Step 13参数确认表格是强制卡点，必须等待明确"确认"
4. ❌ **禁止跳过鉴权检查**——每次创建/查询前必须确认鉴权技能已安装、凭证有效
5. ❌ **禁止跳过任务记录检查**——Step 14创建成功后必须检查skill-logger安装状态（即使不安装也要走完询问流程）
6. ❌ **禁止用工程分覆盖语义排序**——覆盖率高的泛标签不应挤掉语义精准的窄标签；工程分只做门槛过滤和语义分桶(±0.05)内微调
7. ❌ **禁止擅自把TopN候选标签全部加入组合**——必须等用户逐个维度选择
8. ❌ **禁止擅自删除用户选择的MUST标签**——Step 8冲突检测只提示建议，不自动修改
9. ❌ **禁止擅自剔除非矛盾候选标签**——Step 6硬门槛过滤仅可剔除isDirectory≠1、明显互斥矛盾、通用无关三类标签；"相关性偏弱"不是剔除理由，消费力/兴趣等弱相关标签必须保留展示给用户选择
10. ❌ **禁止使用isDirectory≠1的标签**——只有目录标签可用于组合人群
11. ❌ **禁止在对话中明文展示AK/SK**——凭证属于敏感信息
12. ❌ **禁止一开始就追问trackType/idTypes**——执行口径必须延后到Step 9前才询问
13. ❌ **禁止遇到标签缺口不说明原因**——缺口提示必须区分"标签池本身无该维度标签"和"召回阈值过高未命中"两种情况，通过查询tag/list核实后如实告知
14. ❌ **禁止Step 7默认展开逐维度画像表**——Step 7默认只展示推荐组合（标签ID+名称+MUST/PREFERRED分层），不展示完整画像指标表；用户回复"展开标签详情"时才展示画像表
15. ❌ **禁止手动构造query列表或boost-words**——Step 4必须调用scripts/build_queries.py根据Schema确定性生成查询词，禁止AI自由发挥编写query列表，以保证端到端召回结果可复现