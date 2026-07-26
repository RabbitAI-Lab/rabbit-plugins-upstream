## Description: <br>
调用百度 PaddleOCR-VL 大模型 API 解析 PDF、Word、PPT、图片等文档，输出结构化 Markdown 或 JSON 结果，并支持复杂版面、表格、公式、手写文本和多语种内容识别。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maglanyulan](https://clawhub.ai/user/maglanyulan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-processing teams use this skill to submit files or URLs to Baidu PaddleOCR-VL, poll asynchronous parsing tasks, and retrieve Markdown or JSON results for complex documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The shipped CLI may query a hard-coded Baidu task ID while using the user's Baidu credentials. <br>
Mitigation: Review and fix or verify the CLI before execution so it submits and parses the user-selected file or URL. <br>
Risk: Documents and parsing results may be sent to or retrieved from Baidu cloud services. <br>
Mitigation: Use only documents approved for Baidu cloud processing and protect BAIDU_DOC_AI_API_KEY and BAIDU_DOC_AI_SECRET_KEY. <br>
Risk: API quota, QPS, file-size, page-count, and polling limits can cause failed or delayed parsing. <br>
Mitigation: Validate file size and type before submission, handle documented error codes, and use bounded polling with retry behavior for transient service errors. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maglanyulan/skills/baidu-doc-vlm-parser) <br>
- [Baidu PaddleOCR-VL API documentation](https://cloud.baidu.com/doc/OCR/s/3mi73at9o) <br>
- [Baidu OCR error code documentation](https://cloud.baidu.com/doc/OCR/s/dk3iqnq51) <br>
- [Baidu API key setup documentation](https://ai.baidu.com/ai-doc/REFERENCE/Ck3dwjhhu#1-获取aksk) <br>
- [Baidu document analysis pricing and purchase documentation](https://cloud.baidu.com/doc/OCR/s/Fls06fa15#%E6%96%87%E6%A1%A3%E8%A7%A3%E6%9E%90%EF%BC%88paddleocr-vl%EF%BC%89) <br>
- [API parameters reference](artifact/references/parameters.md) <br>
- [API key configuration guide](artifact/references/apikey-fetch.md) <br>
- [Error codes reference](artifact/references/error_codes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON responses and shell or Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May retrieve Baidu-hosted Markdown and JSON result URLs; output depends on Baidu API credentials, quotas, polling status, and documented file limits.] <br>

## Skill Version(s): <br>
1.0.4 (source: evidence.release.version and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
