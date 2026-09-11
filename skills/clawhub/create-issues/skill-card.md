## Description:

Create Issues turns plans, specs, PRDs, and Epics into trackable GitHub Issues with stable Epic IDs, direct links, vertical slices, dependencies, and verifiable acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert roadmaps, PRDs, and SPEC files into linked GitHub Epic and slice issues while keeping local planning documents synchronized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish and edit GitHub tracking data using authenticated gh credentials.

Mitigation: Use it only in intended repositories and review proposed issue batches before publishing them.

Risk: Roadmap or spec tracking can become inconsistent if Epic IDs, issue links, dependencies, or states are wrong.

Mitigation: Run the skill's mandatory validation checks before declaring Epics and slices tracked.

## Reference(s):

- [Create Issues on ClawHub](https://clawhub.ai/afonsoft/skills/create-issues)
- [Repository listed in skill metadata](https://github.com/afonsoft/skills)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [SPEC SDD Template](references/spec-sdd-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with GitHub CLI commands and issue-body templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitHub issues and local roadmap/spec links when run with authenticated gh access.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
