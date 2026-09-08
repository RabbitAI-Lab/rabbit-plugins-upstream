## Description:

A blog content publishing tool for managing a blog system's REST APIs for articles, tags, users, comments, messages, moods, file uploads, and health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect and manage an authorized blog REST API, including content, comments, users, uploads, and health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated write, upload, user creation, and bulk-delete actions can modify or remove blog data.

Mitigation: Install only for controlled or private blog APIs that the operator is authorized to manage, and add authentication and authorization before production use.

Risk: Delete, upload, and admin actions may cause unintended data loss or file exposure.

Mitigation: Require explicit confirmation for destructive or upload actions, add dry-run or preview behavior for bulk deletion, and restrict uploads to intended files and directories.

## Reference(s):

- [Blog System REST API Reference](references/api-reference.md)
- [Test Cases](templates/test-vars.json)
- [ClawHub Skill Page](https://clawhub.ai/yangaiwu/skills/blog-kimi-test-kit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses BLOG_KIMI_TEST_KIT_BASE_URL for target API configuration.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
