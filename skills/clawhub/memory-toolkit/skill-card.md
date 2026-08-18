## Description:

Openclaw Memory Toolkit provides a local-first memory management pipeline for OpenClaw agents, covering archiving, scoring, consolidation advice, health checks, ontology structure, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to maintain OpenClaw memory workspaces with local scripts for lifecycle management, retrieval, scoring, consolidation review, and health reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory workspace files can be moved, rewritten, indexed, or summarized by the bundled scripts.

Mitigation: Review planned operations first, prefer dry-run modes, keep backups, and avoid unattended --force usage in cron or agent automation.

Risk: Memory text may be sent to the configured Ollama endpoint for LLM summaries or embeddings.

Mitigation: Keep OLLAMA_URL and embedding endpoints on localhost unless the workspace contents are approved for that destination.

Risk: Hybrid search can index memory files that may contain sensitive user or project context.

Mitigation: Review the workspace before batch indexing and exclude sensitive files even when scanner skip patterns are present.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [Publisher profile](https://clawhub.ai/user/mistermijarvis)
- [OpenClaw](https://github.com/openclaw/openclaw)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Ontology schema](artifact/ontology/schema.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and local file outputs such as JSON reports, SQLite indexes, and memory workspace updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first operation; optional Ollama and sqlite-vec integrations; script behavior depends on the configured WORKSPACE path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
