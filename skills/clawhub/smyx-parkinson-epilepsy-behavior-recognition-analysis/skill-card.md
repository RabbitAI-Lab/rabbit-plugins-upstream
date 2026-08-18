## Description:

Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze patient monitoring videos or media URLs for Parkinson's- and epilepsy-related abnormal behaviors, then receive structured monitoring results, recommendations, report links, or a history of prior cloud reports. The output is for assistive monitoring and does not replace professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health-related videos, media URLs, identifiers, and report queries may be sent to external lifeemergence services.

Mitigation: Use only in environments approved for patient media and identity-linked data, and review data handling expectations before installation.

Risk: The skill silently manages identities and stores service tokens locally.

Mitigation: Run it in an isolated workspace when possible, limit access to local state, and remove local database or token files when they are no longer needed.

Risk: The analysis may be mistaken for medical diagnosis.

Mitigation: Present results as assistive monitoring only and require professional medical review for clinical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis)
- [API Interface Document](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files]

**Output Format:** [Structured text or JSON reports with optional Markdown tables and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a user-specified file and may query cloud-hosted history reports.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
