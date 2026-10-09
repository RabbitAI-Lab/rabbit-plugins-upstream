## Description:

Parses local PDF, Word, PowerPoint, and image files into Markdown using Alibaba Cloud DTS-AI after user authorization for cloud processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can convert specified local documents and images into Markdown with Alibaba Cloud DTS-AI. The workflow requires authorization before uploading files for cloud processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents are uploaded for cloud parsing.

Mitigation: Use only for explicitly requested files after the user authorizes cloud processing; avoid sensitive files unless the service is approved.

Risk: CLI installation may run a remote installer.

Mitigation: Review the installation source and method, and run it only with organizational approval.

Risk: Automatic CLI and skill updates may change code between uses.

Mitigation: Review update behavior and consider setting DTS_SKILLS_AUTO_UPDATE=0 when automatic updates are not approved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-dts-doc-parse)
- [Alibaba Cloud DTS-AI document parsing guide](https://help.aliyun.com/en/dts/use-cases/use-dtsai-api-to-parse-documents)
- [Alibaba Cloud DTS-AI parser job API](https://help.aliyun.com/en/dts/developer-reference/api-dtsai-2026-04-01-createdocparserjob)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saves a Markdown file for each parsed input and reports its output path.]

## Skill Version(s):

0.0.1-beta.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
