## Description:

Read your organization's Workvivo (Zoom Workvivo employee-experience platform, <org>.workvivo.us/.com/.io) from a shell — the home feed, company news articles, posts and shoutouts with their comments, spaces and their feeds/news/events/content pages, linked documents, upcoming events, the people directory and profiles, your team, notifications, and full-text federated search — through your signed-in Workvivo browser tab with the fpx CLI. Read-only. Use when asked about Workvivo, the company intranet feed, internal news, a Workvivo space, colleagues' profiles, or what's happening at work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to find and read their organization's Workvivo feeds, news, spaces, events, documents, and people directory through their signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad workplace requests may activate searches across internal Workvivo content.

Mitigation: Keep activation scoped to explicit Workvivo requests and clarify the requested content when a query is broad.

Risk: Workvivo records may include sensitive employee or organization fields, including tokens, phone numbers, and webinar passwords.

Mitigation: Use the documented named-field projections and omit tokens, phone numbers, webinar passwords, and unrelated personal details.

Risk: Federated search adds the query to the user's Workvivo search history.

Mitigation: Use federated search only when that history entry is appropriate; use read endpoints when search is not needed.

Risk: The scan could not establish the effective permissions available in the host runtime.

Mitigation: Check which tools the host runtime permits before installing or invoking the skill.

## Reference(s):

- [Workvivo Read Endpoints](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON data and concise textual information from Workvivo]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries except federated search, which adds an entry to the user's Workvivo search history.]

## Skill Version(s):

0.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
