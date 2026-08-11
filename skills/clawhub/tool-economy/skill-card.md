## Description:

Minimize tool call overhead by teaching agents to batch independent calls, avoid redundant reads, cache session results, prefer stronger commands, and track a tool budget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to reduce token and latency overhead in multi-step agent workflows while preserving correctness. It provides checklists, anti-patterns, and an optional session analyzer for evaluating tool-call efficiency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may over-optimize for fewer tool calls and skip a needed freshness, correctness, or safety check.

Mitigation: Require re-checks when information may have changed or when correctness, safety, or user impact depends on verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/tool-economy)
- [Server-Resolved GitHub Repository](https://github.com/voronindenis5/tool-economy)
- [Publisher Profile](https://clawhub.ai/user/voronindenis5)
- [Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs)
- [Batching Independent Tool Calls](references/batching.md)
- [Tool Budgeting](references/budgeting.md)
- [Anti-Patterns Catalog](references/antipatterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code]

**Output Format:** [Markdown guidance with inline shell commands and an optional Python analyzer script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional JSON session-log input for local efficiency analysis.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
