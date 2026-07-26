## Description: <br>
Creates named local project snapshots for rollback, with explicit backup, list, and restore workflows for development projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincsta](https://clawhub.ai/user/vincsta) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, list, and restore local project snapshots before risky changes or refactoring. Restore is destructive and should be preceded by a dry run and explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the fallback backup path can include files the skill promises to exclude, such as environment files or other sensitive project contents. <br>
Mitigation: Review before installing, use only on non-sensitive projects unless rsync is present, and verify backup contents do not contain secrets. <br>
Risk: Restore operations overwrite files in the target project and can permanently lose unsaved or newer local changes. <br>
Mitigation: Run the documented dry run first, require explicit user confirmation, and keep an independent copy of important work before restore. <br>
Risk: Retention deletes older snapshots without additional confirmation. <br>
Mitigation: Choose an appropriate --keep value and verify which snapshots remain before relying on this as the only recovery mechanism. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vincsta/skills/dev-backup) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with bash commands and local snapshot directories] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates numbered project snapshot folders and a .latest symlink when the shell script is executed.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
