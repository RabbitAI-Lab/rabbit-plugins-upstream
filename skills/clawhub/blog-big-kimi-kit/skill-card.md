## Description:

Helps an agent manage a FastAPI-backed blog through documented endpoints for articles, tags, users, comments, messages, moods, file uploads, and health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to let an agent inspect and administer a configured blog API, including content publishing, moderation, user creation, and upload management. It is intended for controlled use against a trusted base URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can create, update, delete, restore, and upload content through an unauthenticated blog API.

Mitigation: Use only with a trusted base URL, require human confirmation for create/update/delete/upload operations, and prefer server-side authorization before production use.

Risk: File upload commands can send local files from paths supplied to the agent.

Mitigation: Confirm the exact local file path and intended destination before asking the agent to upload files.

Risk: The dependency declaration allows older patched states through a broad requests version range.

Mitigation: Pin requests to a current patched version before production deployment.

## Reference(s):

- [API Reference](api-reference.md)
- [Test Variables](test-vars.json)
- [ClawHub Skill Page](https://clawhub.ai/yangaiwu/skills/blog-big-kimi-kit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance]

**Output Format:** [JSON by default, with optional Markdown tables and issue-comment summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a configured BLOG_BIG_KIMI_KIT_BASE_URL and 30-second HTTP timeouts.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
