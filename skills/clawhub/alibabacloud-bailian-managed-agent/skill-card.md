## Description:

Helps sales teams and developers explain, evaluate, provision, and integrate Alibaba Cloud Bailian Managed Agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams use the skill to recommend Bailian Managed Agents and draft customer solutions; developers use it to plan, provision, and integrate managed agents through the CLI, API, or SDKs.

### Deployment Geography for Use:

China (the documented API region is cn-beijing)

## Known Risks and Mitigations:

Risk: Provisioning or deleting cloud resources can change a customer's managed-agent workspace.

Mitigation: Start in a test workspace, show the plan, and require explicit confirmation before applying changes or deleting resources.

Risk: API keys and other credentials can be exposed through copied examples or unsafe handling.

Mitigation: Keep keys in environment variables or a secret store; review legacy examples before using them.

Risk: Active webhooks may deliver events to an unintended receiver.

Mitigation: Use a customer-controlled receiver for live delivery and verify the destination before enabling subscriptions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-bailian-managed-agent)
- [Bailian Managed Agents product documentation](https://docs.agent.bailian.aliyun.com/zh/managed-agents)
- [Managed Agents API documentation](https://docs.agent.bailian.aliyun.com/zh/api/managed-agents/introduction)
- [Integration quick reference](references/integration/api-quickstart.md)
- [Provisioning workflow](references/workflows/provision.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown explanations and proposals with runnable command, code, and configuration examples; files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud-changing actions require a reviewed plan and explicit confirmation.]

## Skill Version(s):

0.0.1 (source: server-resolved release and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
