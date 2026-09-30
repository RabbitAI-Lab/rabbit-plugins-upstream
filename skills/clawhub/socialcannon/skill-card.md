## Description:

Helps agents publish, schedule, and manage social media posts across connected accounts using SocialCannon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miprinia](https://clawhub.ai/user/miprinia)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers, creators, and developers use this skill to help agents draft, schedule, publish, and review posts and engagement across connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, replying, retrying, deleting, disconnecting, or repurposing in post mode can affect live accounts and may be irreversible.

Mitigation: Get explicit human approval before these actions; prefer drafts, scheduled posts, and previews where possible.

Risk: Exposing the client secret or giving an optional MCP process account credentials can compromise connected accounts.

Mitigation: Keep secrets in environment variables or a keychain, not chat or configuration files; enable MCP only when its credential access is intended.

## Reference(s):

- [SocialCannon ClawHub release](https://clawhub.ai/miprinia/skills/socialcannon)
- [SocialCannon homepage](https://socialcannon.app)
- [Optional SocialCannon MCP package](https://www.npmjs.com/package/@socialcannon/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for drafts, schedules, publishing, analytics, and engagement through connected accounts.]

## Skill Version(s):

1.12.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
