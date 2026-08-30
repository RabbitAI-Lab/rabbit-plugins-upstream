## Description:

Manages all 32 Blog System (FastAPI) API endpoints for articles, tags, users, comments, messages, moods, uploads, health checks, blog pages, and admin actions through CLI subcommands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect, create, update, upload, and delete content in an authorized Blog System deployment. It is suited for operational blog administration through documented API calls and shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, upload, and delete live public content, including admin bulk deletion actions.

Mitigation: Install only for blog systems the user owns or is authorized to administer, and require manual review before upload, delete, hard-delete, user creation, or admin bulk deletion actions.

Risk: A misconfigured base URL could send actions to the wrong blog system.

Mitigation: Set the base URL explicitly and verify the health-check target before performing write operations.

Risk: Weak or default admin credentials increase the impact of admin operations.

Mitigation: Avoid default admin credentials and do not store unnecessary prefixed secrets in project configuration or environment variables.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-mini-kit-mys)
- [API endpoint index](references/api-reference.md)
- [Articles API](references/articles.md)
- [Tags API](references/tags.md)
- [Users API](references/users.md)
- [Comments API](references/comments.md)
- [Messages API](references/messages.md)
- [Moods API](references/moods.md)
- [Uploads API](references/uploads.md)
- [Health check API](references/health.md)
- [Blog pages API](references/pages.md)
- [Admin API](references/admin.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON or Markdown responses with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute live API calls against the configured blog system and report operation results.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
