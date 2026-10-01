## Description:

Maintains durable project decisions, findings, and rules in Git-native Open Knowledge Format bundles with traceable sources and trust tiers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineering teams use this skill to capture durable project knowledge, retrieve relevant decisions, and keep repository knowledge current and traceable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository knowledge edits or optional instruction and commit-hook changes may conflict with project policies.

Mitigation: Review proposed documentation, agent instructions, and validation hooks against repository policies before committing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/tenequm/skills/okf-project-knowledge-base)
- [Skill homepage (listed in metadata)](https://github.com/tenequm/skills/tree/main/skills/okf-project-knowledge-base)
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format)

## Skill Output:

**Output Type(s):** [Markdown, Text, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown concepts with YAML frontmatter, indexes, and optional repository guidance or validation scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Git-native files with sources and optional verification metadata]

## Skill Version(s):

0.3.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
