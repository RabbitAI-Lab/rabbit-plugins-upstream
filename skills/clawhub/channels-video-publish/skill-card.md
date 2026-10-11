## Description:

Helps agents upload, schedule or publish videos to WeChat Channels and review published posts through a logged-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and account managers use this skill to upload videos, schedule or immediately publish posts, change scheduled times, and check publication and originality status in WeChat Channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or rescheduling through a logged-in browser can change account content without sufficient confirmation.

Mitigation: Review commands and post details before publishing or rescheduling; check the saved draft or publication record afterward.

Risk: Browser automation has broad authority over the authenticated session.

Mitigation: Use an isolated Chrome profile and keep the remote debugging connection bound to localhost.

Risk: Exported post lists can expose private account metadata.

Mitigation: Treat ch-posts.json as private and limit access to the exported file.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jiaxinmmhh/skills/channels-video-publish)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON data]

**Output Format:** [Plain text and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can publish or reschedule account posts and export post metadata to ch-posts.json.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
