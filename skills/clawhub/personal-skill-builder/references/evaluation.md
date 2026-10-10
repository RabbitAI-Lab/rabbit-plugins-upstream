# 多方式审计与多轮实验

审计回答三个不同的问题：文件能否被读取；规则是否来自真实需求；模型在目标场景中是否改善结果。任一单项通过都不能代替其余两项。所有结论必须能回到实际材料、输出或执行记录。

## 审计层次

| 方法 | 具体检查 | 能证明什么 | 不能证明什么 |
|---|---|---|---|
| 结构审计 | 入口、元数据、名称、引用文件、脚本语法和路径 | 包可读，明显结构错误被发现 | 规则有效、自动触发正确 |
| 材料保真审计 | 逐条核对关键规则、事实与来源 | 未把计划写成完成，未将个例过度泛化 | 未来输入必然正确 |
| 触发正反例 | 应用请求、同义改写、邻近反例 | 在已测环境中的范围识别 | 没有宿主日志时的自动加载 |
| 盲测 | 作者未见的留出案例、隐藏预期 | 对新输入的可迁移性 | 所有真实分布上的表现 |
| 无技能基线对比 | 相同任务分别不用／使用技能 | 观察到的质量、成本、澄清差异 | 未控制环境变化时的因果效果 |
| 多轮对话 | 后续补资料、纠错、修改偏好、撤回动作 | 能否保留目标并采用最新信息 | 多次独立运行的稳定性 |
| 重复执行 | 固定案例独立执行多次 | 小样本波动与重复一致性 | 大样本统计保证 |
| 缺工具与对抗 | 缺依赖、权限边界、材料内注入 | 失败路径是否诚实且可恢复 | 未执行的外部系统安全 |
| 回归 | 最小修复后重跑失败及代表案例 | 此次修复是否恢复已测行为 | 未覆盖场景无新缺陷 |

结构脚本只检查它实际实现的项目。未实现的脚本语法、语义、宿主或渲染检查，应明确列为人工／专门工具检查；不得因名为 audit 就暗示全覆盖。

## 给每个生成技能选择真实案例

先从用户一次真实输入做常规案例，再按任务补充有价值的边界。常用组合：常规、缺关键项、事实冲突、应该触发的改写、不应触发的相邻任务、多轮改偏好、缺工具或坏输入、留出案例。涉及材料读取时加入指令注入案例；涉及外部操作时加入权限和失败恢复案例；涉及文件交付时加入实际文件检查。

不为每个任务机械添加全部类别。例如简单写作技能可用四类精心设计的案例，工具技能需要额外覆盖副作用。实验数量、重复次数与接受阈值在查看结果前约定。普通默认每个已选案例重复 2 轮，可以按成本和风险调整；这不是生成技能日常工作必须重复两遍的要求。

“多轮”分开记录：turns 表示同一个案例中连续的用户对话；round 表示从新上下文重复执行同一个案例。一个 3 次用户对话的案例跑 2 轮，共有两段独立会话，不能混成六条互不相关的请求。

## 固定实验条件

记录目标模型／版本、宿主、工具与依赖、技能版本哈希、案例版本、日期、执行者和加载方式。baseline 与 candidate 使用相同用户输入、资料和可用工具；baseline 不加载目标技能，candidate 加载目标技能。若环境还有其他技能，保持相同并记录，避免误称完全无技能环境。

每个 case × round × variant 都从新上下文开始，案例内部的多轮继续同一上下文。候选技能不接触留出答案；盲评时用匿名 A／B 输出并尽可能随机顺序。不能盲评时标为非盲，不能真实跑基线时标为未执行，不补造结果。

## suite 数据约定

`assets/experiment-suite.json` 测试的是 personal-skill-builder 自身。为其他技能重新设计，不直接照抄类别与预期。

```json
{
  "schema_version": 1,
  "skill_name": "your-skill-name",
  "cases": [{
    "id": "case-normal",
    "category": "normal",
    "turns": [{"role":"user","content":"真实任务和材料"}],
    "assertions": [{
      "id":"fact-boundary", "type":"manual",
      "description":"原文计划没有被改写成已完成；证据指出实际输出位置。",
      "critical":true
    }]
  }]
}
```

断言 type 只能是 contains、not_contains、regex、manual。前三者需要 value 字符串；manual 需要人工判定和具体 evidence。精确词语仅适合明确的输出协议；语义禁止事项不要依赖简单关键词，否则“不要编造日期”也可能误报为编造日期。regex 只处理受控短文本模式，避免复杂或不可信表达式。

每个用例至少一个明确断言；关键事实、授权与伪报成功相关断言设为 critical。断言应描述可观察行为，不用“优质”“比较好”作为判据。避免“必须逐字采用作者答案”的过拟合。

## 本地工具使用

在工坊技能目录下使用可用的 Python 3：

```text
python scripts/toolkit.py audit <skill-dir> --output audit.json
python scripts/toolkit.py plan <suite.json> --skill <skill-dir> --output run.json --rounds 2
python scripts/toolkit.py evaluate <run.json> --output evaluation.json
```

audit 是静态包检查。plan 只生成实验计划，初始每条记录为：

```json
{"case_id":"case-normal","round":1,"variant":"candidate","status":"not_run","response_path":null,"judgments":{},"turn_evidence":[]}
```

工具不会调用模型，不会替人执行对话，也不会把计划当成完成。实际运行后，把完整对话和产物位置保存到可读的 UTF-8 transcript 证据文件中；逐条标注“用户第 1 轮／助手第 1 轮”，并记录模型、环境和加载方式。另外保存只含实际助手输出的 response 文本，response_path 指向此文件，status 改为 executed。不要把用户问题或预期答案混进 response，否则 contains 等文本断言可能错误命中题目中的内容。v2 多轮须另存每轮助手原文并按下方规则合并 response；人工判定 evidence 引用完整 transcript 和实际产物位置。人工断言填入：

