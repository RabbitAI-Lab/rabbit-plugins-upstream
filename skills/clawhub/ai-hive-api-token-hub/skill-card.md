## Description:

AI大模型专家API中转与Token Hub企业网关，为 AI 工具、中转站、SaaS、代理商和企业内部平台设计多模型 API 接入、租户隔离、密钥治理、额度计费、成本/速度/成功率路由、任务幂等、审计和故障切换。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, SaaS operators, AI API resellers, and enterprise teams use this skill to plan authorized multi-model API gateways, Token Hub governance, routing, metering, billing, audit, and failover workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill could be misused to plan integrations that route around provider terms, billing, quotas, regional restrictions, or key ownership boundaries.

Mitigation: Use it only for legitimate, authorized integrations and confirm upstream contracts, tenant boundaries, billing rules, quota policies, and regional constraints before implementation.

Risk: Gateway planning can expose or mishandle API tokens if complete credentials are stored in tickets, chats, logs, screenshots, skills, or code repositories.

Mitigation: Store only irreversible token digests or controlled ciphertext, show full token values once, redact logs, define rotation and revocation procedures, and audit token usage.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Code]

**Output Format:** [Markdown guidance with architecture, policy, protocol, and rollout recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces planning artifacts such as system boundaries, tenant and data-flow descriptions, token and quota policy, routing rules, billing rules, monitoring metrics, audit controls, and rollout plans.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
