# 🧠 全息脑图生成模块

> 从属于 AHKB-CPS 统一系统。基于知识库或手动输入，生成升维全息思维导图。
> 🔴 **交互规则**：所有选项必须用数字编号展示，用户输入数字选择，**严禁使用 AskUserQuestion 工具**。

## 模块概述

阿色全息脑图（AHMM: Arthur's Holographic Mind Map）是按照大系统观原理开发的新型思维工具，用于升维思考。利用大模型自动生成全息脑图，帮您以系统的观点看世界，抓住事物的本质，透过表象和数据发现规律。

**输出能力：**

- **全息脑图 JSON** — 按 AHMM Schema 生成结构化数据，驱动 ahmm.html 可视化渲染
- **三个维度** — 核心概念（summary_block）、内部序参量（in_blocks × 11）、外部关联参量（out_blocks × 5）
- **KB 驱动 + 独立创作** — 可从知识库检索素材，也可完全自由生成
- **一键呈现** — 浏览器自动打开，全息脑图立即可视化交互

> 🔴 **路径约定**：本文中所有路径均相对于 AHKB-CPS 技能目录（即 `{skill_dir}`），而非工作空间。

---

## 模块主菜单

```
═══════════════════════════════════════════════════════
        AHKB-CPS：全息脑图生成模块菜单
═══════════════════════════════════════════════════════
  1. 🧠 基于知识库生成阿色全息脑图 — AI检索知识库，自动生成
  2. 📄 依据指定的文档生成阿色全息脑图 — 从知识库已入库文档提取内容
  3. ✍️ 独立生成阿色全息脑图       — 不依赖知识库，自由输入主题
  4. ✋ 手动创建阿色全息脑图       — 直接打开编辑器，手动创建和编辑
  e. ↩️ 返回主菜单                — 返回 AHKB-CPS 统一主菜单
═══════════════════════════════════════════════════════
请回复数字 1~4 或 e 选择操作：
```

## 菜单循环规则

- 操作完成后**返回模块主菜单**
- 仅当用户选择 `e` 时才返回 AHKB-CPS 统一主菜单
- 每次返回模块主菜单时，提示用户还可使用其他 AHKB-CPS 模块

---

# 菜单 1 — 🧠 基于知识库生成阿色全息脑图

## 检测知识库并选择工作模式

检查 `知识元/` 目录下是否有 ≥1 个 `.md` 文件。

**情况 A：检测到知识库（N 个知识元）** → 向用户展示：

**检测到知识库（N 个知识元），选择生成模式：**

1. 🧠 知识库驱动生成 — AI根据你的自然语言描述自动检索知识库，提取内容生成阿色全息脑图
2. ✏️ 手动输入制作 — 你指定主题，AI先检索知识库补充素材，再逐步生成阿色全息脑图

> 🔴 **两种模式都会检索知识库。** 如需完全不依赖知识库的独立生成，请使用菜单第 3 项。
>
> 也可以直接说其他要求或选项

**情况 B：无知识库** → 告知用户未检测到知识库，推荐使用菜单第 3 项。

---

## 🧠 知识库驱动模式

### Step K1 — 对话描述需求 + AI 自动检索

**(a) 用户描述需求**

**问：你想生成什么主题的阿色全息脑图？请用一两句话描述。**

**(b) AI 自动检索知识库**

```bash
python {skill_dir}/core/kb2slides.py search --workspace "<Vault路径>" --query "用户描述的关键词" --top 15
```

**(c) 展示检索结果，确认方向**

### Step K2 — 确认素材

**以上述检索到的资料为基础生成阿色全息脑图？**

1. ✅ 确认，基于这些资料
2. 🔍 缩小范围 — 输入更具体的关键词重新搜索
3. ✏️ 我来说明 — 用户直接说明想要哪些内容

> 也可以直接说其他要求或选项

### Step K3 — 进入生成流程

确认素材后，进入下方「🔄 通用生成流程」。

---

## ✏️ 手动模式

### Step M1 — 用户指定主题

**问：你想生成什么主题的阿色全息脑图？请用一两句话描述。**

### Step M2 — 检索知识库补充素材

