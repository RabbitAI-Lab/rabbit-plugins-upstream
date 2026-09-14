## Description:

Supports AI-assisted generation of articles and image-text cards, then pushes them to WeChat Official Accounts or to sites reached through a cloud desktop; it can also work with articles, images, and videos produced by other skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, operators, and developers use this skill to generate styled HTML content, optionally humanize article text, prepare cover pages, and publish drafts or media through WeChat Official Account or cloud-desktop channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing scripts can transmit sensitive configuration and local content with broader control than users may expect.

Mitigation: Install only if the publisher and pcloud service are trusted, keep config.json private, and review generated content before publishing.

Risk: A prompt could steer the agent toward an unexpected API endpoint, local file path, or cleanupDrafts action.

Mitigation: Verify apiBase is the expected HTTPS endpoint and require explicit user approval before using arbitrary local file paths or cleanupDrafts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Configuration Wizard](https://app.pcloud.ac.cn/design/aigc-web-push.html)
- [Cloud Desktop Management](https://app.pcloud.ac.cn/design/#/manage?tab=server)
- [Xiaping Skill Page](https://xiaping.coze.com/skill/015db5c8-8dc6-4c44-b16c-b865ea3c06f0)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, JSON configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local HTML content and command invocations that may send configured content to external publishing services.]

## Skill Version(s):

3.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
