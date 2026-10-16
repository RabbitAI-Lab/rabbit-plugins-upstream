## Description:

Uses Alibaba Cloud DTS-AI to parse local PDF, DOCX, PPTX, and image files into Markdown files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can convert specified local documents and images to Markdown through Alibaba Cloud DTS-AI, with their permission for cloud processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Specified documents are uploaded to Alibaba Cloud DTS-AI for parsing.

Mitigation: Parse only files the user authorizes and avoid sending sensitive documents unless cloud processing is acceptable.

Risk: The installer and automatic CLI or skill updates can change the installed software and skill files.

Mitigation: Review the remote installer or use an approved verified installation process; disable automatic skill updates if pinned behavior is required.

Risk: The CLI stores its API key and recovery state under the user's home directory.

Mitigation: Protect local credentials and recovery data with appropriate device and account access controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-dts-doc-parse)
- [Use the DTS-AI API to parse documents](https://help.aliyun.com/en/dts/use-cases/use-dtsai-api-to-parse-documents)
- [CreateDocParserJob API](https://help.aliyun.com/en/dts/developer-reference/api-dtsai-2026-04-01-createdocparserjob)
- [DescribeDocParserJobStatus API](https://help.aliyun.com/en/dts/developer-reference/api-dtsai-2026-04-01-describedocparserjobstatus)
- [DescribeDocParserJobResult API](https://help.aliyun.com/en/dts/developer-reference/api-dtsai-2026-04-01-describedocparserjobresult)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One output file per input; returns the saved file paths.]

## Skill Version(s):

0.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
