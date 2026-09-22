## Description:

Creates and manages Docker sandbox environments so agents can run project commands and code in an isolated container workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create Docker sandboxes, execute commands, and run agents against project workspaces while reducing direct host exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause agents to run powerful Docker commands or operate on project files more broadly than users expect.

Mitigation: Review proposed commands before execution and use a temporary or read-only workspace for untrusted code.

Risk: Mounted project directories may expose sensitive files to sandbox workflows.

Mitigation: Avoid mounting sensitive project directories, credentials, or secrets into the sandbox.

Risk: Advertised security scanning or API features may not have concrete implementation details in the evidence.

Mitigation: Do not rely on those features unless the publisher provides verifiable implementation details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/docker-sandbox)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash command examples and occasional JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce sandbox names or IDs, command output, status summaries, logs, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
