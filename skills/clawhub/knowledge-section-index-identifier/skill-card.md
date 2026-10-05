## Description:

Segment a knowledge note for indexing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Knowledge managers and agents use this skill to split supplied knowledge notes into indexed sections with a reference, heading, tags, links, and content digests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied notes may contain information that should not be processed without permission.

Mitigation: Only run the local parser on notes you are authorized to provide.

Risk: Automatically extracted sections and links may not match the intended indexing structure.

Mitigation: Review the segmented note before adding it to an index.

## Reference(s):

- [Knowledge Note Segmenter on ClawHub](https://clawhub.ai/wxt-ai/skills/knowledge-section-index-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A segmented_note object with reference, heading, tags, links, content_digest, and sections; no external communication or persistent output.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
