## Description:

Select a document release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Document release coordinators and developers use this skill to select an eligible version from supplied guidance and record the selection locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can automatically receive selection results and local artifact path metadata.

Mitigation: Review the skill before installation and configure delivery endpoints and credentials only in environments where outbound delivery is intended.

## Reference(s):

- [Document Release Selector on ClawHub](https://clawhub.ai/wxt-ai/skills/draft-precedence-guidance-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON selection result with a local artifact and delivery receipt when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes selected version, eligible versions, and selection reason.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
