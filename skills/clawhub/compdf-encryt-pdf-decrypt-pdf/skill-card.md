## Description: <br>
Encrypt PDFs with AES-128, AES-256, or RC4 options and decrypt authorized PDFs with ComPDF. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and document operations teams use this skill to prepare ComPDF Server API requests for PDF encryption, permission controls, and authorized PDF decryption. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may read a local ComPDF API key and use it to send selected PDFs to ComPDF for processing. <br>
Mitigation: Store the key only in the documented local private file, pass it only as the x-api-key header, and confirm the exact files before upload. <br>
Risk: Decryption could be requested for files the user is not authorized to unlock. <br>
Mitigation: Proceed with decryption only after the user explicitly confirms authorization for the affected document. <br>
Risk: Encryption, decryption, overwrite, deletion, upload, or permanent protection changes can affect sensitive or original documents. <br>
Mitigation: Identify affected files and obtain confirmation before external processing or any destructive or permanent document change. <br>
Risk: The artifact bundles broader ComPDF reference material than the encryption and decryption use case requires. <br>
Mitigation: Use only the supported Encrypt PDF and Decrypt PDF entries and their matching official reference sections for request planning. <br>


## Reference(s): <br>
- [ComPDF Endpoint Index](references/endpoint-index.md) <br>
- [Official ComPDF V2 API Reference Snapshot](references/official-api-reference.md) <br>
- [ComPDF API Reference](https://www.compdf.com/guides/api-reference/v2/) <br>
- [ComPDF Portal](https://www.compdf.com/compdf-portal/signin?utm_source=clawhub&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=clawhub_compdfkit_skills_en) <br>
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/compdf-encryt-pdf-decrypt-pdf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint, method, request fields, response fields, and next-step instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not output API keys or passwords; may include commands for maintaining the local API reference snapshot.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
