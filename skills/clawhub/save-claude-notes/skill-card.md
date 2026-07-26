## Description: <br>
Save the latest or current Claude Code Q&A to a local Markdown note. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiao2769433](https://clawhub.ai/user/xiao2769433) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Claude Code users use this skill to save the current or latest Q&A into local Markdown notes, either in a daily note, an exact Markdown file, or a target directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The submitted artifact references a save-claude-notes shell script that is not included. <br>
Mitigation: Install or use the skill only after verifying the missing script from the package or another trusted source. <br>
Risk: Using --latest may read private Claude Code transcript content and append it to local Markdown notes. <br>
Mitigation: Review saved notes for secrets and redact sensitive content before or immediately after saving. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/xiao2769433/save-claude-notes) <br>
- [ClawHub skill page](https://clawhub.ai/xiao2769433/skills/save-claude-notes) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown guidance with bash and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands append selected Q&A content to local Markdown notes; sensitive content may need redaction or explicit confirmation before saving.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
