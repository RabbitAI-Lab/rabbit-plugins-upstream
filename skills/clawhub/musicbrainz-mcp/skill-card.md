## Description:

Searches and browses MusicBrainz metadata, fetches Cover Art Archive images, resolves MusicBrainz URLs, and, when OAuth is configured, submits user-approved tags, ratings, and collection edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer music metadata questions, inspect artist and release catalogs, retrieve cover art URLs, and manage the user's own MusicBrainz tags, ratings, or collections after OAuth setup and explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled write tools can change the user's own MusicBrainz tags, ratings, or collections.

Mitigation: Review the dry-run preview and only approve confirm:true write calls after the user explicitly confirms the intended change.

Risk: Read operations query external MusicBrainz and Cover Art Archive services.

Mitigation: Avoid sending sensitive queries and disclose external service use when the surrounding workflow requires it.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown guidance with MCP tool call examples and JSON-like response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports compact and full response views for selected read tools; OAuth-enabled write tools return a dry-run preview unless confirm:true is explicitly approved.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
