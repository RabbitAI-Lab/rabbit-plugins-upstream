## Description:

AutoThread lets an agent turn `/topic` messages in supported group chats into Telegram or Nicegram topics, Discord threads, or Signal digest posts with generated titles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abyssbugg](https://clawhub.ai/user/abyssbugg)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and team chat operators use AutoThread to let an agent create discussion threads or topic-like posts from `/topic` messages while preserving the original message context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production adapter scripts can be redirected to arbitrary API servers, which could expose bot tokens and message content.

Mitigation: Run only in controlled environments with least-privileged Telegram, Discord, Nicegram, and Signal credentials, and prevent untrusted users or wrappers from setting AUTOTHREAD_API_BASE.

Risk: Reposted Discord content may trigger unwanted mention parsing.

Mitigation: Disable Discord mention parsing for reposted content or sanitize adapter messages before enabling the skill in shared Discord servers.

## Reference(s):

- [AutoThread ClawHub page](https://clawhub.ai/abyssbugg/skills/autothread)
- [AutoThread project homepage](https://github.com/abyssbugg/autothread)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON adapter outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapter scripts return JSON containing topic_id, title, and link fields.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
