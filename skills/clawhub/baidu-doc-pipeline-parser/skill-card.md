## Description: <br>
调用百度文档解析API解析文档，支持PDF、Word、Excel、PPT、图片等18+格式，提取文本、表格、版面分析、OCR识别及RAG文档分块。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maglanyulan](https://clawhub.ai/user/maglanyulan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to parse documents through Baidu's document analysis API, extracting text, tables, layout structure, OCR results, and RAG-ready document chunks from supported files or URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents, document URLs, downloaded parse results, and 30-day result links may contain sensitive information sent to or retrieved from Baidu services. <br>
Mitigation: Use only organization-approved documents and URLs, avoid confidential or regulated content unless the data flow is approved, and do not share or log result URLs. <br>
Risk: Baidu API keys and secret keys are required for normal use. <br>
Mitigation: Store credentials in environment variables or a dedicated secret store, and avoid committing, printing, or sharing them. <br>
Risk: The parser depends on external API availability, quotas, file limits, and asynchronous polling behavior. <br>
Mitigation: Check supported file size and format limits, handle quota and service-busy errors, and use bounded polling or retry behavior. <br>


## Reference(s): <br>
- [Baidu Document Parser API Documentation](https://ai.baidu.com/ai-doc/OCR/llxst5nn0) <br>
- [Baidu Intelligent Document Analysis Platform](https://ai.baidu.com/solution/intelligent-document-analysis) <br>
- [API Key Configuration Guide](references/apikey-fetch.md) <br>
- [API Parameters](references/parameters.md) <br>
- [Error Codes](references/error_codes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Baidu task status, Markdown result URLs, JSON parse results, page layouts, tables, OCR text, images, and document chunks.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
