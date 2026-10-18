## Description:

Generates HTML articles and image cards, then sends them to WeChat Official Accounts or cloud-connected publishing sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and publishing teams use this skill to draft formatted articles or image cards and send them to configured WeChat accounts or cloud-connected sites; it can also forward supplied images and video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured WeChat or cloud credentials can authorize sending content through connected accounts.

Mitigation: Keep config.json and skillKey private, restrict account access, and review generated HTML before sending.

Risk: Publish mode or draft cleanup can release or remove content without sufficient review.

Mitigation: Require explicit user confirmation before publishing or cleaning up drafts.

Risk: A queued cloud submission may be mistaken for a completed publication or resent after a timeout.

Mitigation: Report queued delivery accurately and check the destination before attempting a retry.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Configuration wizard](https://design.pcloud.ac.cn/aigc-web-push.html)
- [Cloud computer management](https://design.pcloud.ac.cn/#/manage?tab=server)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions]

**Output Format:** [HTML files and command-line instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a companion cover HTML file; successful cloud submission means queued delivery, not confirmed publication.]

## Skill Version(s):

3.2.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
