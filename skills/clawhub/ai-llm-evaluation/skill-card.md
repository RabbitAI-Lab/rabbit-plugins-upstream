## Description:

A hands-on playbook for LLM application quality evaluation and regression testing, covering metrics, test-set design, RAG evaluation, hallucination measurement, prompt regression, model comparison, and report templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

AI engineers, QA teams, product owners, and quality leaders use this skill to design measurable LLM quality gates, build evaluation sets, assess RAG behavior, quantify hallucinations, compare model options, and produce regression reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manual verification scripts can rewrite files in the package's verify directory.

Mitigation: Run verification in a working copy and review generated files before packaging or publishing.

Risk: The MIT license text and separate knowledge-copyright language may be inconsistent for redistribution.

Mitigation: Confirm redistribution rights and license terms with the publisher before broad reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-llm-evaluation)
- [01 评测全景与指标](references/01-评测全景与指标.md)
- [02 评测集构建](references/02-评测集构建.md)
- [03 RAG 系统评测](references/03-RAG系统评测.md)
- [04 幻觉检测与度量](references/04-幻觉检测与度量.md)
- [05 Prompt 回归测试](references/05-Prompt回归测试.md)
- [06 模型对比选型](references/06-模型对比选型.md)
- [07 评测流程与报告](references/07-评测流程与报告.md)
- [08 FAQ](references/08-FAQ.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, text]

**Output Format:** [Markdown guidance with inline shell commands and local text report templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled local toolkit uses Python standard library commands and prints results to standard output.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
