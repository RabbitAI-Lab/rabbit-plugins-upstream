## Description:

Scaffolds new projects with git, CI/CD workflows, pre-commit hooks, and build config.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to initialize or modernize Python, Rust, or TypeScript projects with consistent metadata, project tooling, CI workflows, pre-commit hooks, and git setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or overwrite project configuration files.

Mitigation: Review proposed file changes and decline overwrites that should not be applied.

Risk: The workflow may run project setup commands during initialization and verification.

Mitigation: Inspect commands before execution and run them in the intended project workspace.

Risk: The workflow references an external attune plugin script for template rendering.

Mitigation: Verify the external plugin script before executing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-project-init)
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown workflow guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply project files after user review.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
