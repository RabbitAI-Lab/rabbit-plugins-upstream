## Description:

Compress a user-provided PDF by uploading it to Cross-Service-Solutions, polling until completion, then returning a download URL for the compressed file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crossservicesolutions](https://clawhub.ai/user/crossservicesolutions)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to compress PDF files through the Cross-Service-Solutions API and receive a structured result with the job status, output file name, download URL, and settings used.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF files are uploaded to an external service.

Mitigation: Use the skill only for PDFs the user is comfortable sending to Cross-Service-Solutions.

Risk: The helper script can be redirected to send the PDF and API token to an arbitrary server.

Mitigation: Do not allow untrusted users or wrappers to set --base-url or SOLUTIONS_BASE_URL.

Risk: API tokens may be exposed if passed or logged unsafely.

Mitigation: Prefer environment or secret-manager credentials and never echo or log the API key.

## Reference(s):

- [Compress PDF on ClawHub](https://clawhub.ai/crossservicesolutions/skills/compress-pdf)
- [Cross-Service-Solutions publisher profile](https://clawhub.ai/user/crossservicesolutions)
- [Cross-Service-Solutions API registration](https://login.cross-service-solutions.com/register)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON result and human-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns job status, download URL when available, file name, and compression settings.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
