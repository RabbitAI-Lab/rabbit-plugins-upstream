## Description: <br>
Spec-driven development with OpenSpec CLI for building features, migrations, refactors, or other structured development work by managing proposal, specs, design, tasks, and implementation workflows with custom schemas such as TDD and rapid. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcorrego](https://clawhub.ai/user/jcorrego) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering agents use this skill to manage structured development work with OpenSpec, including feature planning, migrations, refactors, requirement specs, design notes, tasks, validation, and archiving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on the external OpenSpec npm package and may generate or update local project files. <br>
Mitigation: Install only if the package is trusted, consider pinning a CLI version, use version control, and review generated openspec/ and .claude/skills/ files before relying on them. <br>
Risk: Implementation and archive steps can lead an agent to make project edits or merge OpenSpec change artifacts into main specs. <br>
Mitigation: Review proposals, specs, design notes, and tasks before accepting implementation edits, and confirm before running archive commands. <br>


## Reference(s): <br>
- [Schema Reference](references/schemas.md) <br>
- [OpenSpec ClawHub Skill Page](https://clawhub.ai/jcorrego/skills/openspec) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and OpenSpec artifact guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides creation and review of OpenSpec project files such as proposals, specs, design documents, tasks, schemas, and configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
