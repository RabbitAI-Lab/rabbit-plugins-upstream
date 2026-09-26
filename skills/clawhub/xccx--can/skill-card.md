## Description:

Agent and MCP integration for stamping data that flows through pipes so agents can verify, name, and log tool outputs locally.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xccx](https://clawhub.ai/user/xccx)

### License/Terms of Use:

Public Domain

## Use Case:

Developers and agent builders use CAN to create local audit trails for MCP and other tool outputs by recording a timestamp, content hash, and human-readable name. Agents can use those entries to verify cached results before reusing them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local logs or caches may retain private reports, customer data, credentials, proprietary API responses, or regulated content.

Mitigation: Use explicit opt-in logging, avoid storing raw tool outputs by default, and define retention and deletion practices.

Risk: Human-readable WHAT values can expose sensitive context even when payloads are hashed.

Mitigation: Redact sensitive WHAT values before writing entries to the CAN index.

Risk: Local CAN files may be readable by other processes or users on the same machine.

Mitigation: Restrict permissions on ~/.can and review local access controls before using CAN with sensitive data.

## Reference(s):

- [CAN Skill on ClawHub](https://clawhub.ai/xccx/skills/can)
- [CAN Homepage](https://github.com/xccx/can)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local timestamp, hash, name, and log-entry patterns for agent-managed data.]

## Skill Version(s):

1.9.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
