## Description:

Selects a release branch, assesses its policy status, records the assessment locally, and optionally delivers it to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release engineers and developers use this skill to identify a release branch, assess its eligibility against the bundled branch policy, and record the result. They can optionally submit the assessment to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send release assessment data and a local file path to an external destination.

Mitigation: Review the delivery destination and clear unintended delivery, SMTP, and mail environment variables before use; treat configured delivery as a real external action.

Risk: Running the skill writes a local release-policy record.

Mitigation: Use a dedicated output directory and review the assessment before relying on or sharing it.

## Reference(s):

- [Release Branch Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/release-branch-policy-complete)

## Skill Output:

**Output Type(s):** [Analysis, Files]

**Output Format:** [JSON assessment and delivery receipt; local business record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The delivery receipt indicates whether external delivery was configured and its outcome.]

## Skill Version(s):

1.2.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
