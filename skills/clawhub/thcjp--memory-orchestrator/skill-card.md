## Description:

记忆编排器 helps AI agents manage four memory layers, retrieve context with keyword, semantic, or hybrid search, generate summaries, monitor memory health, and handle concurrent memory writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent builders use this skill to manage an AI agent's working, short-term, long-term, and important memories, retrieve relevant context, generate summaries, and monitor memory health across longer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to execute shell commands or write persistent memory files.

Mitigation: Use it only in environments where local command execution and retained memory files are acceptable, and require explicit confirmation before shell command execution.

Risk: Persistent memory can retain personal, work, or secret data longer than intended.

Mitigation: Avoid storing secrets, review retained memory content, and require explicit confirmation for cleanup, deletion, and archival actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/memory-orchestrator)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce persisted memory files, retrieval results, structured summaries, health reports, cleanup logs, and configuration confirmations.]

## Skill Version(s):

1.0.3 (source: evidence.release.version; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
