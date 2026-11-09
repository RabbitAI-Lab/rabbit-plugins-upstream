## Description:

Read your organization's Workvivo (Zoom Workvivo employee-experience platform, <org>.workvivo.us/.com/.io) from a shell — the home feed, company news articles, posts and shoutouts with their comments, spaces and their feeds/news/events/content pages, linked documents, upcoming events, the people directory and profiles, your team, notifications, and full-text federated search — through your signed-in Workvivo browser tab with the fpx CLI. Read-only. Use when asked about Workvivo, the company intranet feed, internal news, a Workvivo space, colleagues' profiles, or what's happening at work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use the skill to retrieve and summarize information they are authorized to see in their organization's Workvivo, including internal news, posts, spaces, events, profiles, notifications, and search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses network access through a signed-in Workvivo browser session, and a broad activation phrase could invoke access to that account.

Mitigation: Use it for explicit Workvivo or company-intranet requests, and confirm the intended organization before querying the signed-in session.

Risk: Workvivo responses can contain sensitive account, employee, or event fields that are not needed for a user-facing answer.

Mitigation: Project only the requested fields using the documented jq recipes; do not print or relay raw responses.

## Reference(s):

- [Workvivo endpoint reference](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/workvivo-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown summaries and selected JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented results; Workvivo federated search also adds an entry to the user's own search history.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
