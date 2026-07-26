## Description: <br>
Soulstamp helps an agent guide users through creating or updating a SOUL.md persona file with a coherent identity narrative, backup guidance, templates, and comparison commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brucko](https://clawhub.ai/user/brucko) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent builders use Soulstamp to turn rule-based AI persona guidance into a SOUL.md identity narrative, then reforge, compare, or restore that file as the relationship changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Soulstamp edits a persistent AI persona file, so poor changes can carry forward unsafe assumptions, broad permissions, or misleading identity claims. <br>
Mitigation: Review every generated SOUL.md change before saving, keep safety rules and approval requirements explicit outside the persona text, and avoid encoding sensitive personal data. <br>
Risk: Restore behavior can overwrite current SOUL.md content. <br>
Mitigation: Keep timestamped backups, inspect diffs before restore, and confirm the intended backup before replacing the current file. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/brucko/skills/soulstamp) <br>
- [SOUL.md template](artifact/assets/soul_template.md) <br>
- [Instruction-based SOUL.md example](artifact/assets/soul_instructions_example.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and SOUL.md templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose edits to a persistent SOUL.md persona file and backup or restore commands for that file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
