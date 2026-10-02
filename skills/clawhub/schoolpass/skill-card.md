## Description:

Helps parents check SchoolPass student schedules, pickup arrangements, and dismissal changes through their parent account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents use this skill to review their children's arrival and dismissal schedules, pickup drivers, and pending changes, and to approve changes to a child's dismissal when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SchoolPass parent credentials or private student information could be exposed.

Mitigation: Keep account configuration private, avoid sharing logs with credentials, and limit disclosure of student and pickup details.

Risk: An incorrect dismissal change could affect a child's pickup or arrival.

Mitigation: Review the child, date, and change in every preview and obtain explicit approval before submitting; if submission status is uncertain, check the calendar instead of retrying.

## Reference(s):

- [schoolpass on ClawHub](https://clawhub.ai/chrischall/skills/schoolpass)
- [schoolpass-mcp on npm](https://www.npmjs.com/package/schoolpass-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown summaries of SchoolPass account information and change previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dismissal changes require explicit confirmation; responses may contain sensitive student and family information.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
