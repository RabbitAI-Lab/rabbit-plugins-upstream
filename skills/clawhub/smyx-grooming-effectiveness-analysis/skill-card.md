## Description:

Analyzes pet grooming photos or videos to estimate matting, shed hair, grooming effectiveness, and hairball risk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming service providers can review grooming images or videos to estimate coat matting and shed hair and receive a hairball risk summary. Results are for care reference and are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags privacy and credential concerns, and submitted media may be sent for server-side analysis.

Mitigation: Clarify how media and credentials are handled before use, and avoid submitting sensitive material unless the service is trusted for it.

Risk: The security assessment notes account and report-history capabilities that may involve additional user data.

Mitigation: Use those capabilities only when needed and review the associated data handling.

Risk: The assessment says export-only behavior may still trigger analysis, and its scan was partial because a referenced path was missing.

Mitigation: Confirm export-only behavior and complete the security review before relying on that mode.

## Reference(s):

- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured grooming analysis report with observations, estimated risk level, care suggestions, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual estimates for care reference; not a medical diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
