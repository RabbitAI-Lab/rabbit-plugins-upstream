## Description:

Initialize a brand-new monorepo project in an empty or near-empty folder after a structured requirements interview, then generate and verify a production-grade scaffold for the chosen stack.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to design and create a new monorepo with explicit choices for apps, packages, tooling, CI, release strategy, environment handling, documentation, and verification commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates real project files and can run package-manager verification commands.

Mitigation: Use an empty or dedicated folder when possible, and review the proposed scaffold plan before approving writes.

Risk: Scaffolding into a non-empty directory can merge with or conflict with existing files.

Mitigation: Confirm directory contents first and choose whether to proceed, use a subfolder, or abort before any files are written.

Risk: Git initialization in an existing repository can create confusing repository state.

Mitigation: Check whether the target is already inside a git repository and require explicit confirmation before initializing git.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anjasta-tarigan/skills/monorepo-scaffold)
- [Interview Guide](references/interview-guide.md)
- [Stack Recipes](references/stack-recipes.md)
- [Config Templates](references/config-templates.md)
- [Turbo schema](https://turbo.build/schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration]

**Output Format:** [Markdown status reports plus generated project files, configuration files, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces scaffold files in the target workspace and may run package-manager, build, lint, test, workspace-inspection, and optional git commands after user confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
