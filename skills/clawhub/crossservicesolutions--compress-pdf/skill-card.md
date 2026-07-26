## Description: <br>
Compress a user-provided PDF by uploading it to Cross-Service-Solutions, polling until completion, then returning a download URL for the compressed file. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crossservicesolutions](https://clawhub.ai/user/crossservicesolutions) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to compress selected PDF files through Cross-Service-Solutions and receive job status plus a compressed-file download URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected PDFs are uploaded to Cross-Service-Solutions and the compressed output is returned through a third-party-hosted download URL. <br>
Mitigation: Use only for documents approved for that provider; avoid confidential, regulated, legal, financial, or personal documents unless the provider's privacy and retention practices are approved. <br>
Risk: The Cross-Service-Solutions API key could be exposed if pasted into shared chats, logs, or command history. <br>
Mitigation: Use a dedicated API key, pass it through a secret or environment variable, and do not echo or log the key. <br>


## Reference(s): <br>
- [ClawHub Compress PDF skill page](https://clawhub.ai/crossservicesolutions/skills/compress-pdf) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [JSON result with job status, download URL, file name, and compression settings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided PDF and Cross-Service-Solutions API key; optional image quality and DPI settings control compression.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
