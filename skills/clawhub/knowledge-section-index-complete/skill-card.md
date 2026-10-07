## Description:

Segments knowledge notes into sections and backlinks for a local index, with optional configured delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-base maintainers use this skill to segment notes, update a section and backlink index, and optionally deliver the indexed result to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private note contents are written to a local SQLite index.

Mitigation: Review notes before use and restrict access to the output directory.

Risk: Configured delivery can send full indexed note contents and a local file path to an external destination.

Mitigation: Verify the destination before enabling delivery; clear delivery-related environment variables and omit delivery configuration for local-only use.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local index artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes section and backlink updates, a local artifact receipt, and a delivery status receipt.]

## Skill Version(s):

1.2.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
