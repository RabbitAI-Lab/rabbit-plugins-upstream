## Description:

Prevent file-writing via Windows PowerShell to avoid GBK encoding corruption when Kimi Code CLI is running on Windows and the task involves creating, writing, or modifying text files, especially with Chinese or other non-ASCII characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jvy](https://clawhub.ai/user/jvy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when working on Windows systems where PowerShell may write text using GBK or another locale-dependent encoding. It steers file creation and edits toward deterministic UTF-8 file tools, or explicit UTF-8 PowerShell writes when shell use is unavoidable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using PowerShell redirection or default file-writing commands on Chinese Windows systems can silently corrupt Chinese or other non-ASCII text.

Mitigation: Use dedicated UTF-8 file-editing tools for writes and edits; when PowerShell file output is unavoidable, set UTF-8 explicitly and verify the resulting file is readable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jvy/skills/powershell)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown guidance with PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on UTF-8-safe file creation and editing practices on Windows PowerShell.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
