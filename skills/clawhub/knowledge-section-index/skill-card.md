## Description:

Combines segment a knowledge note for indexing with update a section and backlink index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge workers, developers, and agents use this skill to segment structured knowledge notes and maintain a local section and backlink index for retrieval or curation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The index update operation can change a local knowledge index.

Mitigation: Run the update operation only when an index change is intended; use the segmenting operation alone for read-only preparation.

Risk: Incorrect note sections or backlink relationships could reduce index quality.

Mitigation: Review segmented notes and proposed index updates before relying on them in a shared knowledge index.

## Reference(s):

- [Skill source documentation](artifact/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/knowledge-section-index)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured text fields for segmented notes or index updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operation-specific output is either a segmented_note for note segmentation or an index_update for index curation.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
