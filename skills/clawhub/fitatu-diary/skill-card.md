## Description:

Helps an agent read and manage a user's Fitatu food diary, including meals, nutrition goals, body measurements, activities, and weekly reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jezue](https://clawhub.ai/user/jezue)

### License/Terms of Use:

MIT-0

## Use Case:

Fitatu users can ask an agent to review their food diary and nutrition goals, log or correct meals and health entries, and summarize their week.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An authenticated local session exposes access to the user's Fitatu account and health-related diary data.

Mitigation: Keep ~/.fitatu/session.json protected; use read-only mode when only viewing the diary and demo mode when testing without an account.

Risk: Requested diary actions can modify or delete health-related entries.

Mitigation: Review the affected entries before changes, and confirm inferred or broader changes with the user.

## Reference(s):

- [Fitatu Diary on ClawHub](https://clawhub.ai/jezue/skills/fitatu-diary)
- [fitatu-api project homepage](https://github.com/Jezue/fitatu_library)
- [fitatu-api agent documentation](https://github.com/Jezue/fitatu_library/blob/main/docs/AGENTS.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diary summaries and suggested or confirmed changes depend on the user's Fitatu account and available data.]

## Skill Version(s):

1.0.0 (source: ClawHub release; skill frontmatter lists 0.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
