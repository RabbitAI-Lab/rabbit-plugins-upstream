## Description:

Sets up a local Mac Mini knowledge base and RAG search workflow with document extraction, OCR fallback, scheduled analysis, catalog generation, and Feishu summary delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically capable Mac users use this skill to install and operate a local OpenClaw knowledge base, configure Ollama embeddings, analyze local documents, generate searchable catalogs, and schedule daily summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad host command execution through exec/process and runs local shell and Python workflows.

Mitigation: Review the scripts before installation, enable exec/process only for a trusted workspace, and keep host permissions scoped to the intended knowledge-base directories.

Risk: Scheduled background processing can repeatedly analyze local documents without further prompts.

Mitigation: Confirm cron entries, timeouts, exclusions, and backup or removal steps before enabling unattended daily processing.

Risk: Feishu delivery can send document-derived summaries outside the local machine.

Mitigation: Run setup without a Feishu user ID until scripts and destination accounts are reviewed, and avoid processing confidential directories unless delivery policy is approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/macmini-knowledge-base)
- [Ollama download](https://ollama.com/download)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration snippets, and Python code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides local file analysis, script deployment, OpenClaw configuration, cron registration, and Feishu summary delivery.]

## Skill Version(s):

1.4.1 (source: server release metadata, _meta.json, and CHANGELOG released 2026-08-12; SKILL.md frontmatter says 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
