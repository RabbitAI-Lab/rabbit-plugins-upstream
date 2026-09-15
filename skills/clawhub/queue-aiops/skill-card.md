## Description:

Queue AIops helps agents inspect and operate Redis caches and RabbitMQ brokers, including memory, latency, backlog, connection churn analysis, and governed broker writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations engineers use this skill to diagnose Redis and RabbitMQ health, inspect broker state, and perform audited configuration or queue maintenance tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run an external package and perform high-impact Redis or RabbitMQ writes.

Mitigation: Pin and verify the queue-aiops package version, use a dedicated least-privilege broker account, and reserve writes for explicit maintenance windows.

Risk: There is no built-in read-only mode or approval gate for all broker operations.

Mitigation: Start with broker-side read-only permissions where possible and require the supervising agent or operator to explicitly authorize write tools.

Risk: Queue purge and delete operations can destroy messages or fail to restore deleted message contents.

Mitigation: Use dry-run previews, confirm the target queue and vhost, and avoid purge/delete unless message loss is acceptable.

Risk: Broker credentials and the master password are sensitive operational secrets.

Mitigation: Keep the master password out of broadly readable configuration, prefer encrypted storage, and enable TLS with certificate verification for broker connections.

## Reference(s):

- [Queue AIops ClawHub skill page](https://clawhub.ai/zw008/skills/queue-aiops)
- [Queue AIops project homepage](https://github.com/AIops-tools/Queue-AIops)
- [capabilities.md](artifact/references/capabilities.md)
- [cli-reference.md](artifact/references/cli-reference.md)
- [setup-guide.md](artifact/references/setup-guide.md)
- [agent-guardrails.md](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured broker observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Redis or RabbitMQ operational findings, dry-run instructions, undo guidance, and audit-oriented maintenance steps.]

## Skill Version(s):

0.9.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
