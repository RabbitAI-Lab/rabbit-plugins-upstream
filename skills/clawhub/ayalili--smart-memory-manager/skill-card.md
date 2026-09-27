## Description:

Provides intelligent memory management for agents with short- and long-term memory layers, search, summarization, and optional persistence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ayalili](https://clawhub.ai/user/ayalili)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building long-running agents, chatbots, RAG applications, and assistant workflows can use this skill to add, search, summarize, clear, list, load, and save agent memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Load and save operations accept filesystem paths that can expose or overwrite local JSON files when runtime permissions are broad.

Mitigation: Run with tightly scoped Deno filesystem permissions, use a dedicated memory directory, and avoid load/save paths outside controlled application data locations.

Risk: Persisted memory entries may contain sensitive user or task context.

Mitigation: Do not store secrets or regulated data in memory entries, and review retention expectations before enabling persistence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ayalili/skills/smart-memory-manager)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON responses with memory identifiers, search/list results, status fields, and Markdown-formatted summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory entries can be persisted to JSON files when load/save actions are invoked.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
