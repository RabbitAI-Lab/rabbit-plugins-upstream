## Description:

Use when turning plans, specs, PRDs, and Epics into trackable GitHub Issues. Creates stable Epic IDs, direct links, vertical slices, dependencies, and verifiable acceptance criteria using the GitHub CLI (gh). Part of the afonsoft/skills collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project maintainers use this skill to convert roadmaps, PRDs, specs, and Epics into linked GitHub Issues with stable Epic IDs, dependencies, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to use an authenticated GitHub CLI session to create or update issue-tracking metadata.

Mitigation: Install only for repositories where that GitHub access is appropriate, and review proposed issue batches before publishing when scope, dependency order, or architecture is uncertain.

## Reference(s):

- [GitHub CLI manual](https://cli.github.com/manual/)
- [afonsoft skills source collection](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash code blocks and GitHub issue templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitHub Issues when the agent runs authenticated gh commands after user review.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
