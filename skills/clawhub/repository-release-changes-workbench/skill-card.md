## Description:

Publish a release-note entry from a structured change set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release coordinators and developers use this skill to turn a structured repository change set into a release-note entry and receipt. It writes a local journal entry and can deliver the record to a configured service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can automatically receive the generated release-note data and local artifact path.

Mitigation: Leave delivery endpoint, SMTP, and related credential variables unset unless sending to a trusted service is intentional; review the skill before automated or shared use.

Risk: The skill writes release-note artifacts to a local output directory.

Mitigation: Use a dedicated, writable output directory and review its contents before sharing.

## Reference(s):

- [Release Notes Journal on ClawHub](https://clawhub.ai/wxt-ai/skills/repository-release-changes-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files]

**Output Format:** [JSON receipt containing a Markdown release note; local Markdown journal entry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes change identifier, title, and file count; may include a delivery receipt when a target is configured.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
