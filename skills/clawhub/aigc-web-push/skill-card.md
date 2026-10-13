## Description:

Creates AI-assisted articles and image cards, then sends them to a WeChat Official Account or websites connected through a cloud computer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and account managers use this skill to draft articles or image cards and publish or save them as drafts through authorized WeChat and cloud-connected accounts. It can also send user-provided image or video links where supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing may send content to the wrong account or destination.

Mitigation: Check the selected account and apiBase, then require manual confirmation before sending content.

Risk: The account configuration contains sensitive access details.

Mitigation: Keep config.json private and do not commit it to a repository.

Risk: Clearing drafts changes remote account state, and a timeout does not confirm success.

Mitigation: Require explicit confirmation before cleanupDrafts and check the account draft list after any timeout before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Account configuration wizard](https://app.pcloud.ac.cn/design/aigc-web-push.html)
- [Cloud computer management](https://app.pcloud.ac.cn/design/#/manage?tab=server)

## Skill Output:

**Output Type(s):** [HTML, Markdown, Shell commands, Guidance]

**Output Format:** [HTML content and text instructions for publishing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports articles and image cards; sends content to configured accounts when authorized.]

## Skill Version(s):

3.2.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
