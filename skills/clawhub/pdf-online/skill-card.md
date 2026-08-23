## Description:

Parse PDF, image, Word, or PPT files with SoMark and publish the result to Feishu, DingTalk, or Notion as editable documents, spreadsheets, record tables, or databases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[soul-code](https://clawhub.ai/user/soul-code)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to parse local PDF, image, Word, or PPT files once with SoMark and publish the resulting structured content into Feishu, DingTalk, or Notion. It also supports importing explicitly supplied matching SoMark Markdown and JSON artifacts into those platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parsed document contents may be sent to external Feishu, DingTalk, or Notion workspaces.

Mitigation: Use the skill only for documents intended for the selected external workspace and confirm the destination before publishing sensitive content.

Risk: Local conversion manifests and intermediate artifacts may persist document-derived content or diagnostic details.

Mitigation: Run the skill in an environment where local artifacts are acceptable and clean up generated evidence directories according to the user's data-handling policy.

Risk: Untrusted supplied SoMark Markdown or JSON can include remote image URLs that are later imported or fetched by platform adapters.

Mitigation: Accept explicit SoMark artifact pairs only from trusted sources and review remote image URLs before using them with confidential workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/soul-code/skills/pdf-online)
- [Root skill entry point](artifact/SKILL.md)
- [Feishu adapter](artifact/platforms/feishu/SKILL.md)
- [DingTalk adapter](artifact/platforms/dingtalk/SKILL.md)
- [Notion adapter](artifact/platforms/notion/SKILL.md)
- [DingTalk common foundation contract](artifact/platforms/dingtalk/references/common-contract.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown, JSON manifests, platform import payloads, shell commands, and user-facing status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOMARK_API_KEY and platform-specific authorization for the selected destination.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
