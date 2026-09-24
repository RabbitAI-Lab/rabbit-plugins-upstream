## Description:

Supports local knowledge-base document retrieval, document ingestion, and switching between local and AnythingLLM-style knowledge modes for knowledge management workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, individual creators, and teams use this skill to have an agent search, organize, and ingest local knowledge-base documents, switch retrieval modes, and return task status or summaries. It is intended for knowledge capture, document management, and automation workflows, not unaudited human-judgment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local file read/write and command-execution authority can expose or modify local knowledge-base content if used without clear review.

Mitigation: Install only when comfortable granting those capabilities, and require explicit confirmation before document ingestion, API use, network calls, or shell command execution.

Risk: Inconsistent local-versus-network guidance can cause sensitive document content to be sent outside the intended local workflow.

Mitigation: Use local mode for sensitive documents, verify the active retrieval mode and endpoint before switching modes, and avoid sending confidential content to external services without approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON-style status examples and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize local knowledge-base results, report execution status, and propose configuration or recovery steps.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
