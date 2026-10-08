## Description:

Helps agents view Buffer accounts and channels, manage content ideas, and draft or schedule social media posts through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Social media teams and developers use this skill to inspect Buffer accounts and channels, develop content ideas, and prepare or schedule posts across connected platforms. It also guides approved automations for recurring Buffer tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Buffer write can publish or schedule content publicly on the wrong channel.

Mitigation: Review the target channel, content, and timing with the user before each write; default to drafts unless publication is explicitly requested.

Risk: Hosted functions, triggers, and destinations can continue acting or forwarding data after setup.

Mitigation: Get explicit approval for each deployment or destination and review its scope and ongoing effects.

Risk: Account credentials or connection details could be exposed through unsafe handling.

Mitigation: Prefer OAuth login; never print, store in files, or forward credentials to third-party URLs.

## Reference(s):

- [Buffer API documentation](https://developers.buffer.com/reference.html)
- [Buffer API getting started](https://developers.buffer.com/guides/getting-started.html)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, GraphQL queries, Code]

**Output Format:** [Markdown with command, GraphQL, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing and persistent automations require user review and approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
