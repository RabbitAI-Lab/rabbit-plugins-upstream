## Description:

Operate assigned GitLab work with owner-verified project access and guarded merge request delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to manage assigned GitLab issues, repository changes, merge requests, reviews, and CI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated GitLab actions can change projects and merge requests without user checkpoints.

Mitigation: Use an isolated account limited to explicitly approved projects, with approval gates for consequential changes.

Risk: Recurring runs and pipeline management can amplify unintended repository changes.

Mitigation: Keep scheduled runs disabled until a manual run succeeds and enforce CI policy safeguards.

## Reference(s):

- [GitLab Agent release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles)
- [OpenClaw skill creation guidance](https://docs.openclaw.ai/tools/creating-skills)
- [Documentation style reference](artifact/references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also create or update GitLab issues, branches, merge requests, labels, reviewer assignments, and pipelines.]

## Skill Version(s):

1.102.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
