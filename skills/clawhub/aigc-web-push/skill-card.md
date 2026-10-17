## Description:

Generates AI-assisted articles and visual cards, then sends them to WeChat Official Accounts or connected sites through a cloud computer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and teams use this skill to draft formatted articles and visual cards and send them to authorized WeChat accounts or connected sites. It can also push supplied image links and public video URLs where supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated content and push authorization are sent to an external service.

Mitigation: Install only if you trust the publisher and pcloud service with the content and authorization.

Risk: Locally stored push credentials could be exposed.

Mitigation: Treat config.json and skillKey as credentials; do not share them in public repositories or chat logs.

Risk: A push may target the wrong account or publish unexpectedly; cleanupDrafts can remove remote drafts.

Mitigation: Confirm target accounts and draft or publish mode before each push, and explicitly review any draft-cleanup operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Account configuration wizard](https://design.pcloud.ac.cn/aigc-web-push.html)
- [Cloud computer and connected account management](https://design.pcloud.ac.cn/#/manage?tab=server)

## Skill Output:

**Output Type(s):** [HTML, Shell commands, Configuration guidance]

**Output Format:** [HTML content and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a matching HTML cover and send articles, images, or public video URLs as drafts or published posts.]

## Skill Version(s):

3.2.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
