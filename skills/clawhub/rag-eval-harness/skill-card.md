## Description:

Helps developers evaluate RAG answer quality and test whether systems refuse unsupported questions rather than invent answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); MIT (.py code only); documentation and methodology: all rights reserved

## Use Case:

Developers and engineers use this skill to check retrieval accuracy, test refusals for out-of-scope questions, and choose rejection thresholds before deploying or updating a RAG knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluation scripts read local knowledge-base files, which may contain sensitive content.

Mitigation: Set and review the intended knowledge-base path before running the scripts.

Risk: Running the scripts contacts a local Ollama service and writes or overwrites evaluation reports.

Mitigation: Confirm the local Ollama endpoint and review or back up existing report files before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/rag-eval-harness)
- [Local RAG evaluation script](references/local_rag_eval.py)
- [Capability evaluation suite](references/capability_eval_suite/run_suite.py)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, JSON]

**Output Format:** [Markdown evaluation guidance and local JSON evaluation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes positive retrieval and negative refusal checks and threshold recommendations.]

## Skill Version(s):

1.1.4 (source: server-resolved ClawHub release; bundled files say 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
