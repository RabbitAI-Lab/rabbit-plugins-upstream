## Description:

Evaluates RAG question-answering systems with positive answer checks, negative refusal tests, citation validation, local retrieval scoring, and threshold scanning to reduce hallucinations before release or after corpus or model changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, QA engineers, and knowledge-base owners use this skill to validate RAG systems before launch, after corpus changes, or when switching retrieval or generation models. It helps quantify answer correctness, refusal behavior, citation coverage, and retrieval threshold choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluation scripts read the configured local knowledge base and create local report or history files.

Mitigation: Run them only against approved local knowledge-base paths and review generated JSON or JSONL outputs before sharing.

Risk: The suite runner executes scripts listed in the suite registry.

Mitigation: Keep suite_registry.json limited to trusted, reviewed scripts before running the suite.

## Reference(s):

- [RAG retrieval evaluation script](references/medxpert_rag_eval.py)
- [Capability evaluation suite runner](references/capability_eval_suite/run_suite.py)
- [Capability evaluation suite registry](references/capability_eval_suite/suite_registry.json)
- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-eval-harness)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and JSON reference files plus shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference scripts may create local JSON reports and JSONL suite history files when executed.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
