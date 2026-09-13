## Description:

Guides agents to create, read, and maintain durable project knowledge as Git-native Open Knowledge Format bundles with one concept per file, provenance, and trust tiers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to capture decisions, findings, and standing project rules as repository-backed OKF concepts that outlive a single session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead agents to make persistent repository instruction changes that affect future agent behavior.

Mitigation: Review the exact instruction-file line before allowing the change, and confirm future agents should automatically load this skill or perform capture reviews.

Risk: The skill may propose repository automation such as a pre-commit hook or index generator.

Mitigation: Review automation changes as code before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/okf-project-knowledge-base)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/okf-project-knowledge-base)
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown guidance with YAML frontmatter examples and repository file change proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose persistent repository instruction changes and knowledge-index automation.]

## Skill Version(s):

0.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
