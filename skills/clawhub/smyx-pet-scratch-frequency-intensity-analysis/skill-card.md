## Description:

Analyzes cat scratch-post video files or URLs to summarize scratching frequency, duration, and estimated intensity, with observations about stress and claw health rather than diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to review cat scratch-post footage, quantify scratching behavior, and inspect past analysis reports. Its observations are not veterinary diagnoses or behavior-correction advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household pet footage or video URLs are sent to a cloud service for analysis.

Mitigation: Obtain consent before submitting footage and check the service's privacy and retention terms before using private household videos.

Risk: The skill silently creates or reuses an internal identity and stores service tokens locally.

Mitigation: Review the account linkage before installation and protect local credentials on shared devices.

Risk: History requests can retrieve cloud reports linked to the internal identity without an explicit confirmation step.

Mitigation: Confirm the user's intent before retrieving history and limit access to trusted users.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON, with a Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links; results can be saved to a file.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
