# penguin-guard 已知限制与验证记录（2026-09-29 探针实测）

## 限制 1：skill 级挂载空窗 —— 已解（profile 级激活成立）

v1 时 guard hook 随 oss-workflow skill 加载注册（s4 实测：skill L503 前的 63 条 pwsh 零 hook）。
**2026-09-29 headless 探针 probe2/probe3 证实**：桥接包 @deepseek-ai/dsh-hooks-claude-code
作为 profile 依赖 + cordis.patch.yml insert 条目（configPath 指向本目录 hooks.json）时，
hook 从 **turn 1** 即 fire（probe3 L23：turn 1、PreToolUse、matcher `pwsh|Bash|bash|Shell`），
不依赖任何 skill 加载。skill 级挂载空窗（TRIPLE-BATTLE-SYNTHESIS U3）在 profile 级挂载下关闭。

两个必要条件（缺一不可，probe1 → probe2 对照证实）：
1. profile 的 package.json 依赖里装有桥接包（headless profile 原为空依赖，装后 hook 才 fire——
   "--patch overlay 只注入配置条目，包缺失则插件解析失败从未 apply"）；
2. cordis.patch.yml 有 insert 条目把 configPath 指向本目录 hooks.json。

## 限制 2：存在性门禁 ≠ 时序门禁 —— push 类已修（guard v2 A 类校验）

v1 只查 `.oss-task/*/CHECKLIST.md` 存在。v2 起分级：
- **A 类**（git push / gh pr create）：存在 + R14/放行行 `[x]` + 证据指针
  （m-ref / URL / 引号原文 / 时间戳）。三场实战勾选滞后 push 40-138s、"勾了没做"，
  本闸把顺序强制反转：先勾（带证据）后推。
- **B 类**（gh pr comment/edit/review/merge/close、gh issue 写）：仅存在性
  （评论预览等门禁仍由 oss-workflow s2.md 文本规则承担）。

## 限制 3：宿主 ctx.shell 包装改写非零退出码 —— 已绕行（guard v2.1 双模式）

**发现**：probe2 实测，guard 以 stderr+exit 2 表达拦截，宿主包装层把退出 2 改写为 1
（本地 subprocess 直跑为 2，消息逐字一致）；dsh-hook-protocol 只认 exitCode===2（block）
或 exitCode===0+stdout JSON（L110/L114），exitCode=1 两分支都不命中 → decision=pass，拦截失效。
stderr 消息本身完整送达，但只起提示作用，不产生拦截。

**绕行**：guard v2.1 双模式——stdin 载荷带 `hook_event_name=PreToolUse`（桥接形态）时，
拦截改走 stdout `{"decision":"block","reason":...}` + exit 0；CLI 直调保留 stderr+exit 2。
probe3 transcript 证实：L24 `decision=block, exitCode=0`，L25 tool/result `isError=true`
+ reason 全文送达模型，git 从未启动。

**残留边界**：若宿主未来连 stdout JSON 也改写（未观察到），拦截将退化为提示；
guard 对不可解析 stdin 载荷 fail-open（避免桥接协议变化卡死会话）。

## 限制 4：文本证据可伪造、产物缺失不可验 —— 已修（guard v3 证据槽闸）

**发现**：2026-09-29 五场实战技能利用率审计——套件 29 能力触达 3（council 0/5、
ocr 探测 `--version` 后弃用 2/5、oss-security 0/5）。模型自称「已执行」而无落盘
产物 = 未执行；v2 只验 R14 勾+文本证据指针，挡不住「勾了技能步骤但产物不存在」。

**修复**：guard v3 A 类追加第三道校验 `missing_slots()`——扫描清单已勾选条目
（`- [x]` 行及其后缩进行同属一个条目）中的 `证据:`/`落盘:` 路径槽；token 呈
路径状（含斜杠或以 .md/.json/.txt/.log/.yml/.yaml/.csv 结尾）时按项目根与清单
目录两处解析，文件不存在 → block。m-ref/引号原话等指针型证据不触发文件系统
校验；未勾选条目的槽不校验。

**残留边界**：槽校验只对 A 类（push / gh pr create）生效；B 类评论仍靠文本规则。
模型可把产物写成空文件骗过存在性检查——内容质量由 council.md 格式约定与
战报复盘兜底，机器只验「有没有」，不验「好不好」。

## 复现命令（Windows / DSH）

```powershell
# 依赖：headless profile 已装 @deepseek-ai/dsh-hooks-claude-code 0.2.0-rc.1
# 补丁：同目录 probe-guard.example.yml（insert 条目指向本目录 hooks.json）
cd <无 .oss-task 的干净目录>
dsh --profile headless --patch guard-probe.yml "用 pwsh 跑这个命令并逐字报告输出或被拦截的信息：git push origin master"
# 期望：模型报告被 [penguin-guard] 拦截；session.v4.jsonl 中 hook/result decision=block
# 测试：python guard_v2_test.py（12 断言：六场景 × CLI/桥接双模式）
```
