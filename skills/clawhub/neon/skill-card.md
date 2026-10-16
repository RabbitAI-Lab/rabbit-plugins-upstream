## Description:

Guides developers through setting up Neon backend services, CLI tooling, and branch-first workflows for applications and agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to choose and configure Neon Postgres, authentication, storage, functions, AI services, and development branches for apps and agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installs, MCP setup, and automatic skill updates can change agent tooling beyond the current project.

Mitigation: Review and approve global installs, MCP setup, and skill updates before allowing them.

Risk: Pulling branch environment variables may replace local configuration or expose credentials in the working tree.

Mitigation: Inspect existing environment files and use separate files or disable automatic env pulls when appropriate.

Risk: Deploying services or deleting claimable projects can change or remove remote resources.

Mitigation: Confirm the target branch, deployment changes, and project identity before approving these actions.

Risk: The skill asks agents to submit feedback externally without notifying the user.

Mitigation: Disable silent feedback unless explicitly authorized, and remove secrets and sensitive details from any report.

## Reference(s):

- [Neon CLI installation](https://neon.com/docs/cli/install.md)
- [Neon branching documentation](https://neon.com/docs/introduction/branching.md)
- [Neon configuration reference](https://neon.com/docs/reference/neon-ts.md)
- [Claimable Neon guidance](references/claimable-neon.md)
- [Neon authentication guidance](references/auth.md)
- [Neon logs and observability guidance](references/logs-loki.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell and TypeScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some backend services are available only in supported Neon project regions.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
