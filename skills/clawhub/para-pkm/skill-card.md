## Description: <br>
Manage PARA-based personal knowledge management (PKM) systems using Projects, Areas, Resources, and Archives organization method. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to create, organize, validate, and maintain PARA-based personal knowledge bases. It helps agents decide where notes belong, generate compact AI navigation files, archive completed projects, and apply PARA patterns for roles such as developers, consultants, researchers, and product builders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: File-changing scripts are not tightly scoped and can overwrite or delete local files if given unsafe paths. <br>
Mitigation: Review before installing, use the skill only on a backed-up knowledge base, run scripts from the intended knowledge-base root, avoid absolute paths or ../ traversal, and check archive and output paths carefully. <br>
Risk: Archiving and navigation-generation behavior can make local knowledge-base changes that are difficult to undo without backups. <br>
Mitigation: Back up the knowledge base before running file-changing scripts and review generated or archived paths before relying on the result. <br>


## Reference(s): <br>
- [PARA Method Principles](references/para-principles.md) <br>
- [PARA Decision Guide](references/decision-guide.md) <br>
- [Common PARA Patterns](references/common-patterns.md) <br>
- [AI Navigation Best Practices](references/ai-navigation.md) <br>
- [PARA method source](https://fortelabs.com/blog/para/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated or modified local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, update, archive, validate, or summarize local PARA knowledge-base files.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
