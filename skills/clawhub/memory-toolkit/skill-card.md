## Description:

Helps OpenClaw agents extract, organize, search, and maintain durable memory across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use the toolkit to preserve useful facts from conversations, search prior memories, resolve conflicting facts, and maintain their memory records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maintenance operations can rewrite local memory data.

Mitigation: Back up memory records and review changes before running write-enabled operations.

Risk: Helper scripts can process sensitive OpenClaw session transcripts and index memory content.

Mitigation: Review transcript and memory inputs before processing or indexing them; restrict access to stored results.

Risk: Cloud LLM use can send memory or ontology excerpts off the machine.

Mitigation: Set TRACE_LLM_LOCAL_ONLY=1 for privacy-sensitive use; enable TRACE_LLM_ALLOW_CLOUD=1 only after accepting external transmission.

## Reference(s):

- [Openclaw Memory Toolkit on ClawHub](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw project](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Memory notes, search results, and health or consolidation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some maintenance actions update local memory records.]

## Skill Version(s):

4.0.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
