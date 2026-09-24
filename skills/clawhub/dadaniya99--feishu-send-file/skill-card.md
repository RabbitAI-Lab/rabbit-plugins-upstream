## Description:

Helps an agent send Feishu or Lark file attachments and recover local image sends by uploading the file or image before messaging the recipient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dadaniya99](https://clawhub.ai/user/dadaniya99)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to deliver approved local files or images to Feishu or Lark users from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Application secrets may be exposed through prompts, shell history, process arguments, or logs.

Mitigation: Use a Feishu or Lark app with narrowly scoped permissions, keep app_secret in a protected secret channel, and avoid passing secrets through free-form prompts or persisted command text.

Risk: String-built command execution or unclear recipient and file choices could send unintended content.

Mitigation: Require a user-approved recipient and file path before sending, and invoke helper scripts with argument arrays instead of interpolated shell strings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dadaniya99/skills/feishu-send-file)
- [Feishu Open Platform](https://open.feishu.cn)
- [Lark Open Platform](https://open.larksuite.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with shell commands and Python invocation examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Feishu or Lark app ID, app secret, recipient open_id, and an approved local file or image path.]

## Skill Version(s):

1.2.1 (source: server release evidence and artifact/skill.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
