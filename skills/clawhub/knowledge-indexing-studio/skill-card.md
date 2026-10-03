## Description:

Segments knowledge notes and updates a section and backlink index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge teams use this skill to segment supplied notes into referenced sections, then maintain a local searchable section and backlink index.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing sensitive notes persists their content in a local searchable index.

Mitigation: Use a dedicated output directory and provide sensitive notes only if local persistence is acceptable.

## Reference(s):

- [Knowledge Indexing Studio on ClawHub](https://clawhub.ai/wxt-ai/skills/knowledge-indexing-studio)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON results; local SQLite index for downstream runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream runs persist the index beneath a caller-supplied output directory.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
