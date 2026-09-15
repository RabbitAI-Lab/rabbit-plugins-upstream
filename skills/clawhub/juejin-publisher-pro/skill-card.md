## Description:

Automates Juejin article drafting, cover generation, column attachment, publishing, and review-status checks, with semi-automated Zhihu article preparation through a local browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thneoly](https://clawhub.ai/user/thneoly)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical content creators use this skill to prepare and publish Markdown articles to Juejin, validate required article metadata, generate covers, attach columns, and check publication review status. It also helps prefill Zhihu articles for manual final publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses unofficial Juejin and Zhihu automation with logged-in accounts.

Mitigation: Use it only with accounts you control, keep publishing frequency conservative, and confirm that the workflow fits the relevant platform terms and account-risk tolerance.

Risk: Account cookies are stored in a local environment file.

Mitigation: Keep `.juejin.env` out of git and cloud sync, restrict local file permissions, and rotate or revoke the session if the file is exposed.

Risk: A crafted article filename could run unintended PowerShell commands on Windows when using the Zhihu workflow.

Mitigation: Avoid untrusted Markdown filenames and paths for `zhihu`, rename suspicious files before use, and review the command path before running it.

Risk: Runtime dependencies and browser automation can change behavior over time.

Mitigation: Pin and review dependencies before use, run `preview` first, and revalidate the workflow after browser, platform, or dependency updates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thneoly/skills/juejin-publisher-pro)
- [Category IDs](references/category_ids.md)
- [Example Post](examples/example-post.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with command examples, frontmatter examples, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local session configuration, generated cover images, draft metadata, and platform publishing actions when the included script is executed.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
