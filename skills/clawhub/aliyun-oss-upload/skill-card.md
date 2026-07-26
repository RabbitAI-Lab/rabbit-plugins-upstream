## Description: <br>
Uploads selected local files to Alibaba Cloud OSS and generates temporary signed access URLs after the required OSS environment variables are configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chengjiaxiongkf](https://clawhub.ai/user/chengjiaxiongkf) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to upload a chosen local file to an Alibaba Cloud OSS bucket, then return a temporary signed URL for sharing or downstream access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad or long-lived Alibaba Cloud credentials could expose more OSS access than this upload workflow needs. <br>
Mitigation: Use a dedicated least-privilege RAM user or temporary credential scoped to the target bucket and required object operations. <br>
Risk: The agent may upload an unintended or sensitive local file if the requested path is not reviewed. <br>
Mitigation: Confirm the selected file path and OSS object key before running the upload command. <br>
Risk: Temporary signed URLs can expose uploaded content while they remain valid. <br>
Mitigation: Keep signed URL expirations short and use private bucket permissions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chengjiaxiongkf/skills/aliyun-oss-upload) <br>
- [Aliyun OSS configuration guide](references/config.md) <br>
- [Alibaba Cloud OSS regions and endpoints](https://help.aliyun.com/document_detail/31837.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with CLI commands, upload status, and signed URL output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Signed URL expiry is configurable, with a default of 3600 seconds; successful use requires Alibaba Cloud OSS credentials and bucket configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
