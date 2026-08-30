## Description:

Manage Blog System API v1.0.0 via 27 CLI subcommands covering articles, tags, users, comments, messages, moods, uploads, and health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer a Blog System API instance through CLI subcommands for content, users, comments, messages, moods, uploads, and health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, restore, and upload live blog data through administrative API calls.

Mitigation: Use it only against a Blog System API instance you control, and require explicit user confirmation before mutating commands.

Risk: The target API is documented as unauthenticated, increasing impact if the base URL points to an exposed or unintended instance.

Mitigation: Prefer private-network or authenticated deployments, and verify BLOG_MANAGER_BASE_URL before running any command.

Risk: Hard-delete and upload deletion commands can permanently remove content or files.

Mitigation: Confirm identifiers and filenames from list or get commands before deletion, and prefer soft deletion where available.

## Reference(s):

- [Blog System API v1.0.0 endpoint documentation](references/api-reference.md)
- [Test case definitions](templates/test-vars.json)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-manager)
- [Publisher profile](https://clawhub.ai/user/yangaiwu)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Markdown, JSON]

**Output Format:** [CLI output with JSON and Markdown renderings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BLOG_MANAGER_BASE_URL to target the Blog System API instance.]

## Skill Version(s):

2.1.2 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0 for the Blog System API wrapper)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
