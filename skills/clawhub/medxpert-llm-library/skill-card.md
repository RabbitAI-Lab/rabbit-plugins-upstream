## Description:

MedXpert LLM Library guides users through running local LLMs with Ollama on low-spec computers and building a personal or organizational knowledge base with summarization, retrieval Q&A, library management, and AI-readable templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, knowledge workers, and small teams use this skill to set up a local Ollama-based knowledge base, summarize local Markdown and text documents, ask source-grounded questions, and manage library structure, quality, permissions, and publication workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send local document contents to the endpoint selected by OLLAMA_BASE.

Mitigation: Run with OLLAMA_BASE unset or explicitly set to localhost or 127.0.0.1, and review the endpoint before summarizing or asking questions over private or regulated documents.

Risk: LIBRARY_DIR controls which local folder is initialized, scanned, summarized, and queried.

Mitigation: Set LIBRARY_DIR only to the intended library folder and review its contents before running summarize, ask, health, or scan commands.

Risk: The bundled audit report covers an older version and conflicts with the helper script's actual Ollama HTTP requests.

Mitigation: Use evidence.security as the authoritative review signal and perform a fresh local review before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/medxpert-llm-library)
- [MedXpert Website](https://medxpert.cn)
- [Ollama Download](https://ollama.com/download)
- [AI Library Map Template](templates/llms.txt)
- [AI Usage Instructions Template](templates/README-ai.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, Python helper commands, and reusable template files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local knowledge-base setup, summarization, Q&A, health-check, and sensitive-data scan workflows.]

## Skill Version(s):

1.29.1 (source: frontmatter, CHANGELOG, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