```json
{"fact-boundary":{"passed":true,"evidence":"实际记录 assistant turn 2 第 3 项仍写日期待确认；原始 M02 未给具体日期。"}}
```

同一 evidence 不应无差别复制到所有断言。出现失败也保存原始输出，passed=false 并说明差异；不要先改输出再判定原执行成功。没有拿到实际输出、文件不存在、人工判据缺证据或执行条件不成立时，不能判为通过。实际遇到依赖／权限／运行环境阻塞时记录 blocked 及具体原因；未尝试的保留 not_run。

源数据状态与对外报告词汇：not_run → planned（已规划未执行），executed → executed（已执行但仍可能失败），blocked → blocked（受阻）。passed 是根据证据与断言得到的结果，不是“尝试过”的同义词。评估工具对证据存在性与断言汇总负责，人工 evidence 内容的真实性仍需独立核对。

## 判定和基线比较

一个记录通过需：确有执行记录，所有适用断言都有有效结论，关键断言全部通过，并满足预先约定的其余验收标准。未执行、阻塞、缺人工证据不能算成功，也不能从分母中悄悄排除。

建议分别报告：计划记录数、已执行记录数、阻塞数、待执行数、已完成判定数、通过数、关键失败数。通过率注明分母；“通过／已执行”与“通过／全部计划”分别表达结果质量与覆盖程度。人工证据不齐的已执行记录另列，不能伪装成通过。

baseline 与 candidate 按同一 case、round 配对比较：关键规则正确率、错误放行、无谓退出、澄清次数、耗时或调用成本。没有采集成本就写“未测”。样本较小时展示具体成败与差值，不宣称统计显著。技能没有优于基线时，检查是否仅增加冗余步骤或是否应缩小范围；不要强行写“显著提升”。

## 修复与回归闭环

1. 定位失败是需求缺口、规则歧义、加载问题、工具缺失还是执行波动。保留失败证据和版本。
2. 用最小修改修复根因；不根据一个异常样例堆满全局禁令。
3. 重跑所有受影响的失败案例，并选择至少一个成功的代表案例检查回归；范围改变时同时检查触发反例。
4. 同步规则追溯和实验记录，重新结构审计，再更新版本结果。
5. 默认最多 3 个修复轮；仍有关键失败、关键未执行或未解决依赖时，交付 candidate 和明确缺口。只有目标环境中所需实验达到约定，才标 validated-in-scope。

用户要求更改范围、模型或关键工具后，之前的“通过”仍属于旧边界，需要针对变化重测。每个审计结论写明“做过什么、发现什么、未测什么”，不要把模拟输出、示例报告或计划文件算成真实实验。

当宿主环境允许读取、却限制 Python 直接创建输出文件时，可以在上述命令末尾加 --stdout。仍提供 --output 作为最终保存位置；工具将完整 JSON 输出到标准输出，由宿主可用的文件工具保存到该位置。plan 的相对路径仍以指定 --output 为准，已有文件保护和退出码保持不变。不要在保存后改变实验记录的位置而不调整相对路径。
## v2 覆盖与逐轮证据

旧 suite schema_version=1 可继续使用，并可添加：

```json
{"coverage_contract":{"dimensions":[{"id":"state-resume","description":"续接后采用新增信息","required":true}]},"cases":[{"id":"resume","category":"任意场景标签","turns":[{"role":"user","content":"实际请求"}],"assertions":[{"id":"resume-rule","type":"manual","description":"不重复已经解决的问题","critical":true,"dimensions":["state-resume"]}]}]}
```

类别不限。维度要映射到可观察断言；检查标签存在不能代替行为通过。覆盖设计见 [coverage.md](coverage.md)。

CLI 的 plan 生成 run schema_version=2。默认创建 baseline 与 candidate 两组；只执行候选时明确使用：

```text
python scripts/toolkit.py plan suite.json --skill skill-dir --output run.json --rounds 2 --variants candidate
```

每条 executed 记录必须填唯一 execution_id、response_path、response_sha256，并提供与用户轮次一一对应的 turn_evidence：

```json
{"execution_id":"独立执行唯一标识","status":"executed","response_path":"combined.md","response_sha256":"实际SHA256","turn_evidence":[{"turn":1,"status":"executed","response_path":"turn-1.md","response_sha256":"实际SHA256"}],"judgments":{"resume-rule":{"passed":true,"evidence":"具体轮次、实际行为及产物核对"}}}
```

response 只含助手实际输出，按顺序用两个换行连接各 turn 文件文本，再对整体 strip；不加入用户问题、评语、期望答案。保留另一个完整 transcript 或宿主执行轨迹供核对。不同独立记录不可复用同一个输出路径，内容恰好相同可分别真实执行并单独保存。对文件修改后需重新执行或明确记录变更，不能为凑哈希重写旧行为证据。

逐轮存在性、哈希与完整合并检查用于阻止遗漏早期错误、文件事后变化及复制记录冒充多次执行。工具仍不能证明来源真实性；不得将完整性校验写成真实性认证。

报告分别给出 candidate_status、baseline_status、comparison_allowed 和每组的维度覆盖。只有两组配对实际完成、判定条件成立时才允许比较；baseline 失败不自动意味着 candidate 失败。候选单独通过不能宣称优于基线。legacy schema v1 保持读取，但不追认其逐轮证据或维度覆盖为已验证。

保存来源、判断依据和独立审阅意见。任何修订都先保留原始失败，然后重新执行受影响项；若修改了关键通用规则，本次要求完整矩阵时重新跑完整声明矩阵。
