## Description:

Identifies familiar people in images and videos by comparing faces against an enrolled face database, and returns recognition results and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compare people in images or videos with an enrolled face database and retrieve analysis reports. Recognition results are for reference only and must not be used for legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private face images and videos may be processed by a remote service, and its retention and deletion behavior has not been confirmed.

Mitigation: Confirm the provider's retention and deletion practices before submitting private footage.

Risk: The security review says credentials can be reused as account details and video processing may occur despite the skip-analysis option.

Mitigation: Do not use an API secret as account identity; rotate any secret already submitted, and confirm processing controls before use.

Risk: The export-env-only and API URL options may not prevent uploads or redirect requests as expected.

Mitigation: Do not rely on these options as privacy or network controls, and protect the shared credential database.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured recognition reports and Markdown history tables, with optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include identities, locations, monitoring results, suggestions, and report links; results are for reference only, not legal identity verification.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
