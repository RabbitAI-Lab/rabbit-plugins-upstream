## Description:

Helps agents convert Markdown content into Feishu/Lark document block JSON and guidance for writing those blocks through the document API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation builders, and teams use this skill to prepare Markdown content for Feishu/Lark documents by mapping common document elements to API block structures. It is intended for document conversion and writing workflows, not for encrypted-file recovery or complex human judgment tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad file, write, and command-execution authority may access sensitive local content or perform unintended local actions.

Mitigation: Use the skill only for explicit Feishu/Lark document-writing tasks, limit provided files to the minimum needed, and confirm file access, writes, image uploads, and command execution before approval.

Risk: API keys or document credentials could be exposed through prompts, logs, shell commands, or generated content.

Mitigation: Use environment variables or platform secret storage, avoid hardcoding credentials, and redact tokens from logs and outputs.

Risk: Document writes and media uploads may modify remote Feishu/Lark content or upload unintended data.

Mitigation: Confirm target document identifiers, destination permissions, and content previews before allowing API writes or uploads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/feishu-doc-write)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Feishu/Lark block JSON, execution notes, retry guidance, and API key setup instructions.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
