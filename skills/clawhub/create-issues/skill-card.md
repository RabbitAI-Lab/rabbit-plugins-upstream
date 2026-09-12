## Description:

Use when turning approved plans, specs, PRDs, or Epics into trackable GitHub Issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert approved roadmaps, PRDs, SPEC files, and Epics into linked GitHub Issues with traceable parent-child relationships. It helps keep local planning documents and GitHub issue state aligned.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent changes to GitHub Issues, labels, milestones, projects, and local roadmap files.

Mitigation: Before publishing a batch, verify the gh account, target repository, labels, milestones, project destination, and generated issue bodies.

Risk: Using the skill without confirmed GitHub access or repository context can target the wrong repository or leave traceability incomplete.

Mitigation: Run gh auth status and gh repo view first, and stop before publishing when GitHub is unavailable or origin is not the intended repository.

## Reference(s):

- [SPEC SDD Template](references/spec-sdd-template.md)
- [GitHub CLI Manual](https://cli.github.com/manual/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with GitHub CLI command examples and issue body templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local roadmap/spec files and GitHub issue content after user and repository checks.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; source skill metadata lists 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
