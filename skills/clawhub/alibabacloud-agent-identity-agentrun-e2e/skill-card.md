## Description:

Guides an agent through deploying, verifying, and cleaning up an Alibaba Cloud AgentRun runtime governed by AgentIdentity, including identity-provider setup, credential chains, authorization checks, and tool wiring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to stand up an AgentRun-hosted Alibaba Cloud agent, verify end-user authentication and authorization behavior, test credential injection for local and remote tools, and remove resources from the trial.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or modify local tooling such as conda, Python packages, aliyun CLI plugins, and persistent aliyun CLI settings.

Mitigation: Review AUTO commands before execution and run in a controlled development environment where toolchain changes are acceptable.

Risk: The skill uses the configured aliyun CLI profile to create, modify, and delete Alibaba Cloud resources.

Mitigation: Use a test account or a tightly scoped RAM policy, and verify the active aliyun account before running cloud phases.

Risk: The workflow attaches an OSS read policy to the runtime role and creates credential providers, policy sets, buckets, objects, runtimes, and MCP tools.

Mitigation: Review requested resource names and permissions at each checkpoint, then follow the cleanup checklist for resources that require console removal.

Risk: OIDC ID tokens and DingTalk MCP URLs are sensitive operational secrets during the verification flow.

Mitigation: Do not paste secrets into chat or logs; treat ID tokens and DingTalk MCP URLs as secrets and rotate or remove test resources after use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-agent-identity-agentrun-e2e)
- [AgentRun Runtime Deployment Field Guide](references/agentrun-deploy.md)
- [Console Guides](references/console-guides.md)
- [RAM Permissions Required by This Skill](references/ram-policies.md)
- [Testing Checklist](references/testing-checklist.md)
- [Cleanup Guide](references/cleanup.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Packaging Guide](references/packaging.md)
- [Alibaba Cloud Agent Identity Dev Kit](https://github.com/aliyun/agent-identity-dev-kit)
- [Alibaba Cloud CLI Releases](https://github.com/aliyun/aliyun-cli/releases)
- [DingTalk MCP](https://mcp.dingtalk.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and structured progress prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes AUTO command blocks, WAIT checkpoints for user actions, and cleanup guidance.]

## Skill Version(s):

0.0.1-beta.1 (source: server release metadata; artifact metadata lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
