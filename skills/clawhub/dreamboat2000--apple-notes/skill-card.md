## Description: <br>
Manage Apple Notes via the `memo` CLI on macOS by creating, viewing, editing, deleting, searching, moving, and exporting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dreamboat2000](https://clawhub.ai/user/dreamboat2000) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Apple Notes from a macOS terminal through the `memo` CLI, including note creation, search, organization, export, and user-requested edits or deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit, move, export, or delete Apple Notes when the user asks it to. <br>
Mitigation: Review the selected note and intended operation before running edit, move, export, or delete commands; treat deletion as potentially irreversible. <br>
Risk: The third-party `memo` CLI requires Automation access to Apple Notes. <br>
Mitigation: Install the CLI only if granting Apple Notes Automation access is acceptable, and review macOS privacy permissions before use. <br>
Risk: The skill cannot edit notes containing images or attachments. <br>
Mitigation: Use it for text-oriented Apple Notes workflows and handle attachment-heavy notes directly in Notes.app. <br>


## Reference(s): <br>
- [Apple Notes skill on ClawHub](https://clawhub.ai/dreamboat2000/apple-notes) <br>
- [memo CLI homepage](https://github.com/antoniorodr/memo) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS, the `memo` CLI, Apple Notes.app access, and Automation permission when prompted.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
