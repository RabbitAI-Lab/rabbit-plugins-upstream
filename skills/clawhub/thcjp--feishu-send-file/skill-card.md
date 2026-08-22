## Description:

Feishu-send-file helps agents send ordinary files and image attachments through Feishu or Lark by using the correct file_key and image_key upload flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to have an agent send generated reports, PDFs, archives, code files, and local images to Feishu or Lark users and group chats. It is especially useful when avoiding path-text fallback by choosing the proper ordinary-file or image upload route.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send local files outside the current environment through Feishu or Lark.

Mitigation: Use it only with explicitly selected files and recipients, and review the file path before any upload command is run.

Risk: The skill documentation shows app_secret values being passed directly to commands or read from local configuration.

Mitigation: Prefer secure secret injection, avoid printing secrets in logs, and do not let the agent discover or expose Feishu credentials unnecessarily.

Risk: Callback URLs can send data to destinations that may not be trusted.

Mitigation: Treat callback_url use as unsafe unless the destination, payload, and operator intent are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-send-file)
- [Feishu app access token API](https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal)
- [Feishu file upload API](https://open.feishu.cn/open-apis/im/v1/files)
- [Feishu message send API](https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local file paths, Feishu or Lark recipient IDs, and app credentials supplied by the operator.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter version is 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
