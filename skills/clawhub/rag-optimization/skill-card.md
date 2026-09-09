## Description:

RAG检索增强为开发者提供检索诊断、分块、重排序、Self-RAG、上下文压缩、引用溯源和评估工具，用于提升知识库问答的准确性并降低幻觉风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose and improve RAG systems for knowledge-base question answering, retrieval accuracy, hallucination reduction, citation tracking, and retrieval evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private documents, prompts, or retrieval context may be sent to remote model or embedding endpoints when LLM-backed RAG features are enabled.

Mitigation: Use trusted HTTPS endpoints, avoid confidential corpora without privacy review, and disable or review LLM-backed features for sensitive data.

Risk: API credentials may be loaded from environment variables or project .env files.

Mitigation: Use controlled secret handling, accept .env files only from trusted sources, and do not distribute real credentials in shared skill files or configuration.

Risk: Dependency and model choices can affect retrieval quality and reproducibility.

Mitigation: Install in an isolated environment with pinned dependencies and validate retrieval behavior on a representative golden set before production use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/kiwifruit13/skills/rag-optimization)
- [RAG优化快速入门](references/quickstart.md)
- [全局操作说明](references/global-operations.md)
- [RAG高级技术实现指南](references/advanced-techniques.md)
- [RAG系统全链路问题与应对策略](references/implementation-guide.md)
- [Golden Set 建设指南](references/golden-set-guide.md)
- [scripts API 参考文档](references/api_reference.md)
- [API 文档自动生成](references/api-docs-auto-generation.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code examples, shell commands, JSON configuration templates, and evaluation report JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some LLM-backed features require API credentials and may fall back to rule-based behavior when not configured.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
