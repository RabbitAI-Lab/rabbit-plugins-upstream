## Description:

Create a profile-setting review item.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Workspace administrators and developers use this skill to create a local governance review item for an approved profile setting key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill creates or updates a review JSON file in the chosen output directory.

Mitigation: Use a dedicated, writable output folder and review the resulting file before relying on it.

## Reference(s):

- [Profile Governance Register on ClawHub](https://clawhub.ai/wxt-ai/skills/profile-setting-key-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON review item and local JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the review item ID, setting key, value type, review queue, and a local file receipt.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
