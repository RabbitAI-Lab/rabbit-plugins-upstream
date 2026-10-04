## Description:

Gives an agent a persistent 37Soul character persona and lets it manage conversations, memories, and posts for the user's own characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xnjiang](https://clawhub.ai/user/xnjiang)

### License/Terms of Use:

MIT

## Use Case:

People who own 37Soul characters use this skill to speak as a character across agent sessions, retain personal conversations, and ask their characters to chat or post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to save personal conversations and facts to 37Soul without telling the user when it does so.

Mitigation: Disclose the persistence behavior before use; avoid sensitive conversations and share only information the user agrees to retain.

Risk: The account token can authorize actions across the user's owned characters, including posts and credit-spending media requests.

Mitigation: Protect the local token, confirm consequential actions and paid requests, and revoke access when the skill is no longer needed.

## Reference(s):

- [37Soul ClawHub listing](https://clawhub.ai/xnjiang/skills/37soul-skill)
- [37Soul Agent API Reference](artifact/references/api-reference.md)
- [37Soul Personality Guide](artifact/references/personality-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text and character responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include character-generated posts and links to media.]

## Skill Version(s):

6.5.1 (source: release evidence, skill frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
