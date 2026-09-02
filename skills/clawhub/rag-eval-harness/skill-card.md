## Description:

RAG Q&A quality evaluation and anti-hallucination verification guidance for checking answer accuracy, fabrication risk, and stability across knowledge-base or model changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to evaluate RAG systems before launch, after corpus changes, or after model changes. It supports positive retrieval tests, negative refusal tests, citation-backed answering expectations, local retrieval evaluation, and threshold scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local evaluation script reads the knowledge-base folder configured by RAG_EVAL_BASE and sends text to a local Ollama service.

Mitigation: Review RAG_EVAL_BASE before running and use a trusted local Ollama instance with only the intended corpus.

Risk: The capability suite runs scripts declared in suite_registry.json.

Mitigation: Keep suite_registry.json trusted and review changes before executing the suite.

Risk: The bundled scripts write evaluation reports and history files locally.

Mitigation: Run the scripts in a workspace where generated report files are expected and review outputs before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-eval-harness)
- [local_rag_eval.py](references/local_rag_eval.py)
- [capability_eval_suite/run_suite.py](references/capability_eval_suite/run_suite.py)
- [capability_eval_suite/suite_registry.json](references/capability_eval_suite/suite_registry.json)
- [security_results.json](security_results.json)
- [Security audit report](安全审计报告.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command snippets plus local JSON report outputs from the bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports may include eval_questions.json, rag_eval_report.json, suite_report.json, and suite_history.jsonl when users run the bundled local scripts.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter and manifest report 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
