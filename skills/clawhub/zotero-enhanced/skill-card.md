## Description:

Zotero library management with PDF metadata auto-fetch (Crossref/arXiv), item search, file read, and note management. Supports cloud and WebDAV storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT

## Use Case:

Researchers, students, and developers use this skill to manage Zotero libraries from an agent workflow, including searching items, reading stored PDFs, uploading papers with metadata, and creating, updating, or deleting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Zotero API key with access to the user's library.

Mitigation: Install only if that level of Zotero library access is acceptable, and scope or rotate the API key according to the user's Zotero security practices.

Risk: Upload, read, update, and delete actions can expose or change Zotero library data.

Mitigation: Use dry-run modes and confirmation prompts for sensitive actions, and avoid --no-confirm unless the exact note key and action have already been reviewed.

Risk: Library metadata or document contents may be sent to Zotero, Crossref, arXiv, WebDAV, or appear in agent logs during normal operation.

Mitigation: Review inputs before execution and avoid using the skill with documents or notes that should not be shared with those services or logged.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/zotero-enhanced)
- [Publisher profile](https://clawhub.ai/user/guoxh)
- [Zotero](https://www.zotero.org)
- [Zotero API](https://api.zotero.org/)
- [Crossref API](https://api.crossref.org/)
- [arXiv API](https://export.arxiv.org/api/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and plain text or JSON script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Zotero item metadata, note content, search results, dependency checks, and dry-run previews.]

## Skill Version(s):

1.3.10 (source: server release evidence and SKILL.md changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
