## Description:

Helps agents upload, draft, schedule or publish videos to Weixin Channels and check originality declarations through a logged-in Chrome session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and publishing teams use this skill to prepare and publish videos on Weixin Channels, schedule posts, and review originality declaration status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A logged-in Chrome debugging session can publish from the account without a mandatory final confirmation gate.

Mitigation: Use a separate automation browser profile, try --dry-run first, require human confirmation before running without --dry-run, and close the debugging browser afterward.

Risk: Scheduling, originality confirmation and final publishing steps are not fully verified in the artifact.

Mitigation: Review the draft before publishing and manually verify the publish record, scheduled time and originality declaration afterward.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jiaxinmmhh/skills/channels-video-publish)
- [Troubleshooting and known limitations](references/troubleshooting.md)
- [Weixin Channels publishing interface](https://channels.weixin.qq.com/platform/post/create)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save drafts or publish from a logged-in account and report originality declaration status.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
