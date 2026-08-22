## Description:

Manages Blog System API v1.0.0 content, users, comments, messages, moods, uploads, and health checks through CLI subcommands that return JSON or Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect and manage a Blog System API from an agent-accessible command line. It supports routine content administration, uploads, health checks, and table or JSON reporting for blog resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload, create, update, and delete public blog content against a dynamically selected unauthenticated API.

Mitigation: Verify BLOG_TOOLKIT_BASE_URL before use, prefer non-production targets or current backups, and review destructive or publishing commands before execution.

Risk: Mutable commands do not provide confirmation guardrails before changing blog content or uploaded files.

Mitigation: Add or require confirmations for create, update, upload, and delete operations before using the skill for production administration.

Risk: The release guidance calls out the requests dependency range as needing a safer version policy.

Mitigation: Review and tighten the requests version range before deployment in environments with security or compliance requirements.

## Reference(s):

- [Blog System API v1.0.0 endpoint reference](artifact/api-reference.md)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-toolkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON responses or Markdown tables, with shell command examples and configuration notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Blog System base URL from project knowledge, BLOG_TOOLKIT_BASE_URL, or interactive input; API calls use a 30 second timeout.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
