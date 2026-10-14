## Description:

Prepares a Slack briefing for each booked external meeting, with attendees, relevant deal and activity context, a recent public event, and a tailored opener, then threads material changes and cancellations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams use this skill to receive timely, account-specific meeting briefs in an internal Slack channel and follow meeting changes in the same thread.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad calendar access can expose meetings beyond the sales team.

Mitigation: Obtain Workspace and sales-ops approval; prefer individual OAuth or a selected sales-team scope over domain-wide access.

Risk: Meeting briefs can disclose deal amounts and past activity quotes in Slack.

Mitigation: Post only to a private internal channel approved for sensitive sales information and keep the destination fixed.

Risk: Calendar content may contain instructions intended to redirect the agent.

Mitigation: Treat all calendar-derived fields as untrusted data and review prompt and policy protections before deployment.

## Reference(s):

- [Meeting card format](references/card.md)
- [Project homepage (release metadata)](https://github.com/getcargohq/gtm-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Slack-formatted meeting briefs and threaded updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One briefing per external meeting; material changes and cancellations appear as thread replies.]

## Skill Version(s):

0.2.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
