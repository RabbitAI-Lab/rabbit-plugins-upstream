## Description:

Benchmarks an agent's live memory system with retrieval metrics, confidence intervals, and ablation analysis while defaulting to local execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external OpenClaw or TinkerClaw users use this skill to measure retrieval quality, collect aggregate memory statistics, and optionally prepare a public benchmark submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional OpenAI judging can expose benchmark queries and retrieved memory excerpts to an external API.

Mitigation: Use the default local judge for sensitive memories, or review the data flow and provide explicit consent only after deciding external judging is acceptable.

Risk: Public GitHub submission can publish aggregate report data and attribution when a contributor name is supplied.

Mitigation: Inspect the complete JSON report, run the dry-run preview first, omit the contributor for anonymous reports, and publish only after explicit user approval.

Risk: Benchmarking writes a retrieval_log table into the database selected for the run.

Mitigation: Run against a copied or filtered database with --db when the live memory database should not be modified.

Risk: The built-in preview may not be a complete substitute for reviewing the full report payload.

Mitigation: Open and inspect the complete JSON report before any public submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/memory-bench-pioneer)
- [TinkerClaw repository](https://github.com/globalcaos/tinkerclaw)
- [ENGRAM context compaction paper](https://github.com/globalcaos/clawdbot-moltbot-openclaw/blob/main/docs/papers/context-compaction.md)
- [CORTEX agent memory paper](https://github.com/globalcaos/clawdbot-moltbot-openclaw/blob/main/docs/papers/agent-memory.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes benchmark rows to retrieval_log and can produce a JSON report; optional OpenAI judging and GitHub pull request submission require explicit consent.]

## Skill Version(s):

2.1.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
