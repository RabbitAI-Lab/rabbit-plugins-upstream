## Description: <br>
Manages project documentation: CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, DOCS.md. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this workflow skill to create or maintain project documentation and agent context files from the current repository state. It focuses on AGENTS.md, CLAUDE.md, README.md, CONTRIBUTING.md, and DOCS.md rather than general markdown editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation or context-file edits could introduce stale, incorrect, or misleading instructions for future agents and developers. <br>
Mitigation: Use the skill's verification workflow to check paths, commands, and repository structure against the current codebase before accepting changes. <br>
Risk: Existing AGENTS.md or CLAUDE.md files may be changed, renamed, or linked during context initialization workflows. <br>
Mitigation: Use --dry-run or review planned changes before writing, and confirm before migrating CLAUDE.md to AGENTS.md. <br>
Risk: README or CONTRIBUTING updates could overwrite intentional project-specific prose or governance policy. <br>
Mitigation: Use preserve behavior where appropriate, update CONTRIBUTING.md with targeted replacements, and keep maintainer policy sections intact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-md-docs) <br>
- [Initialize Context Workflow](references/init-agents.md) <br>
- [Monorepo Handling](references/monorepo.md) <br>
- [Update Context Files Workflow](references/update-agents.md) <br>
- [Update CONTRIBUTING Workflow](references/update-contributing.md) <br>
- [Update README Workflow](references/update-readme.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown documentation updates, concise reports, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update AGENTS.md, CLAUDE.md symlinks, README.md, CONTRIBUTING.md, and DOCS.md according to the selected workflow.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
