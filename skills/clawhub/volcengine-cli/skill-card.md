## Description: <br>
Create and manage Volcengine cloud resources using the Volcengine CLI (`ve` command), with guidance for authentication, API discovery, service-specific operations, and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect, create, modify, and delete Volcengine cloud resources through `ve` and bundled helper scripts while following confirmation and credential-safety guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad authenticated Volcengine authority can create, modify, delete, or incur cost for cloud resources. <br>
Mitigation: Use temporary or least-privilege credentials, verify the current identity and region, prefer DryRun when available, and require explicit approval for write or destructive commands. <br>
Risk: Extension APIs can reach high-impact operations outside the ordinary `ve` command surface. <br>
Mitigation: Review the API name, parameters, and impact summary before execution; be especially cautious with billable actions, domain registration, IoT/device actions, and security workflow calls. <br>
Risk: Login and credential flows may expose or replace active sessions if handled loosely. <br>
Mitigation: Use the bundled remote-login helper, avoid printing secrets, prefer temporary credentials, and do not read or echo credential files or tokens. <br>


## Reference(s): <br>
- [Volcengine CLI GitHub Releases](https://github.com/volcengine/volcengine-cli/releases) <br>
- [ALB Service Notes](references/alb.md) <br>
- [CLB Service Notes](references/clb.md) <br>
- [Common Error Handling](references/common-errors.md) <br>
- [CR Service Notes](references/cr.md) <br>
- [DNS and Edge Service Notes](references/dns-edge.md) <br>
- [EBS Service Notes](references/ebs.md) <br>
- [ECS Service Notes](references/ecs.md) <br>
- [Extended APIs](references/extend-apis.md) <br>
- [IAM Service Notes](references/iam.md) <br>
- [KMS Service Notes](references/kms.md) <br>
- [Message Queue Service Notes](references/mq.md) <br>
- [NAT Gateway Service Notes](references/natgateway.md) <br>
- [Observability Service Notes](references/observability.md) <br>
- [RDS Service Notes](references/rds.md) <br>
- [Redis Service Notes](references/redis.md) <br>
- [Storage Service Notes](references/storage.md) <br>
- [veFaaS Service Notes](references/vefaas.md) <br>
- [VKE Service Notes](references/vke.md) <br>
- [VPC Service Notes](references/vpc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should preserve credential redaction and request confirmation before write or destructive cloud operations.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
