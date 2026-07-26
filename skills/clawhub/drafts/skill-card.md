## Description: <br>
Manage Drafts app notes via CLI on macOS, including creating, listing, viewing, editing, appending, prepending, and running actions on drafts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nerveband](https://clawhub.ai/user/nerveband) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Drafts users use this skill to manage Drafts notes from an agent workflow on macOS when Drafts is running. It is suited for creating notes, searching or listing drafts, updating draft content, and triggering Drafts actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Draft update commands can overwrite or change note content. <br>
Mitigation: Be explicit about the target draft UUID and review replace, append, and prepend operations before relying on the changed note. <br>
Risk: Running Drafts actions can trigger local automations. <br>
Mitigation: Only run trusted Drafts actions and confirm the intended action name and draft or text input before execution. <br>
Risk: The skill depends on a third-party CLI and local Drafts automation on macOS. <br>
Mitigation: Install it only in trusted macOS environments where Drafts is running and the external CLI source is trusted. <br>


## Reference(s): <br>
- [Drafts CLI on ClawHub](https://clawhub.ai/nerveband/skills/drafts) <br>
- [Drafts](https://getdrafts.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON command output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS, the Drafts app running, and the drafts CLI binary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
