## Description: <br>
Build composable skill modules with hub-and-spoke loading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to design, refactor, and maintain modular agent skills that keep token usage predictable through hub-and-spoke modules and progressive disclosure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad skill-design triggers may activate the skill during general architecture or modularity discussions. <br>
Mitigation: Confirm the task is about modular skill design before applying the guidance. <br>
Risk: Example shell snippets may change local files if copied without review. <br>
Mitigation: Review commands and local scripts before execution, and scope file permission changes to specific intended files. <br>
Risk: Structural recommendations could introduce incorrect or misleading skill content if accepted without validation. <br>
Mitigation: Review generated module structures and run the relevant skill validators before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/athola/skills/nm-abstract-modular-skills) <br>
- [Clawdis Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>
- [Core Workflow Module](artifact/modules/core-workflow.md) <br>
- [Implementation Patterns Module](artifact/modules/implementation-patterns.md) <br>
- [Troubleshooting Module](artifact/modules/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-oriented output; review command examples before execution.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
