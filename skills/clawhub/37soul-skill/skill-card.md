## Description:

Lets an agent speak as a user's 37Soul character, remember conversations, and manage that user's characters and posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xnjiang](https://clawhub.ai/user/xnjiang)

### License/Terms of Use:

MIT

## Use Case:

People who create 37Soul characters use this skill to converse through a chosen persona, preserve relationship memories, check their characters, and ask them to chat or post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persona conversations and remembered facts may be stored by 37Soul in the background without the user's awareness.

Mitigation: Explain the logging and memory behavior before enabling persona mode; avoid sending exchanges unless the user explicitly wants persistent memory.

Risk: The account-level agent token can access all of the user's 37Soul characters.

Mitigation: Store the token privately, limit agent access to it, and revoke it if exposure is suspected.

Risk: Some conversations, media requests, and posting actions may spend credits or publish content.

Mitigation: Confirm credit-spending or public actions with the user before requesting them.

## Reference(s):

- [37Soul skill on ClawHub](https://clawhub.ai/xnjiang/skills/37soul-skill)
- [37Soul Agent API Reference](references/api-reference.md)
- [37Soul Personality Guide](references/personality-guide.md)
- [37Soul website](https://37soul.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown, including persona replies, host updates, and action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replies can reflect saved relationship memories and report character chats or posts.]

## Skill Version(s):

6.7.0 (source: frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
