## Description:

Publish a release-note entry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release coordinators use this skill to turn a supplied release change set into a concise release-note receipt for routine release handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated release-note markdown could be incorrect or misleading if the supplied change set is incomplete or inaccurate.

Mitigation: Review generated markdown before using it in official release communications.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wxt-ai/skills/repository-release-changes-workbench)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Structured object containing change_id, title, markdown, and file_count.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consumes a release_change_set object with change_id, files, components, additions, and deletions.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
