## Description:

Hybrid memory pipeline for OpenClaw agents covering extraction, archiving, temporal decay scoring, consolidation, health checks, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate a local-first memory lifecycle for OpenClaw agents, including extracting durable facts from notes or session transcripts, ranking memory items, suggesting consolidations, and querying memory with lexical and vector search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local memory files, skill notes, configuration notes, and optional session transcripts may be read, indexed, embedded, and written back to disk.

Mitigation: Review the workspace before installation or indexing, keep Ollama endpoints local, and run preview or dry-run modes before enabling scheduled writes.

Risk: Some commands can mutate files or skip confirmation when force-style flags are used.

Mitigation: Avoid --force, --yes, and similar automation flags unless current backups exist and the workspace is trusted.

Risk: The included index report may contain publisher-specific benchmark or workspace data.

Mitigation: Treat the report as sensitive release evidence rather than generic public documentation, and avoid redistributing its contents unless reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [README.md](artifact/README.md)
- [OpenClaw project](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands, local Python scripts, JSON reports, and SQLite search indexes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and modifies local workspace memory files; optional local Ollama calls can process memory text for extraction, summaries, and embeddings.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
