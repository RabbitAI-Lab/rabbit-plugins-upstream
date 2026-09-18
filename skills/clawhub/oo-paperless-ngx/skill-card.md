## Description:

Operate Paperless-ngx through the OOMOL oo CLI connector for reading, creating, updating, deleting, searching, sharing, and managing documents and related metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Paperless-ngx documents, metadata, workflows, mail ingestion, users, tasks, and related administrative settings through an OOMOL-connected account. It is suited for agent-assisted document management where read operations can run directly and state-changing operations require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands for the oo CLI.

Mitigation: Review the setup path before installing, prefer verified vendor documentation or signed/package-manager sources, and do not allow an agent to run installer pipe commands automatically.

Risk: The skill can perform state-changing and destructive Paperless-ngx operations, including deletion, user management, public share links, email, and profile changes.

Mitigation: Use a Paperless-ngx account with only the permissions the agent should exercise, and require explicit user confirmation for write or destructive payloads before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-paperless-ngx)
- [Paperless-ngx Documentation](https://docs.paperless-ngx.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions may return JSON responses, task identifiers, or temporary connector file URLs depending on the Paperless-ngx operation.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
