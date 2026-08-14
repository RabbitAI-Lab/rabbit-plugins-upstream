## Description:

Connects GetNote to the current AI agent through the official CLI so the agent can save, query, search, and organize the user's real notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to connect an AI agent to their GetNote account, then save content, search notes, inspect note details, organize notes into knowledge bases or folders, subscribe to supported creators, and manage tags through the official CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and update flows can change the local machine by globally installing or updating the GetNote CLI.

Mitigation: Install only when the publisher and CLI are trusted, and treat setup or update prompts as software-update prompts.

Risk: The update flow can refresh local skill files from a remote release.

Mitigation: Review refreshed skill files and security scan results before relying on the updated skill in sensitive workflows.

Risk: The skill can surface private note content in the agent conversation.

Mitigation: Avoid shared sessions for private notes and confirm visibility scope before displaying full note content.

## Reference(s):

- [GetNote connection, diagnostics, and updates](artifact/references/auth.md)
- [GetNote notes](artifact/references/note.md)
- [GetNote search](artifact/references/search.md)
- [GetNote knowledge bases](artifact/references/kb.md)
- [GetNote tags](artifact/references/tag.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI command summaries, note metadata, links, IDs, and error details when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real note titles, note IDs, note URLs, request IDs, authentication or diagnostic status, and confirmation prompts for destructive or sharing actions.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
