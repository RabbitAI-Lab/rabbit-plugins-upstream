## Description:

Helps agents research TikTok posts and creators through search, post details, comments, replies, profiles, and creator post lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this read-only skill to investigate TikTok posts, audience comments, and creator activity with a SocialDataX API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned package may execute changed code with access to the user's SocialDataX API key.

Mitigation: Pin socialdatax-skills to a reviewed version or use a preinstalled, controlled binary.

Risk: Interrupted pagination may leave TikTok search or comment results incomplete.

Mitigation: Retain returned items, disclose incomplete results, and resume with the supplied next-page token when available.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-tiktok)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown guidance with shell commands and retrieved TikTok data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data access; search and list results may be partial if pagination fails.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
