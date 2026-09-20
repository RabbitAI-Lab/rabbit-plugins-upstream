## Description:

Buildwright applies agent-led software development workflows for planning, implementation, TDD, verification, security review, code review, shipping, repository analysis, and cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raunakkathuria](https://clawhub.ai/user/raunakkathuria)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use Buildwright to guide agent-assisted project work: plan, implement, verify, review, ship changes, analyze repositories, and clean stale project material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: /bw-ship can commit, push, and open a pull request.

Mitigation: Use /bw-ship only when branch changes are ready for publication and review the proposed commit and PR before relying on the result.

Risk: /bw-analyse can create or update .buildwright files in the repository.

Mitigation: Review generated .buildwright files before treating them as authoritative project steering.

Risk: Software-development workflows can modify source, documentation, and configuration files.

Mitigation: Run project verification gates and inspect diffs before merging or deploying generated changes.

## Reference(s):

- [Buildwright homepage](https://github.com/raunakkathuria/buildwright)
- [Buildwright on ClawHub](https://clawhub.ai/raunakkathuria/skills/buildwright)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command names, review findings, shell commands, and repository file updates when a workflow calls for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update project files and documentation during implementation, verification, analysis, cleanup, and shipping workflows.]

## Skill Version(s):

0.0.20 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
