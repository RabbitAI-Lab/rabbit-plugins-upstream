## Description:

A Blog System REST API management skill that helps agents manage articles, labels, users, comments, messages, moods, uploads, and health checks through 28 CLI subcommands without authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent administer a Blog System API, including reading content, publishing or updating posts, managing comments and messages, handling uploads, and checking service health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, or permanently delete public blog content through an unauthenticated API.

Mitigation: Install it only for Blog System instances you control, review mutable commands before execution, prefer soft delete where possible, and require explicit approval before hard-delete operations.

Risk: The skill can upload local files and delete uploaded files.

Mitigation: Review file paths and filenames before upload or deletion, and restrict use to files intended for the target blog system.

Risk: The skill falls back to a built-in HTTP base URL when no target API is configured.

Mitigation: Set BLOG_MANAGER_KIT_BASE_URL or project configuration explicitly for the intended target before running commands.

Risk: Issue or PR comments generated after operations may expose API results outside the blog system.

Mitigation: Review generated comments for sensitive content before posting them to external collaboration systems.

## Reference(s):

- [Blog System API endpoint reference](api-reference.md)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-manager-kit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls]

**Output Format:** [JSON or Markdown responses with shell command examples and API result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses BLOG_MANAGER_KIT_BASE_URL or project configuration for the target API base URL; defaults to a built-in HTTP endpoint when not configured.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
