## Description:

Analyzes pet camera or feeder monitoring videos with computer vision to report feeding, drinking, excretion, mental state, vomiting, limping, and other health indicators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit pet monitoring videos or URLs for cloud-based health behavior analysis, receive structured health monitoring reports, and query prior reports. Results are for pet health reference and do not replace professional veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet monitoring videos or URLs are sent to the Life Emergence cloud service for analysis.

Mitigation: Install and use only when cloud processing and retention of the submitted footage is acceptable.

Risk: The skill may create or reuse an account identity and store identity tokens in a local workspace database.

Mitigation: Run in a workspace where local identity-token storage is acceptable, and avoid private household footage when that identity model is not appropriate.

Risk: Health monitoring reports may be mistaken for professional diagnosis.

Mitigation: Treat results as reference information and consult a veterinarian when abnormalities are detected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)
- [Pet health analysis API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or plain text reports with optional JSON detail and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save report output to a user-specified file path]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
