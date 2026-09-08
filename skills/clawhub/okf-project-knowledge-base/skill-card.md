## Description:

Maintains durable project knowledge as Git-native OKF v0.2 bundles with one Markdown concept per file, YAML frontmatter, provenance sources, trust tiers, and a progressive-disclosure index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, recall, and maintain durable project knowledge in a repository using OKF bundles, so decisions, findings, and rules survive context resets without becoming session state or operating instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill intentionally writes durable project knowledge into the repository and may add a pointer line to an instruction file.

Mitigation: Use it only in repositories where project knowledge should be committed and shared, and review entries to exclude secrets, personal data, private host details, and unrelated session state.

Risk: Incorrect or stale knowledge could mislead future agents or humans after it becomes part of the repository record.

Mitigation: Require traceable sources, status and staleness fields where useful, index and log updates in the same change, and verification of frontmatter, links, and format before claiming conformance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/okf-project-knowledge-base)
- [Project Homepage](https://github.com/tenequm/skills/tree/main/skills/okf-project-knowledge-base)
- [Open Knowledge Format](https://github.com/GoogleCloudPlatform/open-knowledge-format)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown concepts with YAML frontmatter, index and log updates, and concise implementation guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update repository documentation files and add one instruction-file pointer line when appropriate.]

## Skill Version(s):

0.1.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
