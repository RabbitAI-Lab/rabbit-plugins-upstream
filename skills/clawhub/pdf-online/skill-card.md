## Description:

Parse PDF, image, Word, or PPT files with SoMark and publish the result to Feishu, DingTalk, or Notion as editable documents, spreadsheets, record tables, or databases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[soul-code](https://clawhub.ai/user/soul-code)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to convert parsed SoMark document results into editable Feishu, DingTalk, or Notion destinations. It supports raw document parsing through the separate official SoMark parser and direct import of explicitly supplied matching Markdown and JSON artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or modify Feishu, DingTalk, or Notion content through logged-in platform accounts.

Mitigation: Install and run it only for workflows where external document or database publishing is intended, and review the selected platform target before execution.

Risk: Image URLs from source documents or explicit SoMark artifacts may be fetched from the agent environment and uploaded to the destination platform.

Mitigation: Review source documents and supplied Markdown/JSON artifacts before publishing, especially when they contain external image URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/soul-code/skills/pdf-online)
- [DingTalk common adapter contract](artifact/platforms/dingtalk/references/common-contract.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON lifecycle events, generated files, and platform publishing actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify Feishu, DingTalk, or Notion content through the user's authenticated platform accounts.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
