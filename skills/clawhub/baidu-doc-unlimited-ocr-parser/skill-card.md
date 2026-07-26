## Description: <br>
Calls Baidu Unlimited-OCR to parse PDFs, Word files, PowerPoint files, and images into structured Markdown, including HTML table markup for complex tables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maglanyulan](https://clawhub.ai/user/maglanyulan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-processing users can use this skill to submit supported documents or document URLs to Baidu Unlimited-OCR and retrieve Markdown suitable for review, RAG ingestion, or knowledge-base workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents, document URLs, OCR result links, and parsed output are sent to and handled by Baidu services. <br>
Mitigation: Use the skill only for documents approved for Baidu processing, and avoid confidential, regulated, customer, or otherwise sensitive material unless organizational policy permits it. <br>
Risk: Baidu API keys and secret keys are required to obtain access tokens. <br>
Mitigation: Store credentials in approved secret or environment-variable management, avoid committing them to skill files or shared settings, and rotate them if exposed. <br>
Risk: Downloaded Markdown and JSON parse results may contain sensitive source-document content. <br>
Mitigation: Treat generated result files and time-limited result URLs as sensitive artifacts, and review sharing, retention, and logging practices before use. <br>


## Reference(s): <br>
- [Baidu Unlimited-OCR API documentation](https://cloud.baidu.com/doc/OCR/s/fmr1p39gb) <br>
- [Baidu OCR pricing documentation](https://cloud.baidu.com/doc/OCR/s/Fls06fa15) <br>
- [Baidu AI console](https://console.bce.baidu.com/ai/) <br>
- [Baidu intelligent document analysis](https://ai.baidu.com/solution/intelligent-document-analysis) <br>
- [API parameters](references/parameters.md) <br>
- [Error codes](references/error_codes.md) <br>
- [API key setup](references/apikey-fetch.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown and JSON from Baidu OCR results, with command-line status and error output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Asynchronous processing returns a task ID, polls until completion, and may download Markdown and parse-result JSON from time-limited result URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
