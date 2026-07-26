## Description: <br>
Quark Scan enhances single images and screenshots by improving clarity, removing visual artifacts such as handwriting, watermarks, shadows, screen patterns, and background color, and returning an optimized high-definition image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yescan-ai](https://clawhub.ai/user/yescan-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to send a single image, screenshot, document photo, receipt, exam page, contract, or similar picture to Quark Scan for visual cleanup and enhancement. It is not intended for OCR, document conversion, video processing, batch processing, or AI image generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images, including potentially sensitive IDs, contracts, receipts, exams, or notes, are sent to Quark's remote scan service. <br>
Mitigation: Use the skill only after confirming the user is comfortable with remote processing, review Quark's privacy terms, and avoid sensitive images unless necessary. <br>
Risk: Enhanced image outputs are saved locally in the system temporary directory and may persist after the agent response. <br>
Mitigation: Periodically clean the temporary output folder when local persistence is not desired. <br>
Risk: The skill requires SCAN_WEBSERVICE_KEY for the remote service. <br>
Mitigation: Store the API key in the configured environment variable, avoid exposing it in prompts or logs, and rotate or revoke it if it may have leaked. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yescan-ai/skills/alibaba-quark-scan) <br>
- [Quark Scan business portal](https://scan.quark.cn/business) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Guidance] <br>
**Output Format:** [JSON response containing status, message, and a local path to the saved enhanced image when processing succeeds] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and SCAN_WEBSERVICE_KEY; accepts one image input as a URL, local path, or base64 string; saves returned images under the system temporary directory.] <br>

## Skill Version(s): <br>
1.0.18 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
