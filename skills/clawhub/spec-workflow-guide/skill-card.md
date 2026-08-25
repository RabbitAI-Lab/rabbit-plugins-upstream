## Description:

Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unclear acceptance criteria, or architecture-heavy requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to decide when a coding request needs structured planning and to produce requirements, design, and task documents before implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can add planning overhead by asking the agent to write requirements, design, and task files before implementation.

Mitigation: Use it for medium-to-large or unclear changes, and skip the full workflow for small, low-risk tasks with clear acceptance criteria.

Risk: Specification documents may contain incorrect assumptions if the original request is underspecified.

Mitigation: Review and confirm each planning phase before using the task plan for implementation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown planning documents and concise agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces requirements.md, design.md, and tasks.md under a specs/<spec_name>/ workflow when the full process is used.]

## Skill Version(s):

1.18.37 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
