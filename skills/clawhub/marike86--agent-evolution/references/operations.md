# 记忆与试验操作

## 记忆对象和采用条件

| 对象 | 记忆内容 | 后续用途 |
| --- | --- | --- |
| 成果 | 产物路径或来源、简要用途、版本与可用范围 | 查到后直接打开核对。例如实验材料、文献证据表、分析代码或可复用评分规则。 |
| 事实 | 经核实的事实、证据位置、适用条件与重查触发 | 当前任务匹配时引用或核对。 |
| 决定 | 用户或项目确认过的决定、理由及范围 | 后续同项目任务按范围沿用，遇新指令则更新。 |
| 假设 | 提出的新问题、候选机制、预期模式与判别线索 | 当作待检验构思取回，附状态。 |
| 做法 | 一次有效或可能有效的策略、何时使用及反例 | 作为待验证做法试用。稳定改变默认行为时再做配对验证。 |
| 经历 | 事件、反馈、错误或成功、证据位置及不确定性 | 解释策略从何而来，按需提炼或作反例。 |

## 文件与命令

优先使用当前宿主实际读取的记忆。需要文件型存储时，可在授权项目中用随附脚本初始化。Python 3.9 或更新版本。

```bash
python3 EVOLVE --project PROJECT init
python3 EVOLVE --project PROJECT capture ENTRY.json
python3 EVOLVE --project PROJECT recall "量表 计分"
python3 EVOLVE --project PROJECT recall "认知卸载" --include-unverified
python3 EVOLVE --project PROJECT stage candidate.md
python3 EVOLVE --project PROJECT promote TRIAL_ID results.json
python3 EVOLVE --project PROJECT rollback
```

- `EVOLVE` 为随附脚本路径，`PROJECT` 为项目路径。`init` 可接收一个已有记忆文件作为长期记忆初版。
- `capture` 以单条记录写入 `.agent-evolution/entries/`，供检索和后续提炼。相同内容再次提交会返回同一条记录。需要替换失效条目时，在新记录填入 `supersedes` 的旧条目 ID。
- `recall` 用空格分隔关键词，按匹配程度和记录时间返回少量条目。用 `--scope` 可限定到完全匹配的记录范围。默认返回可复用的成果、核实事实和确认决定。显式加入 `--include-unverified` 可查候选假设、待验证做法和任务经历。旧 `episodes.md` 若存在，可按需读取，保持原记录。
- `.agent-evolution/MEMORY.md` 是版本化的长期记忆。短写经核对的通用知识、索引或已验证的行动规则。可从其中指向相关条目和产物。日常登记走 `capture`，可继续按需读取版本化记忆，无需每次重写。
- `stage` 把当前长期记忆和候选保存到 `.agent-evolution/trials/TRIAL_ID/`。已明确授权且要长期改变行为时，用 `promote` 检查结果并采用。已保存版本可回滚，`--to VERSION` 指定版本。脚本核对记录结构、摘要与评分条件，事实和结果仍由执行者检查。

### 捕捉条目示例

```json
{
  "kind": "artifact",
  "title": "科学假设生成任务的盲评方案",
  "summary": "保存了两套平行任务的评分表和分歧处理流程。",
  "scope": "当前项目的本科生预实验",
  "source": "analysis/ratings/rubric-v2.md",
  "trigger": "复用任务或训练评定者时",
  "review_when": "任务材料或评分维度发生变化时"
}
```

`kind` 取 `artifact`、`fact`、`decision`、`hypothesis`、`practice`、`observation` 之一。前四个必填文本字段是 `title`、`summary`、`scope`、`source`，`trigger`、`review_when` 和 `supersedes` 可选。未核实的事实保留为 `observation`。仅在证据和授权足够时登记 `fact` 或 `decision`。每条尽量保持简短。

## 长期做法的配对验证

1. 在不同会话比较基线与候选，保持任务、模型、工具与材料可比。留出未参与调优的案例，另测需要保护的既有行为。
2. 事先规定分值 0 至 1 的含义。评测 JSON 用 `trial`、`baseline_sha256`、`candidate_sha256` 匹配试验清单。每条 `cases` 包含 `id`、`kind`（`holdout` 或 `regression`）、`criterion`、`before`、`after`、`baseline_evidence` 和 `candidate_evidence`。
3. 至少一个留出案例改善且既有检查未退步，才采用这条长期规则。证据不稳时继续试验，或把做法保留为条件性经验。新会话确认被读取且行为符合预期。

## 科研工作例子

在读论文过程中得到一个可区分「外部信息依赖」和「知识整合」的实验比较。立刻将设计稿作为成果登记，将两种解释作为候选假设保留。结束时可以发现「先画各机制的预测表，再决定操纵」帮助减少了返工，于是记录成待验证做法。下次做机制比较时取回预测表。若新的任务继续支持该做法，并且简单任务无额外负担，再升级为项目的默认程序记忆。
