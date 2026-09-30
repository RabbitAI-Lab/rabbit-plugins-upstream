## Description:

Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit patient home-monitoring images, videos, or media URLs to a remote analysis service for tremor, convulsion, stiffness, and gait-abnormality recognition. The skill can also retrieve prior cloud reports and return structured monitoring results, recommendations, and report links for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patient or home-monitoring media, media URLs, and report history are processed by lifeemergence.com cloud services.

Mitigation: Use the skill only when that remote processing matches privacy, consent, and compliance requirements for the monitored media.

Risk: The skill silently creates or reuses an internal identity and may store service tokens in a workspace SQLite database.

Mitigation: Review local workspace data handling before installation, restrict workspace access, and clear stored identities or tokens when they are no longer needed.

Risk: The output is health-related monitoring guidance and is not a medical diagnosis.

Mitigation: Treat results as assistive monitoring information and route frequent or concerning events to qualified medical professionals.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Smyx Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill accepts local media paths or media URLs, supports report-list retrieval, and documents a 10 MB media size limit for supported video/image formats.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
