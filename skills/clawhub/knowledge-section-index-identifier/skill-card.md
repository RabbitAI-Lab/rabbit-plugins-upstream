## Description:

Segment a knowledge note for indexing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge operations users use this skill to segment a supplied knowledge note into indexing-friendly fields such as reference, heading, tags, links, digest, and sections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user may include knowledge-note content they did not intend to process.

Mitigation: Provide only the knowledge-note content intended for segmentation.

Risk: Incorrect segmentation could affect downstream indexing quality.

Mitigation: Review the segmented_note output before adding it to an index or knowledge base.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/knowledge-section-index-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Structured object with reference, heading, tags, links, content_digest, and sections fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes only the knowledge note supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
