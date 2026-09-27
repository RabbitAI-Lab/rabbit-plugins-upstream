## Description:

Helps OpenClaw agents manage local memory through archiving, scoring, consolidation, health checks, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to maintain, organize, and search local agent memory across daily notes and long-term records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The health check is described as read-only but can trigger persistent memory updates.

Mitigation: Do not rely on memory-health.py as read-only until its trace extraction uses --dry-run or otherwise avoids writes; back up memory before running it.

Risk: Memory maintenance and scheduled runs can move or change local notes.

Mitigation: Use a trusted workspace, keep backups, and review cron jobs before enabling them.

Risk: Memory text sent to a remote Ollama endpoint could leave the machine.

Mitigation: Keep Ollama endpoints local.

## Reference(s):

- [Openclaw Memory Toolkit on ClawHub](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw agent framework](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the supplied scripts may create or change local memory files.]

## Skill Version(s):

2.1.2 (source: ClawHub release metadata and CHANGELOG, released 2026-09-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
