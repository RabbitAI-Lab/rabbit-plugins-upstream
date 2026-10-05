## Description:

Assess a release branch against its catalog status and expected version line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release managers and developers use this skill to assess whether a release branch is registered, aligned with its expected version line, and eligible under the bundled policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can automatically send assessment data and local artifact paths to external services.

Mitigation: Review the skill before installation; use only trusted destinations and control delivery and credential settings. For local-only assessments, leave delivery settings unset.

## Reference(s):

- [Release Branch Policy Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/release-branch-policy-workbench)

## Skill Output:

**Output Type(s):** [JSON assessment, Local record]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes branch and version-line status, a local record receipt, and a delivery receipt when external delivery is configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
