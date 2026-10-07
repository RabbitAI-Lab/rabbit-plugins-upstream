## Description:

Compares current and approved workspace access lists, creates a local access review checklist, and optionally delivers the result to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and access reviewers use this skill to compare membership lists and prepare a checklist of access changes for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured HTTP endpoint can receive sensitive workspace membership differences without an in-run confirmation or destination restriction.

Mitigation: Review delivery settings before use and enable delivery only to a trusted endpoint you control; otherwise leave delivery configuration unset to keep processing local.

Risk: Local checklists contain potentially sensitive workspace membership and access changes.

Mitigation: Store local checklist files in an access-controlled workspace and limit who can view or share them.

## Reference(s):

- [Workspace Access Comparator on ClawHub](https://clawhub.ai/wxt-ai/skills/workspace-access-checklist-complete)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON access differences and delivery receipt; local YAML access review checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Delivery is optional; without delivery configuration, the checklist stays local.]

## Skill Version(s):

1.2.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
