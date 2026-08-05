## Description:

Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unclear acceptance criteria, or architecture-heavy requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to decide when a larger change needs explicit requirements, design, and task planning before implementation. It guides the agent through concise, reviewable Markdown planning artifacts with user confirmation between phases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can slow larger coding work by asking the agent to produce requirements, design, and task documents before implementation.

Mitigation: Use it for medium-to-large or unclear changes, and skip the full workflow for small, low-risk tasks with clear acceptance criteria.

Risk: Planning artifacts may encode incorrect assumptions if the original request is underspecified.

Mitigation: Require user confirmation before moving from requirements to design, from design to tasks, and from tasks to implementation.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown planning documents and concise agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces requirements.md, design.md, and tasks.md under specs/<spec_name>/ when the full workflow is appropriate.]

## Skill Version(s):

1.18.26 (source: server release metadata; artifact frontmatter reports 2.25.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
