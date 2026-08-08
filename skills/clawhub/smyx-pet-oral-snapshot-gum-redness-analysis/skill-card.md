## Description:

Analyzes pet oral snapshot images or videos through provider cloud APIs to report visible gum color, redness level, tartar coverage, and oral-health observations without providing diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and pet health product teams use this skill to submit pet mouth images, videos, or URLs for structured oral-health observations in pet cameras, smart pet products, and pet health management platforms. The skill supports current analysis and cloud history lookup, but its observations are not medical diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet mouth images, videos, or provided URLs are sent to the provider's cloud service for analysis.

Mitigation: Use only media that is appropriate to share with the provider, avoid private or signed URLs unless permitted, and review the provider's retention and deletion terms before use.

Risk: Reports are tied to an automatically managed identity and history can be queried from the cloud service.

Mitigation: Treat report history as account-linked data and use history lookup only when the user expects cloud-stored reports to be retrieved.

Risk: Authentication tokens and identity data may be stored locally for reuse.

Mitigation: Restrict workspace access, review local data storage before deployment, and remove stored credentials or identity files when the skill is no longer needed.

## Reference(s):

- [Pet Oral Snapshot API Documentation](references/api_doc.md)
- [Common Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the returned report content to a file when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
