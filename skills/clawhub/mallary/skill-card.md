## Description:

Guides agents using Mallary to inspect connected social accounts and, when explicitly requested, publish or manage social-media content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sammydigits](https://clawhub.ai/user/sammydigits)

### License/Terms of Use:

MIT-0

## Use Case:

Social-media operators and developers use this skill to inspect Mallary profiles, posts, analytics, and connected accounts, or carry out explicitly requested publishing and account-management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth setup grants access to read, publish, engage, and manage connected accounts.

Mitigation: Start authentication only at the user's request and explain the access before browser approval.

Risk: Publishing or account changes can affect public content or the wrong profile.

Mitigation: Resolve the exact profile, destination, content, media, and timing from the user's request; perform the requested action once and verify it read-only.

Risk: Credentials or transient CLI installs may expose connected accounts.

Mitigation: Keep tokens and API keys out of chat and logs, and use a reviewed or pinned CLI version rather than unpinned npx.

## Reference(s):

- [Mallary skill release on ClawHub](https://clawhub.ai/sammydigits/skills/mallary)
- [Mallary website](https://mallary.ai/)
- [Mallary CLI package](https://www.npmjs.com/package/@mallary/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only discovery by default; report the result of authorized actions without repeating them.]

## Skill Version(s):

1.1.5 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
