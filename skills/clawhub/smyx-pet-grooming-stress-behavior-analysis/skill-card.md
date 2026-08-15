## Description:

Analyzes pet grooming video files or URLs through cloud APIs to identify stress behaviors such as struggling, panting, and tail tucking, then returns a structured stress-level report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet grooming businesses, veterinary clinics, and pet care service teams use this skill to analyze grooming-session videos for observable pet stress signals and stress-level grading. Agents can also retrieve cloud history reports associated with the internally resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Grooming videos or video URLs are sent to lifeemergence.com cloud services for analysis.

Mitigation: Use only footage with appropriate authorization and consent, and review service retention and data-processing expectations before using customer, clinic, or business video.

Risk: The skill silently creates and reuses identity sessions and stores account/session tokens locally.

Mitigation: Run it in a workspace with appropriate access controls, review local token/session storage before installation, and clear local session records when they are no longer needed.

Risk: Cloud history report queries are associated with an internally resolved identity.

Mitigation: Confirm user/account boundaries before retrieving history reports and avoid exposing report links or history results to unauthorized users.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Grooming Stress Behavior Analysis API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown text with structured JSON report content and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes stress behavior observations, stress-level grading, history-report listings, and report export links when returned by the cloud service.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
