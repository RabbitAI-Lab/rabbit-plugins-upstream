## Description:

Helps an agent send regular files and image attachments through Feishu/Lark by using the separate file_key and image_key upload paths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to upload local reports, archives, PDFs, code files, and generated images to Feishu or Lark recipients. It is most useful when a workflow needs reliable attachment delivery instead of sending local file paths as message text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles local files and can upload files the user did not intend to share.

Mitigation: Use it only with explicit file paths selected for sharing, avoid broad or sensitive local paths, and confirm the intended recipient before upload.

Risk: The workflow requires Feishu/Lark app credentials and may expose secrets if they are passed on the command line or read from local configuration files.

Mitigation: Prefer a scoped secret manager or protected environment variables, avoid printing secrets, and do not ask the agent to search local configuration files for credentials.

Risk: Attachment delivery can expose sensitive content to users or groups in Feishu/Lark.

Mitigation: Review file contents and recipient identifiers before sending, especially for group chats or automated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-file-sender)
- [Feishu app access token endpoint](https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal)
- [Feishu file upload endpoint](https://open.feishu.cn/open-apis/im/v1/files)
- [Feishu message send endpoint](https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local file paths, recipient identifiers, Feishu/Lark app credentials, upload keys, and troubleshooting steps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
