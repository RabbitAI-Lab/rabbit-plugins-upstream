## Description: <br>
C Disk Cleanup helps a Windows user inspect C: drive usage, explain cleanup options in plain language, and perform confirmation-gated cleanup steps that favor backups or official migration paths over permanent deletion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiamiaolou-art](https://clawhub.ai/user/jiamiaolou-art) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Windows users and support agents use this skill to diagnose a full C: drive, separate low-risk cache cleanup from user-data decisions, and guide cleanup with explicit consent. It is especially aimed at non-expert users who need readable explanations, recovery paths, and repeatable cleanup habits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can scan large parts of C:, move files, remember cleanup preferences, and run Windows maintenance commands. <br>
Mitigation: Keep initial use scan-only, require explicit confirmation for each cleanup run, and review the proposed paths and actions before allowing file movement or maintenance commands. <br>
Risk: Some documented actions can change system or app files beyond the strongest safety promises in the skill documentation. <br>
Mitigation: Prefer the conservative cache cleanup flow, keep backups or recovery paths available, and avoid advanced Program Files compression, CompactOS, DISM, junction, and backup-deletion steps unless the user understands how to recover. <br>
Risk: Moving active app data or chat databases can damage applications or make records appear missing. <br>
Mitigation: Use official app migration flows for chat data, close relevant applications before moving cache folders, and verify restored records or application behavior before removing old backups. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiamiaolou-art/skills/c-disk-cleanup) <br>
- [Workflow guide](artifact/references/workflow.md) <br>
- [Troubleshooting guide](artifact/references/troubleshooting.md) <br>
- [Plain-language cleanup glossary](artifact/references/glossary.md) <br>
- [Cleanup habit sample](artifact/references/habit.sample.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with PowerShell command examples and JSON preference data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows-only; requires PowerShell; cleanup actions are intended to be scan-only or confirmation-gated before file movement or Windows maintenance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter version: 1.1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
