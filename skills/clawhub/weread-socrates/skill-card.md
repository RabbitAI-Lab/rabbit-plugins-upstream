## Description:

Provides a fully offline, single-file Socratic reading companion for manually pasted WeChat Reading excerpts, with Reader Memory v2 and user-confirmed cross-book relationships.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External readers and learners use this skill to open an offline browser companion, paste excerpts they are allowed to use, generate Socratic questions, save local reading-memory entries, and confirm relationships across books.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted passages, notes, and confirmed relationships can remain in browser localStorage until the user clears the page data or Memory.

Mitigation: Use the clear-Memory flow or browser site-data controls to remove local reading data, and avoid pasting sensitive material.

Risk: User-triggered Markdown and PNG exports may contain pasted book text.

Mitigation: Only paste, export, and share material the user has rights to use, and keep exported study materials private unless redistribution is permitted.

## Reference(s):

- [weread-socrates ClawHub page](https://clawhub.ai/bonniegeng-max/skills/weread-socrates)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Offline reading companion HTML](assets/ai-reading-companion.html)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Files]

**Output Format:** [Browser-rendered text with user-triggered Markdown and PNG downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline single-file runtime; saved notes and confirmed relations remain in browser localStorage until cleared.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter, _meta.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
