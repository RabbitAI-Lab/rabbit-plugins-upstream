---
name: resume-optimizer
description: "简历优化两步走编排器：第一步调用 resume-assistant 按 JD 重组内容并量化成果，第二步调用 humanizer 去除 AI 写作痕迹。解决直连 AI 重写导致的「空洞修饰词+千篇一律句式」问题，产出既专业又像本人写的简历。"
description_zh: "简历优化两步走编排器：重组量化 + 去AI味"
description_en: "Two-step resume optimizer: restructure-quantify then de-AI"
version: 1.0.0
category: career
tags:
  - resume
  - career
  - job-hunting
  - ai-writing
  - humanizer
  - orchestrator
allowed-tools:
  - Skill
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# Resume Optimizer — 简历优化两步走编排器

> **一句话**：用户给简历素材（+ 可选 JD）→ 第一步 `resume-assistant` 重组量化 → 第二步 `humanizer` 去AI味 → 输出可投递终稿。

## 一、为什么需要这个编排器

直接让 AI 重写简历有三个典型病灶：

| 病灶 | 表现 | 后果 |
|---|---|---|
| 成果没量化 | "负责用户增长""效果还行" | HR 看不到价值密度 |
| 措辞太口语 | "做了个活动""带团队做迭代" | 专业度不够，首轮被筛 |
| AI 味太重 | "具有丰富的 XX 经验""在 XX 领域有深刻理解""深度参与、高质量交付、显著提升" | HR 一眼识破，比口语化更致命 |

**核心矛盾**：AI 重写能解决前两个问题，但会引入第三个问题。HR 每天看几百份简历，AI 味传递的信号是「求职者自己都没认真对待」。

**解决方案**：两步走 — 先用 `resume-assistant` 把内容和结构搞对，再用 `humanizer` 把 AI 味洗掉。两步缺一不可。

## 二、触发条件

- "帮我优化简历 / 改简历 / 简历润色"
- "我的简历 AI 味太重，帮我弄自然点"
- "按这个 JD 改我的简历，但别让 HR 看出是 AI 写的"
- "简历投出去石沉大海，帮我看哪里有问题"
- 用户引用 `@scene#18` 或提到「简历优化场景」

## 三、编排工作流

### Step 0 · 素材收集（必做）

向用户收集：
1. **简历素材**：粘贴文本 / 上传 PDF·Word / 口述经历均可
2. **目标 JD**（可选，强烈推荐）：有 JD 时走 `tailor` 模式，效果显著更好
3. **偏好**（可选）：模板风格、长度、语言（中/英/双版）

> 若用户只给 JD 没给简历 → 追问简历素材
> 若用户只给简历没给 JD → 走 `rewrite` 模式，并在 Step 2 后提示"提供 JD 可进一步定制"

### Step 1 · 调用 resume-assistant（重组 + 量化）

**触发方式**：调用 `Skill` 工具，command = `resume-assistant`

**你需要对这个 Skill 说的话**（作为它的用户输入）：

```
用户简历素材：
<粘贴用户提供的简历原文>

目标 JD（如有）：
<粘贴 JD，没有则删掉这行>

请按照以下要求处理：
1. 路由到 <tailor | rewrite> 模式（有 JD 走 tailor，无 JD 走 rewrite）
2. Preflight 偏好：<按用户回答填，或"默认">
3. 重点：量化所有成果（缺数字的经历用占位符 [待补充] 标注，绝不编造）
4. 输出 Markdown 版本到 resume-output/

⚠️ 这是两步走的第一步，本步只做结构化+量化，不需要过度润色措辞。
   AI 味的清除会在第二步由 humanizer 处理。
```

**验收 checkpoint**（拿到 resume-assistant 产出后检查）：
- [ ] 所有经历条目都有数字（或 `[待补充]` 占位符），无凭空编造的数字
- [ ] 结构符合 STAR / 项目导向模板
- [ ] 待填的联系信息用占位符（`[电话待填写]` 等），非假号码
- [ ] 有 JD 时，关键词已对齐
- [ ] 输出落在 `resume-output/*.md`

**若 checkpoint 不过**：把问题回传给 resume-assistant 让它修，不要自己动手改简历内容（编排器不越权改内容）。

### Step 2 · 调用 humanizer（去 AI 味）

**触发方式**：调用 `Skill` 工具，command = `humanizer`

**给 humanizer 的输入**：Step 1 产出的 Markdown 简历全文。

**你需要说的话**：

```
请对以下简历内容做去 AI 味处理。这是一份求职简历，目标读者是 HR 和业务面试官。

重点清理：
- 空洞修饰词："丰富的""深刻的""显著的""高质量""深入""深度参与"
- 排比三连（Rule of Three）："做了X、优化了Y、提升了Z"
- 负向并列："不仅…更是…"
- 算法腔句式：每句等长、整齐划一
- 谄媚收尾："期待能加入贵公司共同成长"

要求：
- 保留所有数字和事实（这些是 step 1 量化出来的，不能动）
- 句式长短交错，允许适度口语但不失专业
- 加入第一人称视角，让它像本人写的
- 输出去 AI 味后的完整简历 Markdown

简历内容：
<粘贴 step 1 产出>
```

**验收 checkpoint**：
- [ ] 所有数字 / 项目名 / 技术栈与 Step 1 产出一致（humanizer 不许改事实）
- [ ] 无明显 AI 味词（"此外/至关重要/凸显/赋能/助力/持续推动"）
- [ ] 句式不整齐划一，有长短变化
- [ ] 读起来像本人写的，不像机器生成的

### Step 3 · 交付 + 提示

把 Step 2 产出作为最终简历交付给用户，并附带：

1. **占位符清单**：列出所有 `[待补充]` / `[电话待填写]` 等，提醒投递前填写
2. **可选下一步**：
   - "需要导出 PDF 投递版吗？" → 触发 resume-assistant 的 `export` 模式（ATS-safe 主题）
   - "需要针对这个 JD 的面试准备吗？" → 触发 resume-assistant 的战略附录
   - "要不要再针对另一家公司做一个定制版？" → 回到 Step 1，新走一轮

## 四、边界与 NEVER

| 边界 | 说明 |
|---|---|
| ❌ 不自己改简历内容 | 编排器只协调，内容改写交给两个子 Skill |
| ❌ 不编造数字 | 缺数字一律 `[待补充]` 占位符 |
| ❌ 不跳过 Step 2 | 没去 AI 味的简历不允许作为终稿交付 |
| ❌ 不做 OCR | 扫描件 PDF 让用户复制粘贴文本 |
| ❌ 不补假联系方式 | 姓名/电话/邮箱未提供一律占位符 |
| ✅ 两步都要做 | 即使用户说"随便改改"也要走完两步 |

## 五、子 Skill 依赖

| 子 Skill | 来源 | 版本 | 作用 |
|---|---|---|---|
| resume-assistant | marketplace (skill_2057443453823152128) | 1.0.0+ | 重组 + 量化 + JD 对齐 |
| humanizer | marketplace (skill_2053082097175687168) | 2.1.1+ | 去除 24 类 AI 写作痕迹 |

> 若任一子 Skill 未安装，编排器应提示用户先安装，不可降级走单步。

## 六、参考文档

- 详细方法论与场景介绍：[`references/scene-18-overview.md`](references/scene-18-overview.md)
- Before/After 写法对比：[`references/before-after-examples.md`](references/before-after-examples.md)
