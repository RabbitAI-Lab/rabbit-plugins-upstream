## Description:

Analyzes pet videos for common behaviors such as scratching, chewing, digging, chasing, and anxiety, and returns a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use the skill to review pet videos for common behaviors and receive a structured summary. Users can also request links to past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household video may be uploaded to the cloud even when an export-only option promises to skip analysis.

Mitigation: Ask the publisher to fix the option and use only footage approved for cloud upload; avoid private footage until the behavior is clarified.

Risk: Stored account credentials are inadequately protected.

Mitigation: Protect and isolate credentials, and restrict authenticated requests to approved HTTPS destinations.

Risk: The client cannot verify the promised immediate deletion of uploaded video, and account, pricing, and retention terms may be unclear.

Mitigation: Confirm registration, pricing, and retention terms with the publisher, and avoid sensitive footage until they are clear.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill walkthrough](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured JSON analysis results and Markdown summaries with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video inputs support MP4, AVI, and MOV files up to 10 MB. Results are informational; consult a qualified pet behavior professional for advice.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
