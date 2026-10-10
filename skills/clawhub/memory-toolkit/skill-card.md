## Description:

Helps OpenClaw agents retain useful facts across sessions through extraction, search, contradiction resolution, and memory maintenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to find, preserve, organize, and reconcile agent memories across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing or capturing session transcripts may expose private memories; redaction is best-effort.

Mitigation: Review the data being indexed and use transcript capture only for sessions you intend to process.

Risk: Memory excerpts may be sent to Ollama cloud when credentials are configured.

Mitigation: For sensitive data, set TRACE_LLM_LOCAL_ONLY=1 and keep OLLAMA_URL and OLLAMA_EMBED_URL loopback-only.

Risk: Automated maintenance and forced operations can change or archive memory data.

Mitigation: Review cron jobs and confirm backups before running mutating commands, especially with --force.

## Reference(s):

- [Openclaw Memory Toolkit on ClawHub](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw agent framework](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and CLI text or JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some operations update memory files and search indexes.]

## Skill Version(s):

3.6.1 (source: ClawHub release, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
