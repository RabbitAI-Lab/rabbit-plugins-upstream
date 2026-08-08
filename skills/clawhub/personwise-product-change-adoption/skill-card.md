## Description:

Turn release notes and migration documentation into a grounded, askable digital-human adoption course for product changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, product managers, enablement leads, and customer-success teams use this skill to create an interactive course explaining a specific product update, feature adoption path, migration, or breaking change from supplied source materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-selected release notes, migration documents, or reference images to the PersonWise SaaS for course creation.

Mitigation: Use only materials the user named or explicitly selected, and keep sensitive documents out unless the user intends to upload them to PersonWise.

Risk: Creating a course may consume existing PersonWise course credits.

Mitigation: Create only the requested number of courses, check readiness before creation, and do not purchase credits automatically.

Risk: Changing access to link, publication, or Topics submission can broaden who can view the resulting course.

Mitigation: Default to private access unless the user requests broader access, then report the final access mode and URL exactly.

Risk: The workflow may install or update the local PersonWise CLI before running business commands.

Mitigation: Use the bundled approval-gated bootstrap or the exact service-provided update command, without sudo, PATH edits, alternate origins, or credential handling.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/personwiseai/skills/personwise-product-change-adoption)
- [PersonWise service](https://personwise.ai)
- [PersonWise CLI release origin](https://releases.personwise.ai/cli/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Configuration]

**Output Format:** [Markdown guidance with JSON inputs and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates a PersonWise digital-human course through the local CLI and may return run status, source status, course IDs, and the final private or share URL.]

## Skill Version(s):

2.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
