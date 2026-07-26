## Description: <br>
Track workouts, log sets, manage exercises and templates with workout-cli. Supports multi-user profiles. Use when helping users record gym sessions, view history, or analyze strength progression. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gricha](https://clawhub.ai/user/gricha) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill to help users record gym sessions, manage workout profiles, maintain exercise libraries and templates, and review workout history, PRs, volume, and progression. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delete, cancel, undo, edit, and profile deletion commands can change or remove workout history. <br>
Mitigation: Confirm the exact profile, session, exercise, or set before using destructive commands, and export or back up important workout history first. <br>
Risk: Incorrect weights or reps can make PR, volume, and progression analysis misleading. <br>
Mitigation: Ask for missing weight or rep values before logging, record the actual numbers used, and keep notes for context rather than data correction. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the workout CLI and can include JSON-capable command variants when useful.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
