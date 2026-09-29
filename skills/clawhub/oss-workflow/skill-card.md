## Description:

Routes GitHub collaboration tasks through scenario-specific checklists and supporting skills, tracking evidence before delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qikairo7](https://clawhub.ai/user/qikairo7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and open-source contributors use this skill to organize repository review, pull requests, documentation changes, fork maintenance, and new repository setup with auditable checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad shell hook may block or allow GitHub commands unexpectedly.

Mitigation: Review the guard setup and test its behavior before enabling profile-level hooks.

Risk: Guard checks do not fully authorize merges, closes, edits, comments, or issue operations.

Mitigation: Require independent review and explicit authorization before GitHub write operations.

## Reference(s):

- [ClawHub oss-workflow release](https://clawhub.ai/qikairo7/skills/oss-workflow)
- [Repository review checklist](references/checklists/s1.md)
- [Pull request and bug-fix checklist](references/checklists/s2.md)
- [Documentation checklist](references/checklists/s3.md)
- [Ongoing collaboration checklist](references/checklists/s4.md)
- [New repository checklist](references/checklists/s5.md)
- [Guard limitations](references/guard/LIMITATIONS.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown checklist and task guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local task checklist with step-by-step evidence pointers.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
