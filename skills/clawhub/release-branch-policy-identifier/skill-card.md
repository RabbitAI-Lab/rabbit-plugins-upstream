## Description:

Selects a release source branch from a supplied quarter and release name.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release managers and developers use the skill to choose a consistent source branch name for a planned release from its quarter and release name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect quarter or release name can yield the wrong branch identifier.

Mitigation: Supply the intended release details in an explicit request JSON file and review the returned branch before using it.

## Reference(s):

- [Release Branch Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/release-branch-policy-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with a source_branch string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a release/qN-name branch identifier without creating a business artifact.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
