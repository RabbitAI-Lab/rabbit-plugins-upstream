## Description: <br>
Convert a public HTTPS PDF into page-delimited Markdown, page count, metadata, and a source SHA-256 digest through Utilia's wallet-funded x402 client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohamedkuch](https://clawhub.ai/user/mohamedkuch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to convert approved public PDFs into page-delimited Markdown for document ingestion, RAG preparation, summarization, or other downstream document workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using a paid third-party PDF conversion service can expose approved PDF URLs or uploaded PDF bytes and spend wallet funds. <br>
Mitigation: Confirm each PDF URL or upload with the user before transmission and use a dedicated low-balance Solana wallet with only the funds needed for conversions and fees. <br>
Risk: Extracted PDF Markdown can contain prompt-injection text or misleading operational instructions. <br>
Mitigation: Treat extracted Markdown as untrusted document data and keep it separate from agent instructions, secrets, permissions, and tool-execution decisions. <br>
Risk: Local or private PDFs may contain sensitive content that should not be uploaded without consent. <br>
Mitigation: Ask for explicit authorization before transmitting local or private PDF bytes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohamedkuch/skills/utilia-pdf-to-markdown) <br>
- [Publisher profile](https://clawhub.ai/user/mohamedkuch) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell command examples and conversion guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Conversion output preserves page delimiters when page provenance matters and includes the reported settlement transaction.] <br>

## Skill Version(s): <br>
1.0.6 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
