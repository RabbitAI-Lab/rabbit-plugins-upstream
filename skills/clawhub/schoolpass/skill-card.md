## Description:

Helps parents review their children's SchoolPass arrival and dismissal information and manage pickup changes through their own account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use this skill to check student calendars, pickup arrangements, authorized drivers, and school information, and to request or cancel dismissal changes with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Parent credentials stored in configuration can be exposed to collaborators or committed to a repository.

Mitigation: Use private user-level configuration and keep credentials out of shared files and version control.

Risk: The unpinned npm server can access sensitive child dismissal records and change tools.

Mitigation: Review the package and pin a trusted version before granting access to the parent account.

Risk: An incorrect or repeated dismissal update could affect a child's real pickup arrangements.

Mitigation: Avoid auto-confirm, review the preview with the parent before approval, and check the calendar rather than resubmitting if the result is uncertain.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown with account summaries, change previews, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive student and dismissal details; dismissal changes require explicit confirmation.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
