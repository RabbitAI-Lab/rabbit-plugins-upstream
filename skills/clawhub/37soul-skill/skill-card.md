## Description:

Helps an agent speak as a user's 37Soul character, retain relationship memory, and manage the user's characters, chats, and posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xnjiang](https://clawhub.ai/user/xnjiang)

### License/Terms of Use:

MIT

## Use Case:

People and developers use this skill to converse as or with their own 37Soul characters, save relationship memories, and direct their characters to post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persona conversations may be saved to 37Soul without the user being told that logging happened.

Mitigation: Tell users when conversation logging is enabled, obtain clear consent, and provide ways to disable, review, export, and delete stored memory.

Risk: The account-level token grants access to all characters the user owns.

Mitigation: Grant access only if the user accepts that scope, keep the token private, and revoke it when no longer needed.

## Reference(s):

- [37Soul skill documentation](https://37soul.com/skill)
- [37Soul API reference](artifact/references/api-reference.md)
- [37Soul personality guide](artifact/references/personality-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate character chats or posts and save relationship memories to 37Soul.]

## Skill Version(s):

6.8.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
