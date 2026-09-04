## Description:

Helps agents turn one e-commerce product asset set into localized regional listing copy, size-conversion tables, platform image guidance, and compliance-label prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, e-commerce operators, and localization agents use this skill to adapt product listings for target regions, generate region-specific image prompts, and run platform image checks before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product prompts and reference images may be uploaded to selected cloud AI providers during generated-image workflows.

Mitigation: Choose the provider deliberately, avoid confidential unreleased assets unless approved, and use dry-run or doctor modes to inspect what will be called before execution.

Risk: Generated localized text or compliance-label suggestions may be inaccurate or incomplete.

Mitigation: Have humans review generated text, regional claims, and compliance labels before publishing marketplace listings.

Risk: Provider routing can vary with command flags and environment variables.

Mitigation: Keep commands scoped to --task cross-border-localize and confirm provider credentials and routing before running generation commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specs](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with bash examples and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image files when generated commands are executed through a selected cloud image provider.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
