## Description:

Helps OpenClaw agents extract, archive, score, consolidate, check, and search persistent memories using a local-first pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users manage agent memories across session extraction, archiving, scoring, consolidation, health checks, and hybrid search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory excerpts or explicit session transcripts may be sent to Ollama cloud when cloud access is configured.

Mitigation: For sensitive content, set TRACE_LLM_LOCAL_ONLY=1, keep OLLAMA_URL on localhost, and review any --session-file input.

Risk: Scheduled jobs and --fix, --force, or --apply options can move or rewrite memory files.

Mitigation: Review scheduled commands and use previews and backups before enabling file-changing operations.

## Reference(s):

- [Openclaw Memory Toolkit on ClawHub](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw agent framework](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON reports]

**Output Format:** [Markdown guidance, shell commands, and local reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update memory files and a local search index when write operations are enabled.]

## Skill Version(s):

3.1.1 (source: ClawHub release and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
