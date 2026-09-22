## Description:

The skill should be used when the user asks about Alibaba Cloud AgentLoop platform for onboarding applications into observability, managing Datasets, building pipelines, and evaluating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to route Alibaba Cloud AgentLoop requests into focused workflows for application observability onboarding, Dataset management, Pipeline creation, and evaluation. It helps produce CLI commands, JSON specifications, configuration guidance, and verification steps for AgentLoop operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud and application changes can be made when the skill runs with real Alibaba Cloud credentials.

Mitigation: Use a least-privilege Aliyun profile, confirm all mutation parameters, and require explicit previews before cloud mutations or Kubernetes/application changes.

Risk: Install and upgrade paths may involve CLI plugins or shell setup scripts.

Mitigation: Approve plugin or CLI installs separately, prefer organization-approved update paths, and avoid curl-to-bash execution.

Risk: AI pipeline nodes may process sensitive prompts, tool arguments, logs, secrets, or PII.

Mitigation: Do not run AI pipeline nodes on sensitive data unless that processing is allowed, and use synthetic previews when real payloads would expose sensitive content.

Risk: Global deduplication can create persistent Dataset state that affects future runs.

Mitigation: Treat global dedup as persistent state and validate Dataset reconciliation before relying on the processed output.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/sdk-team/skills/alibabacloud-agentloop-management)
- [AgentLoop application onboarding](references/onboarding.md)
- [Application Monitoring module](references/apm.md)
- [AI observability module](references/ai.md)
- [AgentLoop evaluation workflow](references/evaluation/evaluation.md)
- [AgentLoop Dataset workflow](references/dataset/dataset.md)
- [AgentLoop Pipeline workflow](references/pipeline/pipeline.md)
- [Skill-wide RAM policy reference](references/ram-policies.md)
- [AgentLoop Experience skill](https://skills.aliyun.com/skills/alibabacloud-agentloop-experience)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands, JSON specifications, configuration snippets, and verification summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud operation plans, dry-run previews, request IDs, and redacted credential status; secret values should not be printed.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
