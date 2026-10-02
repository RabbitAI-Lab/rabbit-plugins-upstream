## Description:

Compares workspace access lists and creates an access review checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Collaboration operations teams compare current and approved workspace members, then prepare a local checklist for reviewing access differences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace membership details may be sensitive.

Mitigation: Use only membership data appropriate for local processing.

Risk: The checklist operation writes a local YAML file that may contain access details.

Mitigation: Select a dedicated output directory and review the generated checklist before sharing it.

## Reference(s):

- [Workspace Access Review Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-access-review-desk)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON access delta and checklist response; local YAML checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checklist operation writes to a caller-selected local directory; it does not change workspace access.]

## Skill Version(s):

3.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
