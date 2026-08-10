## Description:

Qwencloud-deploy helps agents deploy, update, clean up, and optionally configure HTTPS for local projects or Git repositories on Alibaba Cloud International using ROS, ECS, OSS, and optional RDS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuixiaoyang123](https://clawhub.ai/user/cuixiaoyang123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to publish a local project or Git repository to Alibaba Cloud International, then manage hot updates, cleanup, and optional domain or HTTPS setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create billable cloud resources such as ECS, EIP, OSS, and optional RDS.

Mitigation: Use a least-privilege Alibaba Cloud account, verify region and resource plans, and require explicit cost confirmation before resource creation.

Risk: Cleanup and redeploy operations can delete cloud resources and database data.

Mitigation: Read deletion prompts carefully, back up data before cleanup or redeploy, and keep the deployment state file until cleanup is complete.

Risk: Domain purchase and HTTPS setup may require registrant information and DNS changes.

Mitigation: Avoid the domain-purchase flow unless comfortable sending registrant details to Alibaba Cloud, and verify DNS and certificate changes before relying on them.

Risk: The skill can execute remote commands through Alibaba Cloud tooling during deployment, update, and troubleshooting.

Mitigation: Review generated actions, use constrained credentials, and monitor remote command output and logs during deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cuixiaoyang123/skills/qwencloud-deploy)
- [Alibaba Cloud CLI install guide](https://www.alibabacloud.com/help/en/cli/install-update-alibaba-cloud-cli)
- [Deployment workflow reference](artifact/reference/deploy/01_env_check.md)
- [Cleanup reference](artifact/reference/cleanup/delete_stack.md)
- [HTTPS setup reference](artifact/reference/https/https_setup.md)
- [Interaction and cost rules](artifact/reference/rules/rule_interaction.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with shell command execution and generated deployment configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a running cloud service URL, a .qwencloud-deploy state file, a local credentials/state companion file, cost summaries, and next-step guidance.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact SKILL.md frontmatter states 2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
