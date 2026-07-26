## Description: <br>
This skill converts user-selected images, screenshots, or scanned pages into Word, Excel, or PDF files through Quark Scanner's document conversion service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yescan-ai](https://clawhub.ai/user/yescan-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need a single image, screenshot, or scan converted into an editable Word or Excel document, or into a PDF, while preserving complex layout. It is not intended for pure text extraction, image enhancement, batch processing, or creating documents from scratch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected images or scans are sent to Quark's scan-business.quark.cn service for processing. <br>
Mitigation: Use the skill only when that third-party processing is acceptable, and avoid highly sensitive IDs, contracts, medical, financial, or confidential business documents unless approved. <br>
Risk: Generated Office or PDF files are saved locally under the system temporary directory and may remain after the session. <br>
Mitigation: Clean up generated files from the temp directory after use, especially when source documents contain sensitive content. <br>
Risk: The skill depends on the SCAN_WEBSERVICE_KEY credential. <br>
Mitigation: Store the key in the configured environment only, avoid exposing it in prompts or logs, and rotate or revoke it if leakage is suspected. <br>


## Reference(s): <br>
- [Quark Scanner Open Platform](https://scan.quark.cn/business) <br>
- [ClawHub skill listing](https://clawhub.ai/yescan-ai/skills/alibaba-quark-transoffice) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON, files] <br>
**Output Format:** [JSON response with a local file path when conversion succeeds, plus a generated DOCX, XLSX, or PDF file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAN_WEBSERVICE_KEY and accepts one image URL, local image path, or base64 image per invocation.] <br>

## Skill Version(s): <br>
1.1.19 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
