## Description: <br>
This skill helps an agent create a transferable Migration Package that summarizes project state, decisions, open work, and relevant project files so another AI session can continue the work without reading the full conversation history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shary-ho](https://clawhub.ai/user/shary-ho) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when moving project work to another AI model or a new chat session. It guides the agent to inspect available project context, write a structured Markdown handoff, and preserve relevant produced files where appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to inspect and package broad project files, conversation context, uploads, and git history. <br>
Mitigation: Before use, explicitly define allowed directories and files, exclude secrets and private documents, and review the attachment manifest before any downloadable package is produced. <br>
Risk: A handoff package may include stale, incorrect, or over-broad context if the agent gathers files without clear boundaries. <br>
Mitigation: Ask the agent to mark unavailable information as unknown, verify important files from disk, and keep the handoff focused on information needed for continuation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shary-ho/skills/llm-session-handoff-assistant) <br>
- [Migration Package template](artifact/references/template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Guidance] <br>
**Output Format:** [Markdown handoff document with an optional collected file bundle] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Follows a 16-section migration template and may include an attachment manifest for collected files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