```bash
python {skill_dir}/core/kb2slides.py search --workspace "<Vault路径>" --query "用户输入的主题" --top 10
```

> 🔴 **知识库有料就用，没料不勉强。**

### Step M3 — 进入生成流程

---

# 菜单 2 — 📄 依据指定的文档生成阿色全息脑图

## Step A — 文档选择

```bash
python {skill_dir}/core/kb2slides.py list-docs --workspace "<Vault路径>"
```

向用户展示编号列表（支持多选，如 1,3）。

## Step B — 获取文档内容

```bash
python {skill_dir}/core/kb2slides.py read-doc --workspace "<Vault路径>" --doc "文档路径"
```

## Step C — 进入生成流程

---

# 菜单 3 — ✍️ 独立生成阿色全息脑图

> 🔴 **菜单 3 与知识库完全无关。** 不做知识库检测，不做知识库检索。

```
指定主题 → 确认 → AI生成JSON → 打开阿色全息脑图 → 返回模块主菜单
```

---

# 菜单 4 — ✋ 手动创建阿色全息脑图

直接打开 `ahmm.html` 进入手动编辑模式，**不经过 AI 生成**。

```bash
# 🔴 路径必须用正斜杠 / ，不可用反斜杠 \
python -c "import webbrowser; webbrowser.open('{skill_dir_forward_slash}/mm/ahmm.html')"
```

> ✅ 阿色全息脑图编辑器已在浏览器中打开！
> 💡 单击各个【...】可编辑脑图，【≚】排版配色，Ctrl+S 保存

---

# 🔄 通用生成流程（菜单 1/2/3 共用）

## Step G1 — 确认主题与素材

向用户展示生成摘要：

```
═══════════════════════════════════════════════════════
  阿色全息脑图生成确认
═══════════════════════════════════════════════════════
  主题：【用户描述的主题】
  素材来源：【知识库/文档/独立创作】
  知识元数量：【N 个】（菜单 3 显示"无"）
═══════════════════════════════════════════════════════
```

**确认以上信息？确认后AI立即开始生成阿色全息脑图：**

1. ✅ 确认，开始生成 2. ✏️ 需要修改

---

## Step G2 — AI 生成全息脑图 JSON

AI **严格按照下方 JSON Schema** 生成阿色全息脑图数据。

### 🔴 JSON 输出规范

#### 一、总体要求

1. **标题(title)**：精准捕捉核心概念，**少于 20 字**
2. **简介(intro)**：提炼核心思想、主张、意义、作用、影响等，长度**约 180 字**
3. **内容区块处理**：
   - **(1) 总结区块(summary_block)**：核心区块/吸引子区块。**只有 1 个**
   - **(2) 内部主题区块(in_blocks)**：**自动识别 11 个**
   - **(3) 外部关联区块(out_blocks)**：**自动识别 5 个**

#### 二、各字段字数限制

| 区块 | 字段 | 字数限制 |
|------|------|---------|
| title | 标题 | **< 20 字** |
| intro | 简介 | **约 180 字** |
| summary_block | summary_block_name | **< 7 字** |
| summary_block | summary_block_kernal_word | **< 7 字** |
| summary_block | summary_block_keywords | **< 10 字** |
| summary_block | summary_block_info | **< 15 字** |
| summary_block | summary_block_more_info | **< 15 字** |
| in_blocks[i] | in_block_name | **< 8 字** |
| in_blocks[i] | in_block_kernal_word | **< 7 字** |
| in_blocks[i] | in_block_keywords | **< 12 字** |
| in_blocks[i] | in_block_info | **< 17 字** |
| in_blocks[i] | in_block_more_info | **< 17 字** |
| in_blocks[i] | in_block_importance | **5~10 数字** |
| out_blocks[i] | out_block_name | **< 10 字** |
| out_blocks[i] | out_block_kernal_word | **< 9 字** |
| out_blocks[i] | out_block_keywords | **< 13 字** |
| out_blocks[i] | out_block_info | **< 15 字** |

#### 三、命名规范

