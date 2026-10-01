## Description:

Analyzes child video and optional audio to identify apparent emotions and provide soothing suggestions and historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and educators use child video or audio to review apparent emotional states, receive soothing suggestions, and look up past reports. Results are not psychological diagnoses or clinical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child video, audio, and inferred emotions are sent to a vendor cloud and may be retained as historical reports.

Mitigation: Use only with explicit guardian or institutional authorization; confirm the vendor's data-handling and retention terms before uploading.

Risk: The skill silently creates or reuses an identity and stores tokens associated with sensitive child reports.

Mitigation: Review identity and token handling before use, restrict access to the device and cloud account, and limit who can retrieve report history.

Risk: Saved reports may expose sensitive child information if written to insecure paths.

Mitigation: Save reports only to access-controlled locations and delete unneeded copies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text analysis reports and Markdown history tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion classifications and suggested soothing actions; not a clinical assessment]

## Skill Version(s):

1.0.30 (source: ClawHub release; bundled frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
