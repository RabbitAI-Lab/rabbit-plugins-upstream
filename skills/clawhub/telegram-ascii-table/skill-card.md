## Description: <br>
Format tabular data as ASCII box tables for Telegram. Stdin-only input eliminates shell injection risks. Handles smart column sizing, text wrapping, and proper padding for monospace display. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nalg](https://clawhub.ai/user/nalg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and other Telegram users use this skill to turn pipe-delimited stdin data into fixed-width tables that display cleanly in Telegram code blocks. It supports desktop and mobile table modes, custom widths, and wrapped cell text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-supplied table data may contain private information that will appear in the generated output. <br>
Mitigation: Only pipe or paste data that is acceptable to include in the resulting table, and review the output before sending it. <br>
Risk: Pipe characters, very long words, emoji, CJK, or mobile Telegram rendering can affect table alignment or cell parsing. <br>
Mitigation: Use the documented mobile mode for mobile recipients, choose an appropriate width, and avoid unescaped pipe characters inside cell content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nalg/skills/telegram-ascii-table) <br>
- [Publisher profile](https://clawhub.ai/user/nalg) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Plain text ASCII or Unicode table, usually wrapped in a Markdown code block for Telegram.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Input is read from stdin as pipe-delimited rows; desktop, mobile, and custom-width modes are available.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
