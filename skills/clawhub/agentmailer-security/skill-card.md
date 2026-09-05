## Description:

Design or review secure AgentMailer integrations, authorization boundaries, prompt-injection defenses, credential handling, webhook verification, and safe communication workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to assess AgentMailer workflows for authorization boundaries, untrusted communication, credential exposure, webhook replay, duplicate effects, and unsafe observability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat advisory review guidance as proof that an AgentMailer integration is production-safe.

Mitigation: Use the skill as a security-review aid and separately review the actual integration and any linked example code before adoption.

## Reference(s):

- [Authorization model](references/authorization.md)
- [AgentMailer integration threat model](references/threat-model.md)
- [Approval inbox example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-approval-inbox)
- [Signed webhook consumer example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-webhook-consumer)
- [x402 payment agent example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-x402-payment-agent)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Markdown guidance and review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No direct execution, data access, or mutation behavior.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
