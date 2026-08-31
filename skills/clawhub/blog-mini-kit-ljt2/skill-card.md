## Description:

A blog API management skill for checking health, managing articles, labels, users, comments, messages, moods, and uploaded files through a configured public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage a target blog service through its documented REST endpoints. It supports read operations, content creation and updates, deletion and restore workflows, file upload management, and health checks after the target base URL is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make live unauthenticated changes, deletions, and uploads against the configured blog API.

Mitigation: Verify the base URL before each use and require human confirmation before delete, upload, create, or update actions.

Risk: File upload commands may send local files to the target service.

Mitigation: Avoid uploading sensitive local files and confirm each file path before running upload commands.

Risk: The dependency constraint allows older requests versions.

Mitigation: Review and update the requests dependency constraint before production deployment.

## Reference(s):

- [API endpoint reference](artifact/api-reference.md)
- [Test variables and cases](artifact/test-vars.json)
- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/blog-mini-kit-ljt2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON by default, with optional Markdown output and human-readable status or error text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a configured BLOG_MINI_KIT_LJT2_BASE_URL or equivalent project configuration before API calls.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
