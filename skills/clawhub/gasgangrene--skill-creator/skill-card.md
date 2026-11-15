## Description:

Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gasgangrene](https://clawhub.ai/user/gasgangrene)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and agent authors use this skill to design, scaffold, validate, package, and iterate on agent skills with clear frontmatter, resource structure, and output guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled scripts can create local skill folders and package archives, and server security evidence notes filesystem containment gaps.

Mitigation: Run the scripts only against trusted paths, avoid packaging untrusted skill trees or trees containing symlinks, and review generated archive contents before sharing.

Risk: Skill-authoring guidance can introduce incorrect or misleading instructions into generated skills.

Mitigation: Review generated SKILL.md content and run validation before installing, publishing, or sharing a packaged skill.

## Reference(s):

- [Workflow Patterns](references/workflows.md)
- [Output Patterns](references/output-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated local skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create skill folders, validate skill metadata, and package .skill archives when its bundled scripts are run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
