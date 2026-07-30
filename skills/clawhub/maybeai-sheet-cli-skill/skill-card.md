## Description: <br>
Helps agents inspect, import, edit, style, analyze, and share MaybeAI spreadsheets through the mbs CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[no7dw](https://clawhub.ai/user/no7dw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and spreadsheet operators use this skill to guide an agent through MaybeAI spreadsheet workflows with the mbs CLI, including workbook inspection, imports, table and range writes, formulas, styling, dashboards, and sharing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide public sharing or editor grants for MaybeAI spreadsheets. <br>
Mitigation: Require explicit confirmation before changing visibility or granting access; verify the target sheet, recipient email, and permission level, and prefer private or viewer access. <br>
Risk: Workbook metadata may send worksheet samples to the service for LLM summarization and caching. <br>
Mitigation: Avoid profiling sensitive workbooks without user approval; use targeted reads for exact values and treat summaries as orientation rather than complete audits. <br>
Risk: The MAYBEAI_API_TOKEN enables spreadsheet read, modification, import, export, and sharing operations. <br>
Mitigation: Use the token only in intended environments, avoid exposing it in command output or files, and verify write operations with CLI output and spreadsheet readback. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/no7dw/skills/maybeai-sheet-cli-skill) <br>
- [MaybeAI project homepage](https://github.com/OmniMCP-AI/maybeai-uni) <br>
- [Skill README](artifact/README.md) <br>
- [Command Catalog](artifact/references/cli-commands.md) <br>
- [Read/Write Reference](artifact/references/read-write.md) <br>
- [File Management Reference](artifact/references/file-management.md) <br>
- [Permission And Sharing Reference](artifact/references/permission-sharing.md) <br>
- [Workbook Profile Reference](artifact/references/workbook-profile.md) <br>
- [Charts and Formatting Reference](artifact/references/charts-formatting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MAYBEAI_API_TOKEN and the mbs CLI; write operations should be verified with CLI output and spreadsheet readback.] <br>

## Skill Version(s): <br>
0.16.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
