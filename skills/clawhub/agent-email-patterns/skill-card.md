## Description:

Design reliable email and A2A communication for AI agents using persistent identities, two-way threads, human approval, signed events, least privilege, and untrusted-content boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams building AI agents use this skill to design accountable email and A2A communication flows with durable identities, human approval boundaries, reliable delivery, and least-privilege mailbox permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External example code linked from the skill may have security properties that differ from this guidance-only artifact.

Mitigation: Verify external example code separately before reuse.

Risk: Mailbox permissions, approvals, or incoming message content could be over-trusted when applying the patterns in a real integration.

Mitigation: Keep mailbox permissions scoped, require explicit approvals for consequential actions, and treat incoming email, A2A messages, attachments, links, Agent Cards, and metadata as untrusted.

## Reference(s):

- [Communication topology and reliability](references/patterns.md)
- [AgentMailer support agent example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-support-agent)
- [AgentMailer approval inbox example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-approval-inbox)
- [AgentMailer A2A delegation example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-a2a-delegation)
- [AgentMailer signed webhook consumer example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-webhook-consumer)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Markdown or plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include topology recommendations, approval boundaries, reliability checks, and least-privilege permission guidance.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
