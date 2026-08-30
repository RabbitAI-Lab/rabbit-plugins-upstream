## Description:

A local, offline LLM evaluation toolkit that helps agents create and check JSONL evaluation sets, detect rule-based hallucination signals, compute simplified RAG metrics, compare regressions, and produce launch-gate reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI engineers, QA teams, and quality leads use this skill to turn LLM evaluation methodology into repeatable local checks for datasets, hallucination signals, RAG quality, regression deltas, and release gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Python commands read local evaluation data and can create output files.

Mitigation: Review file paths before running commands and execute the tool only in the intended workspace.

Risk: Rule-based hallucination checks and simplified RAG metrics can miss issues or produce false positives.

Mitigation: Use the outputs as a baseline signal and review important release decisions with human or stronger evaluator checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-eval-toolkit)
- [01 工具链全景](references/01-工具链全景.md)
- [02 评测集管理](references/02-评测集管理.md)
- [03 幻觉检测引擎](references/03-幻觉检测引擎.md)
- [04 RAG指标计算](references/04-RAG指标计算.md)
- [05 回归对比](references/05-回归对比.md)
- [06 报告与门禁](references/06-报告与门禁.md)
- [07 与平台工具衔接](references/07-与平台工具衔接.md)
- [08 FAQ](references/08-FAQ.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSONL examples, and local Python tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local evaluation artifacts such as JSONL templates, metric summaries, comparison results, and launch-gate reports when the bundled Python tool is run.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
