## Description:

Update a section and backlink index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge operations users use this skill to turn a supplied segmented note into a concise section and backlink index update, including indexed sections, backlinks, deduplication status, and removed duplicates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes note-section content supplied in the current request, which may include information the user did not intend to index.

Mitigation: Provide only note content intended for indexing and review the resulting index_update before using it in a shared knowledge index.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/knowledge-section-index-workbench)

## Skill Output:

**Output Type(s):** [Text, Structured data, Guidance]

**Output Format:** [JSON object in the requested index_update field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses supplied segmented_note data and returns index_id, reference, heading, content_digest, indexed_sections, backlinks, dedup_status, and duplicates_removed.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
