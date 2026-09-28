## Description:

Analyzes face photos or videos to suggest nine traditional Chinese medicine constitution types and personalized wellness guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking traditional Chinese medicine wellness guidance can submit face photos or videos for constitution assessments and personalized lifestyle suggestions. They can also request past assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face photos or videos and health-adjacent reports are sent to configured cloud services.

Mitigation: Obtain consent before upload, treat reports as sensitive, and confirm acceptable data retention and account controls before use.

Risk: Broad history requests can retrieve prior reports associated with the account.

Mitigation: Request history only when intended and review the scope before sharing retrieved reports.

Risk: Constitution assessments could be mistaken for medical diagnoses.

Mitigation: Use results for wellness reference only; seek professional care for symptoms or medical decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [Constitution analysis API documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured assessment text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes constitution tendencies, scores, and wellness suggestions; reports may be saved to a file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled skill frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