- **summary_block_name**：使用"核心概念或词汇"命名
- **in_block_name**：使用"核心概念/关键领域/主题维度"三元组命名法
- **out_block_name**：使用"核心概念/关键领域/主题维度"三元组命名法
- **keywords** 字段：采用"主语+状态+影响因素"模式提取
- **info** 字段：按"数据指标/现状描述/关联要素"三级压缩
- **more_info** 字段：聚焦"因果关系/解决方案/趋势预测"
- **kernal_word**：依据事实提取，避免宽泛字词

#### 四、输出格式

- ✅ JSON 格式正确，所有字段必须填写
- ✅ **输出为单行 JSON，禁止换行**
- ✅ 禁用所有空白字符及注释
- ✅ in_blocks 固定 11 个，out_blocks 固定 5 个

#### 五、JSON Schema 示例

```json
{
  "title":"全息脑图系统",
  "intro":"全息脑图是按照大系统思维原理制作的新型思维导图。让您以系统的观点看世界，专注系统的结构信息——全息，抓住事物的本质，透过表象和数据发现规律。",
  "summary_block": {
    "summary_block_name":"[ 系统总览 ]",
    "summary_block_kernal_word":"内外结构失衡",
    "summary_block_keywords":"经济失衡/贸易壁垒",
    "summary_block_info":"CPI波动/失业率攀升/地缘风险升级",
    "summary_block_more_info":"政策协同/产业升级/国际谈判"
  },
  "in_blocks": [
    {
      "in_block_name":"[ 1:经济系统 ]",
      "in_block_kernal_word":"内需严重不足",
      "in_block_keywords":"居民收入/无刺激政策",
      "in_block_info":"CPI指数/就业率/贸易逆差",
      "in_block_more_info":"刺激政策/产业升级/国际谈判",
      "in_block_importance":"5"
    }
  ],
  "out_blocks": [
    {
      "out_block_name":"[ 1:国际市场 ]",
      "out_block_kernal_word":"外需不足外贸收缩",
      "out_block_keywords":"高关税/产品低端/圣诞节",
      "out_block_info":"地缘政治动荡/贸易逆差大"
    }
  ]
}
```

> 📘 示例中仅显示部分，实际必须生成 **11 个 in_blocks** 和 **5 个 out_blocks**。

---

## Step G3 — 创建启动器并打开阿色全息脑图

### 工作原理

1. 在技能目录 `{skill_dir}/mm/` 下创建/覆盖启动器 HTML 文件
2. 启动器将 JSON 写入 `sessionStorage.setItem("ahmm_json", ...)`
3. 启动器自动跳转到 `ahmm.html?func=7`
4. `ahmm.html` 从 sessionStorage 读取 JSON 并渲染

### 启动器 HTML 模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>AHMM Launcher</title></head>
<body>
<script>
var json = {AI生成的JSON对象};
var jsonStr = JSON.stringify(json);
sessionStorage.setItem("ahmm_json", encodeURIComponent(jsonStr));
sessionStorage.setItem("ahmm_web_url", "");
window.location.href = "ahmm.html?func=7";
</script>
</body>
</html>
```

> 🔴 **关键细节**：
> - JSON 必须经过 `encodeURIComponent` 编码后再存入 sessionStorage
> - `ahmm_web_url` 设置为空字符串（KB 模式下可填知识元路径）
> - 启动器文件名：`ahmm_launcher.html`
> - 启动器必须写入 `{skill_dir}/mm/` 目录（与 `ahmm.html` 同目录）

### 生成与打开命令

```bash
# 1. AI 将启动器 HTML 写入 {skill_dir}/mm/ahmm_launcher.html
# 2. 自动打开启动器
# 🔴 路径必须用正斜杠 / ，不可用反斜杠 \
python -c "import webbrowser; webbrowser.open('{skill_dir_forward_slash}/mm/ahmm_launcher.html')"
```

### 生成完成后提示

> ✅ 阿色全息脑图已生成并自动打开！
> 💡 如果浏览器未弹出新标签页，请检查是否被浏览器拦截。也可手动打开：`{skill_dir}/mm/ahmm.html?func=7`
> 💡 单击各个【...】可编辑脑图，【≚】排版配色，Ctrl+S 保存

完成后**返回模块主菜单**。

---

# 返回

**用户选择 `e` 时：**

1. 感谢用户使用全息脑图生成模块
2. **返回 AHKB-CPS 统一主菜单**
