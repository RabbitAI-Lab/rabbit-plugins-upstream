## Description:

Merge multiple user-provided PDF files by uploading them to Cross-Service-Solutions, polling until completion, then returning a download URL for the merged PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crossservicesolutions](https://clawhub.ai/user/crossservicesolutions)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to merge multiple PDF files through the Cross-Service-Solutions API and receive a structured result with the job status and merged PDF download URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected PDFs and the API key to Cross-Service-Solutions, and evidence.security notes that a base-url override can redirect them away from the stated service.

Mitigation: Use only approved documents and review or remove the base-url override before use so PDFs and credentials cannot be redirected.

Risk: Confidential, legal, financial, medical, or regulated documents may be exposed to a third-party PDF processing service.

Mitigation: Avoid those document classes unless Cross-Service-Solutions handling terms and internal approvals cover the intended use.

## Reference(s):

- [ClawHub Merge PDF release page](https://clawhub.ai/crossservicesolutions/skills/merge-pdf)
- [Cross-Service-Solutions API registration](https://login.cross-service-solutions.com/register)
- [Cross-Service-Solutions PDF merge API endpoint](https://api.xss-cross-service-solutions.com/solutions/solutions/api/30)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Structured JSON result with job status, download URL, output file name, and input file names.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided PDF files and a Cross-Service-Solutions API key.]

## Skill Version(s):

1.0.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
