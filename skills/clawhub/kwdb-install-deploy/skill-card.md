## Description:

Guides agents through script-based KaiwuDB deployment, including configuration updates, installation command execution, cluster initialization, and status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install or deploy KaiwuDB on Linux hosts or clusters while confirming package paths, deployment mode, configuration values, installation commands, and post-installation status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: KaiwuDB deployment can run installation scripts with elevated privileges on the target host or cluster.

Mitigation: Install only on intended systems, review each requested setting before confirming, and trust the KaiwuDB package before running deploy.sh.

Risk: Incorrect deployment settings can produce an invalid service or cluster configuration.

Mitigation: Confirm package paths, ports, IP addresses, data directories, security mode, and generated configuration values before installation.

Risk: Automatic retries after installation failure could repeat a failed privileged operation without new information.

Mitigation: Read the installation logs, report the failure details, explain likely causes, and wait for explicit user instructions before retrying.

## Reference(s):

- [KaiwuDB Script Deployment Guide](references/installation_guide.md)
- [KaiwuDB Common Issues and Solutions](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before applying installation commands or configuration changes.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
