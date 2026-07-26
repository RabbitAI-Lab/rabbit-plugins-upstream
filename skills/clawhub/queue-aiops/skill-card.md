## Description: <br>
Queue Aiops helps agents inspect and operate Redis and RabbitMQ deployments, including memory, latency, backlog, connection churn, policies, audited writes, and undo-aware workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and platform operators use this skill to inspect Redis caches and RabbitMQ brokers, triage memory, latency, backlog, and connection churn issues, and perform governed broker changes when appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform destructive Redis or RabbitMQ writes through MCP without a built-in approval gate. <br>
Mitigation: Start with read-only Redis ACL or RabbitMQ monitoring accounts, grant write permissions only when needed, and require explicit human approval before purge, delete-queue, Redis CONFIG SET, or policy changes. <br>
Risk: Purge and queue deletion can remove messages that undo workflows cannot restore. <br>
Mitigation: Use dry-run previews, confirm the queue state and business impact first, and reserve destructive actions for cases with explicit sign-off. <br>
Risk: QUEUE_AIOPS_MASTER_PASSWORD unlocks the encrypted broker secret store. <br>
Mitigation: Provide the master password through a private runtime environment and keep it out of shared configuration, logs, and source control. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/AIops-tools/Queue-AIops) <br>
- [Capability reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include broker observations, RCA findings, dry-run recommendations, and audit or undo guidance.] <br>

## Skill Version(s): <br>
0.4.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
