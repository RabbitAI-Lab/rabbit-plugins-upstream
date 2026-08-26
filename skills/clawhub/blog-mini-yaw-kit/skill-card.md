## Description:

Manages a FastAPI Blog System API across articles, labels, users, comments, messages, moods, uploads, admin actions, and health checks through no-auth command-driven workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to inspect and manage a Blog System API, including publishing, updating, uploading, deleting, and checking service health from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, upload, delete, and bulk-delete public blog content.

Mitigation: Require explicit user approval before uploads, hard deletes, and admin-delete-articles, and confirm the target base URL before running commands.

Risk: Public no-auth endpoints can affect whichever trusted blog API is configured.

Mitigation: Use the skill only with trusted Blog System API instances and avoid setting unnecessary BLOG_MINI_YAW_KIT_* environment values.

## Reference(s):

- [API endpoint reference](artifact/api-reference.md)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-mini-yaw-kit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown, with shell command examples and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a configurable BLOG_MINI_YAW_KIT_BASE_URL and JSON or Markdown command output.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
