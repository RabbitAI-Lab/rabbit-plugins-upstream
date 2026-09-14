## Description:

Use when turning approved plans, specs, PRDs, or Epics into trackable GitHub Issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to convert approved roadmaps, specs, PRDs, and epics into linked GitHub Issues with traceable parent and child work items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitHub Issues or project records may be created in the wrong account or repository if GitHub CLI authentication or the remote origin is incorrect.

Mitigation: Confirm gh authentication and repository targeting with gh auth status and gh repo view before publishing changes.

Risk: Batch issue creation or project updates can affect public or business-critical work tracking data.

Mitigation: Review proposed issue batches, labels, milestones, and project changes before executing mutations.

Risk: Generated issues can diverge from approved planning documents if the roadmap or spec is missing or ambiguous.

Mitigation: Use approved source documents as the source of truth and stop rather than inventing epics or requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/afonsoft/skills/create-issues)
- [Skill Metadata URL](https://github.com/afonsoft/skills)
- [GitHub CLI Manual](https://cli.github.com/manual/)
- [SPEC SDD Template](references/spec-sdd-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with GitHub CLI commands and issue body templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update GitHub Issues, labels, milestones, projects, and roadmap links when GitHub access is confirmed.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact metadata.version is 1.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
