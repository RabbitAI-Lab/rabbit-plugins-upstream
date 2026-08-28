## Description:

blog-mini-ljt helps agents manage a blog system through 28 REST API endpoints for articles, comments, labels, messages, moods, users, uploads, and admin actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to read and manage content in an authorized blog instance, including publishing articles, moderating comments and messages, managing tags and users, uploading files, and running admin cleanup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete live blog content, users, comments, messages, moods, articles, and uploaded files.

Mitigation: Use it only against a blog instance you own or are authorized to manage, and require manual confirmation before create, update, upload, admin, or delete operations.

Risk: If no base URL is configured, the wrapper can use its built-in remote default host.

Mitigation: Set an explicit trusted HTTPS BLOG_MINI_LJT_BASE_URL or project configuration before network operations, and avoid the built-in default remote host for testing.

Risk: Upload commands can send local files to the remote blog API.

Mitigation: Confirm the selected path, file contents, and destination before upload-file or upload-files, and do not upload sensitive local files.

Risk: Admin login and admin delete commands can perform privileged destructive changes.

Mitigation: Require explicit approval before admin-login, admin-delete-articles, or any operation using returned admin tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-mini-ljt)
- [API endpoint documentation](artifact/api-reference.md)
- [Data model schemas](artifact/schemas.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses or Markdown summaries with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can make live HTTP requests and file uploads against the configured blog API.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
