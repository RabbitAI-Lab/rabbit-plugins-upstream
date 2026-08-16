## Description:

Generates standards-compliant article and image-card HTML, humanizes text, and prepares content for publishing to WeChat Official Accounts or configured cloud publishing targets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, operators, and agent builders use this skill to draft formatted web articles or image-card posts, refine AI-generated prose, and prepare shell commands and configuration for publishing through the selected WeChat or cloud channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing commands can send unpublished content and account identifiers to the configured remote API.

Mitigation: Keep config.json out of version control, verify apiBase and the selected account or cloud instance before pushing, and review all generated content before publication.

Risk: Draft cleanup behavior can remove drafts when the cleanupDrafts action is used.

Mitigation: Use cleanupDrafts only when the user explicitly intends to clear drafts, and confirm the target account first.

Risk: The humanizer file workflow can rewrite prose files in place.

Mitigation: Review target file paths before applying file-mode edits and preserve a backup or version-control checkpoint for important drafts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Configuration wizard](https://app.pcloud.ac.cn/design/aigc-web-push.html)
- [Cloud computer management](https://app.pcloud.ac.cn/design/#/manage?tab=server)
- [Default publishing API endpoint](https://api.pcloud.ac.cn/openAccessService)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML/code snippets, JSON configuration examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce publish-ready HTML and commands that call a configured remote API when executed.]

## Skill Version(s):

3.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
