## Description:

Qwencloud Deploy deploys, publishes, updates, and cleans up local projects or Git repositories on Alibaba Cloud International using ROS-managed cloud resources, health checks, deployment-state recording, hot updates, and optional domain and HTTPS setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuixiaoyang123](https://clawhub.ai/user/cuixiaoyang123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to put a local project or Git repository online on Alibaba Cloud International, update an existing deployment, clean up its cloud stack, or add domain and HTTPS support. It is intended for deployments where the user has valid Alibaba Cloud CLI credentials and confirms cost-bearing resource creation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete cloud resources and can manage DNS/domain settings.

Mitigation: Use a narrowly scoped Alibaba Cloud RAM role, review the planned resources and hourly USD cost, and require explicit confirmation before resource creation or deletion.

Risk: Hot updates and health checks use Cloud Assistant and root-level remote command authority on deployed ECS instances.

Mitigation: Deploy only trusted projects, inspect uploaded archives and generated commands before execution, and avoid granting broader permissions than the deployment requires.

Risk: Credentials, passwords, signed URLs, and deployment state can be exposed through chat, command history, process arguments, or project files.

Mitigation: Keep secrets out of chat and project directories, prefer OAuth or environment variables, restrict temporary parameter files to mode 600, delete temporary files after use, and rotate any exposed credential.

Risk: The security guidance flags Docker Compose deployments, unpinned binary downloads, and archive/start-command hardening as areas needing caution.

Mitigation: Avoid untrusted repositories, review Docker Compose files and startup commands, and defer high-trust production use of those paths until the hardening issues are fixed.

## Reference(s):

- [Qwencloud Deploy Skill Definition](artifact/SKILL.md)
- [Environment Check](artifact/reference/deploy/01_env_check.md)
- [Create Stack](artifact/reference/deploy/11_create_stack.md)
- [Hot Update](artifact/reference/hotfix/update_app.md)
- [Delete / Cleanup](artifact/reference/cleanup/delete_stack.md)
- [HTTPS Setup](artifact/reference/https/https_setup.md)
- [RAM Policies](artifact/reference/rules/ram_policies.md)
- [Alibaba Cloud CLI install guide](https://www.alibabacloud.com/help/en/cli/install-update-alibaba-cloud-cli)
- [Alibaba Cloud OSS console](https://oss.console.aliyun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON state output, generated ROS configuration, and deployment state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a public service URL or domain, cost summary, deployment state file, and next-step guidance after successful deployment.]

## Skill Version(s):

2.2 (source: frontmatter); ClawHub release 1.0.3

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
