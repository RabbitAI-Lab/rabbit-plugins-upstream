## Description:

iHatePosting is a tool to schedule social media and chat posts to 15 channels X, LinkedIn, Instagram, Facebook Page, Threads, YouTube, Google Business, TikTok, Pinterest, Discord, Slack, Mastodon, Bluesky, Telegram, Tumblr. Use this skill to find a workspace's channels, read each channel's rules, upload media, create posts, change a post's status or settings and read analytics from the command line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mayankkasavala](https://clawhub.ai/user/mayankkasavala)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers and developers can use this skill to discover connected channels, follow channel-specific rules, prepare and schedule posts, manage post status and settings, and review analytics across the supported services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags post deletion as a capability that is not disclosed in the skill description.

Mitigation: Confirm deletion is intended and check the target post before running a deletion command.

Risk: The skill uses API credentials, and the security guidance notes that credentials may be stored locally.

Mitigation: Use the skill only where local credential storage is acceptable and protect access to the credentials.

Risk: The scan was partial and did not fully cover some referenced paths.

Mitigation: Review unresolved referenced material before relying on the skill in a deployment.

## Reference(s):

- [iHatePosting agent documentation](https://ihateposting.com/ai-agents)
- [iHatePosting CLI package](https://www.npmjs.com/package/ihateposting)
- [Command line guide](https://github.com/iHatePostingOrg/iHatePosting-Agent/blob/main/examples/COMMAND_LINE_GUIDE.md)
- [Provider settings guide](https://github.com/iHatePostingOrg/iHatePosting-Agent/blob/main/PROVIDER_SETTINGS.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on the connected channels, their rules, and the requested post or analytics task.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
