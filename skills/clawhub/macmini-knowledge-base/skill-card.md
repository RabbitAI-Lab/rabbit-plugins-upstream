## Description:

Helps OpenClaw users set up a local Mac Mini knowledge base and RAG search workflow with document extraction, OCR fallback, catalog generation, scheduled analysis, and Feishu summary delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill on a personal Mac to install dependencies, configure local knowledge-base folders, extract text from common document formats, generate searchable summaries and catalogs, and schedule recurring Feishu delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install packages, change OpenClaw configuration, read and write knowledge-base files, and register recurring jobs.

Mitigation: Run it only on a personal Mac, use the documented dry-run and confirmation prompts, and review each proposed operation before enabling it.

Risk: Recurring jobs can automatically process local documents and send summaries through Feishu on the configured schedule.

Mitigation: Review the cron entries, confirm the Asia/Shanghai schedule is intended, and remove unwanted jobs with the documented OpenClaw cron removal command.

Risk: The Feishu webhook secret is persisted insecurely if configured.

Mitigation: Avoid saving a real webhook unless it can be protected, scoped to a dedicated destination, and rotated if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/seairteng/skills/macmini-knowledge-base)
- [Ollama Download](https://ollama.com/download)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local text, Markdown, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can register recurring cron jobs and write summaries, catalog files, cache/state files, and OCR repair reports under the local knowledge workspace.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
