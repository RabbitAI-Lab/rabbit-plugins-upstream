## Description:

Create a profile-setting review item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to create a governance review item for an approved profile setting key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send the review item and local artifact path to an arbitrary endpoint through ambient settings.

Mitigation: Check delivery endpoint and SMTP settings before running; remove unapproved values or use a trusted destination.

Risk: Running the skill writes a review artifact to the selected local directory.

Mitigation: Choose an approved writable output directory and handle stored review records according to local retention rules.

## Reference(s):

- [Profile Governance Register on ClawHub](https://clawhub.ai/wxt-ai/skills/profile-setting-key-workbench)
- [Publisher profile: wxt-ai](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON review item with a local record and, when configured, a delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes review item ID, setting key, value type, and review queue.]

## Skill Version(s):

1.1.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
