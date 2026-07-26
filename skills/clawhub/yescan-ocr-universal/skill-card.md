## Description: <br>
由夸克扫描王提供的高准取率 OCR 文字识别工具，支持印刷、手写、表格、多语言、公式等各种场景。支持图片、截图、扫描件中的文字提取，包括手写文档、表格内容、数学公式、商品图片等复杂场景。精准识别各类证件（身份证、社保卡、驾驶证、行驶证、港澳通行证、学位证等证件）及票据（增值税发票、火车票、英文发票等票据），同时支持医疗报告单、营业执照、习题题目等专业文档识别。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yescan-ai](https://clawhub.ai/user/yescan-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent workflows use this skill to extract OCR text and structured fields from a single image URL, local image path, or base64 image. It supports handwriting, tables, identity documents, invoices, formulas, medical reports, business licenses, product images, and general text extraction through Quark's OCR service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images submitted to this skill are sent to Quark's OCR service and may contain sensitive IDs, invoices, medical documents, or other confidential content. <br>
Mitigation: Use the skill only with documents that policy permits Quark to process; avoid submitting content that should not leave the user's machine. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yescan-ai/skills/yescan-ocr-universal) <br>
- [Quark Scan business platform](https://scan.quark.cn/business) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, files] <br>
**Output Format:** [JSON responses and command output containing OCR text, structured fields, or generated file paths returned by the service] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and SCAN_WEBSERVICE_KEY; each invocation processes one image URL, local image path, or base64 image.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
