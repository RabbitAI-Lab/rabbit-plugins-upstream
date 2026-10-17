## Description:

Connects an agent to a user's GetNote (Dedao Brain) account to save, find, read, and organize notes through the official CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT-0

## Use Case:

GetNote users use this skill to authorize access, search and read their notes, save links and files, and organize knowledge bases and tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser authorization stores account credentials locally.

Mitigation: Authorize only the intended account and never share or display full credentials in chat.

Risk: Saving, sharing, replacing tags, or deleting notes can change remote account data.

Mitigation: Confirm deletion, public sharing, broad tag replacement, and bulk removal before acting; check the final state after changes.

Risk: Reading notes in a shared conversation can disclose private content.

Mitigation: Show only necessary titles and summaries until the requester and display scope are confirmed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iswalle/skills/getnote)
- [Authentication and connection](references/auth.md)
- [Knowledge bases and file uploads](references/kb.md)
- [Notes](references/note.md)
- [Search](references/search.md)
- [Tags](references/tag.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with note links and inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on account permissions, CLI availability, and the completion of remote operations.]

## Skill Version(s):

2.2.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
