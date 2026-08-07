## Description: <br>
Alibaba Quark Scan helps an agent prepare commands and guidance for enhancing single document images through an external scan service, including image cleanup, crop correction, handwriting removal, watermark removal, and document-focused visual enhancement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and automation teams use this skill to route a single image URL, local image path, or base64 image into one of the documented scan scenes and return the external service result or saved processed image path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends supplied images to an external scanning service and requires an API key. <br>
Mitigation: Use it only for images the user has the right to process, confirm the service terms and data handling before sensitive use, and rotate the API key if it is exposed. <br>
Risk: The security summary flags overbroad routing language and support for questionable removal of exam answers and watermarks. <br>
Mitigation: Review requests before execution and reject uses that remove watermarks or answers without clear authorization. <br>
Risk: Processed images can be saved locally after service execution. <br>
Mitigation: Inspect and clean temporary output paths after use, especially when processing private, business, contract, certificate, or exam materials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/alibaba-quark-scan) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown, JSON responses, files] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON service responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save processed images to a local temporary image path when the external service returns image data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
