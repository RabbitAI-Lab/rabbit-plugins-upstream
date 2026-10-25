## Description:

Scans a collection of skill folders and generates a JSON registry and Markdown overview of their metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill collection maintainers use this skill to inventory skill folders and track names, versions, licenses, categories, and risk labels in a JSON registry and Markdown table.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registry output may overwrite existing files at the selected paths.

Mitigation: Choose dedicated output paths or back up existing registry files before running.

Risk: The declared permissions omit the filesystem access needed to scan skills and write the registry.

Mitigation: Run only against skill folders you intend to inventory, limit access to those folders and chosen output paths, and correct the permissions declaration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/skill-registry)

## Skill Output:

**Output Type(s):** [JSON, Markdown]

**Output Format:** [JSON registry file and Markdown overview table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the generation date, skill count, and available skill metadata; output file paths are configurable.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
