## Description:

Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers use this skill to analyze home monitoring video or image inputs for tremors, convulsions, stiffness, gait abnormalities, and related historical reports. The output is intended for auxiliary monitoring and does not replace professional medical diagnosis or clinical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload sensitive medical or household video to a remote service.

Mitigation: Use only with informed consent and documented service endpoints, retention policy, deletion process, and handling rules for sensitive health or household data.

Risk: The skill may silently create or bind an account-like identity, persist tokens, and query cloud report history.

Mitigation: Review identity creation, token storage, and report-history access before installation; avoid shared workspaces unless account and data boundaries are documented.

Risk: The package includes development or private HTTP configuration behavior.

Mitigation: Require documented production configuration and remove or disable private, development, and non-HTTPS endpoints before deployment.

Risk: Behavior recognition results may be mistaken for medical diagnosis.

Mitigation: Present outputs as auxiliary monitoring only and direct users to professional medical evaluation for health decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON responses, report links, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file when --output is supplied; list mode returns cloud report history as structured text.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
