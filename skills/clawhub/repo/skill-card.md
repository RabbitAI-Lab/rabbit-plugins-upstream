## Description:

Project initialization toolkit that analyzes project structure and settings to generate a project-specific CONTRIBUTING.md guide.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect repository configuration, project layout, package metadata, style settings, and hooks, then draft a CONTRIBUTING.md guide that reflects the detected project conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases such as init or contributing guide may activate the skill unexpectedly.

Mitigation: Review the agent's proposed action before allowing it to analyze or write repository files.

Risk: Generated CONTRIBUTING.md content may not match the repository owner's preferred language, workflow, or project policy.

Mitigation: Review the generated guide before accepting it, with attention to language choice, commands, hooks, and overwrite prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/repo)
- [Contributing generator guide](artifact/contributing.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with project-specific guidance and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose writing CONTRIBUTING.md after analyzing repository configuration; existing files should be reviewed before overwrite.]

## Skill Version(s):

0.3.1 (source: server release metadata, created 2026-08-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
