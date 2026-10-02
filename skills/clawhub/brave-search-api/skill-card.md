## Description:

Helps agents search the web, images, news, and videos through Brave Search using a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to find web pages, images, news, and videos through their authorized Brave Search connection. Optional automation can schedule searches or respond to events after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Functions, triggers, and destinations can persistently send event data or run automated actions.

Mitigation: Confirm the exact target, destination, data flow, and persistence with the user before enabling automation.

Risk: Raw API keys and local event handlers can expose credentials or execute untrusted event data.

Mitigation: Prefer authenticated read-only CLI searches; use raw keys or reviewed event handlers only when necessary and with explicit approval.

## Reference(s):

- [ClawHub Brave Search skill](https://clawhub.ai/byungkyu/skills/brave-search-api)
- [Brave Search API documentation](https://api-dashboard.search.brave.com/documentation)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown search summaries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search availability depends on an authorized Maton connection and Brave Search access.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
