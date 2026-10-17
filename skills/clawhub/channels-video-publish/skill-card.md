## Description:

Automates publishing finished videos to Weixin Channels, including metadata, originality declarations, scheduling, and post-publication checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and publishing teams use this skill to upload finished videos and prepared copy to Weixin Channels, schedule series, check publication status, and reschedule pending posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a logged-in browser profile can publish or enumerate account content.

Mitigation: Use a separate Chrome profile, try a dry-run first, and manually verify each publish or reschedule result in Weixin Channels.

Risk: The browser debugging port and sandbox-bypass guidance expose sensitive session control if used carelessly.

Mitigation: Keep the debugging port bound to localhost and review the need for any sandbox bypass before running commands.

Risk: Account-content exports use a fixed local Downloads path.

Mitigation: Review and protect exported files in Downloads.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jiaxinmmhh/skills/channels-video-publish)
- [Troubleshooting guide](references/troubleshooting.md)
- [Weixin Channels publishing interface](https://channels.weixin.qq.com/platform/post/create)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single-video publishing, batch scheduling, listing, and rescheduling; dry-run saves a draft without publishing.]

## Skill Version(s):

1.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
