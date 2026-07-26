## Description: <br>
Manage Apple Notes via deterministic local scripts (create, append, list, search, export, and edit). Use when a user asks OpenClaw to add a note, list notes, search notes, or manage note folders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clinchcc](https://clawhub.ai/user/clinchcc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users and agents use this skill to create, list, search, export, and manage Apple Notes through deterministic local shell scripts on macOS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires local helper access to Apple Notes and may trigger macOS automation permission prompts. <br>
Mitigation: Install only when that access is acceptable, review the bundled scripts and memo CLI, and approve macOS automation prompts deliberately. <br>
Risk: Export workflows can write note contents to local files and may expose sensitive notes if used broadly. <br>
Mitigation: Use narrow search terms and destination directories, and avoid exporting sensitive notes unless the export is necessary. <br>
Risk: Editing existing notes is documented as fragile. <br>
Mitigation: Prefer creating new notes or append-style workflows; use interactive editing only when explicitly requested. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clinchcc/skills/notesctl-skill-for-openclaw) <br>
- [Publisher profile](https://clawhub.ai/user/clinchcc) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Files, Guidance] <br>
**Output Format:** [Shell commands and plain-text receipts; exported notes as files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local macOS dependencies: memo, python3, and osascript.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
