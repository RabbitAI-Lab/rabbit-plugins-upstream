## Description: <br>
Manages project documentation for CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, and DOCS.md update, creation, and initialization workflows, not general markdown editing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to keep agent-facing project documentation aligned with the actual repository state. It verifies files, commands, structure, and conventions before updating context files, README content, CONTRIBUTING guidance, or API-level DOCS.md. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update repository documentation files and a CLAUDE.md symlink. <br>
Mitigation: Use --dry-run on important repositories, review planned changes before committing, and rely on the workflow's backup step before overwriting files. <br>
Risk: Incorrect documentation changes could mislead future agents or contributors. <br>
Mitigation: Review generated AGENTS.md, README.md, CONTRIBUTING.md, and DOCS.md changes against the repository state before accepting them. <br>


## Reference(s): <br>
- [Initialize Context Workflow](references/init-agents.md) <br>
- [Monorepo Handling](references/monorepo.md) <br>
- [Update Context Files Workflow](references/update-agents.md) <br>
- [Update CONTRIBUTING Workflow](references/update-contributing.md) <br>
- [Update README Workflow](references/update-readme.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown files and concise Markdown status summaries with optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update AGENTS.md, create a CLAUDE.md symlink, update README.md, update existing CONTRIBUTING.md or DOCS.md, and supports --dry-run, --preserve, --minimal, and --thorough modifiers.] <br>

## Skill Version(s): <br>
4.3.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
