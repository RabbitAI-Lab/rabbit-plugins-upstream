## Description: <br>
亚马逊店铺文件上传技能，通过 LinkFox 网关调用 Amazon SP-API Uploads API v2020-11-01 创建上传目的地，并将文件上传到返回的 URL 以供 A+ Content、Messaging 等后续 API 使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and marketplace operators use this skill to create Amazon SP-API upload destinations, compute or provide contentMD5 values, and upload binary files for downstream A+ Content or Messaging workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full upload and API responses, including presigned URLs, headers, upload IDs, or seller metadata, may be saved in the workspace linkfox session directory. <br>
Mitigation: Run the skill only in workspaces where those saved JSON files are acceptable, restrict access to the workspace, and delete the saved response files after use when they contain sensitive data. <br>
Risk: Uploads depend on LinkFox API credentials and Amazon store authorization state. <br>
Mitigation: Use the required LinkFox API key environment variable and the companion Amazon store auth skill only in approved environments; rotate or revoke credentials if response files or shell history expose sensitive values. <br>
Risk: The uploaded bytes must match the contentMD5 used when creating the Amazon upload destination. <br>
Mitigation: Prefer filePath or contentBase64 inputs that allow the script to compute contentMD5, or verify the Base64 MD5 manually before uploading. <br>


## Reference(s): <br>
- [linkfox-amazon-store-uploads API reference](references/api.md) <br>
- [Amazon SP-API createUploadDestinationForResource](https://developer-docs.amazon.com/sp-api/reference/createuploaddestinationforresource) <br>
- [Amazon SP-API create an upload destination](https://developer-docs.amazon.com/sp-api/docs/create-an-upload-destination) <br>
- [Amazon SP-API Messaging API reference](https://developer-docs.amazon.com/sp-api/docs/messaging-api-v1-reference) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-uploads) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell commands; scripts emit JSON responses or summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save full API/upload responses under a local linkfox session directory and print full JSON or a concise summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
