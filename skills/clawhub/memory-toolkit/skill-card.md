## Description:

Helps OpenClaw agents extract, organize, score, consolidate, and search local memory, with optional language-model assistance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use the toolkit to maintain agent memories, identify stale or conflicting facts, and retrieve relevant notes through hybrid search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory or session excerpts may leave the device when cloud extraction is enabled.

Mitigation: Use TRACE_LLM_LOCAL_ONLY=1 for sensitive use and review any --session-file input before extraction.

Risk: Memory files can be moved or rewritten by corrective and forced operations.

Mitigation: Review changes first, retain backups, and reserve --force or destructive --fix modes for trusted automation.

Risk: Local model requests process potentially sensitive memory content.

Mitigation: Keep Ollama endpoints on localhost and grant memory-directory access only when appropriate.

## Reference(s):

- [Openclaw Memory Toolkit release](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw framework](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON reports]

**Output Format:** [Markdown guidance and commands; local JSON reports and memory files when scripts run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some commands update local memory files or indexes; optional language-model extraction can transmit excerpts to Ollama cloud.]

## Skill Version(s):

3.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
