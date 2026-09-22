## Description:

Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unclear acceptance criteria, or architecture-heavy requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to structure medium-to-large or unclear software changes into requirements, design, task planning, and confirmed execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can slow larger coding tasks by routing them through requirements, design, and task-confirmation phases.

Mitigation: Use it for medium-to-large or unclear work, and skip the full workflow when the scope and acceptance criteria are already clear.

Risk: The skill can create local spec Markdown files containing project requirements, design notes, and task plans.

Mitigation: Review generated spec files before implementation and avoid including secrets or sensitive business data unless the workspace is authorized for them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown planning documents and concise procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create requirements.md, design.md, and tasks.md under specs/<spec_name>/ when the workflow is used.]

## Skill Version(s):

1.18.51 (source: server release metadata; artifact frontmatter reports 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
