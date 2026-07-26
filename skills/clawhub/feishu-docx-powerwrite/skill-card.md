## Description: <br>
Feishu Docx PowerWrite helps agents turn Markdown into well-formatted Feishu/Lark Docx content using OpenClaw's Feishu document tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiongjjlj](https://clawhub.ai/user/xiongjjlj) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and Feishu/Lark users use this skill to create, append, or replace Docx content from Markdown while preserving headings, lists, nesting, and code blocks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Replace mode can overwrite the target Feishu/Lark document. <br>
Mitigation: Prefer append mode for existing documents, verify the document ID or link before writing, and require explicit confirmation before replacement. <br>
Risk: Feishu credentials, tokens, or document links could be exposed if hardcoded into skill files or prompts. <br>
Mitigation: Use the user's own Feishu app credentials and scopes, and avoid hardcoding tokens, chat IDs, open IDs, or document links. <br>
Risk: Writes can fail or target the wrong document when Feishu app permissions or document collaboration settings are incomplete. <br>
Mitigation: Verify Docx/Drive scopes and ensure the bot or app has access to the intended document before writing. <br>


## Reference(s): <br>
- [Feishu Docx PowerWrite Skill Page](https://clawhub.ai/xiongjjlj/skills/feishu-docx-powerwrite) <br>
- [Docx templates](references/templates.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline tool names and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports append and replace workflows; replace mode is destructive and requires explicit confirmation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
