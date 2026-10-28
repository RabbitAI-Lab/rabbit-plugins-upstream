## Description:

Finds and browses Huawei Cloud agent skills by keyword or category and provides details and installation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Huawei Cloud users can search for relevant cloud-service skills, review their descriptions, and obtain installation instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation reports an install count to an external service.

Mitigation: Ask for explicit consent before sending install telemetry.

Risk: Installation uses package-manager commands against unpinned remote sources.

Mitigation: Confirm the requested installation, validate the skill identifier, and review the source before running an installer; never paste raw search results into a shell command.

Risk: Broad activation and unrelated creator or cloud-testing references can pull the agent beyond skill discovery.

Mitigation: Limit use to the requested search or installation and disregard unrelated cloud-resource guidance unless separately requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-find-skills)
- [Skill instructions](artifact/SKILL.md)
- [Skill search utility](artifact/scripts/search-skills.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with skill search results, descriptions, and installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches a remote index; installation is optional and requires network access.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
