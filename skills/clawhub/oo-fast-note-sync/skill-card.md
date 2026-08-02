## Description: <br>
Fast Note Sync lets an agent read, search, create, update, and delete notes, vaults, and attachments through the OOMOL fast_note_sync connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Fast Note Sync from an agent, including vault, note, and attachment workflows. It supports read operations as well as confirmed write and destructive changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create or replace notes, vaults, or attachments in the connected Fast Note Sync account. <br>
Mitigation: Confirm the exact action name, target, and JSON payload with the user before running write actions. <br>
Risk: Destructive actions can delete attachments or vaults, or move notes to the recycle bin. <br>
Mitigation: Require explicit approval for the specific target before running destructive actions. <br>
Risk: First-time CLI installation, login, or service connection steps grant account access through OOMOL. <br>
Mitigation: Have the user perform setup or approve the exact command and connection flow before proceeding. <br>


## Reference(s): <br>
- [Fast Note Sync homepage](https://github.com/haierkeys/fast-note-sync-service) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fast-note-sync) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions can return JSON data and execution metadata; write and destructive operations require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
