## Description:

Search public LinkedIn, X, and Reddit posts for brand monitoring, competitor monitoring, public-conversation research, and weekly marketing briefs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shash7](https://clawhub.ai/user/shash7)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, research, and competitive intelligence users use this skill to search public social posts, collect sourced mentions, and prepare concise human-reviewed briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends chosen search queries to SocialListeningAPI and may spend API credits.

Mitigation: Confirm the user is comfortable with the selected query, platforms, and credit use before running the search.

Risk: Public-search results can be irrelevant, incomplete, or unsuitable for direct business decisions.

Mitigation: Treat returned posts as research leads, review errors and source URLs, and require human review before action.

## Reference(s):

- [Monitoring workflows](references/monitoring-workflows.md)
- [Server-resolved GitHub provenance](https://github.com/shash7/sociallisteningapi-examples/tree/master/openclaw/social-listening-monitor)
- [ClawHub skill page](https://clawhub.ai/shash7/skills/social-listening-monitor)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Normalized JSON from the search script, plus concise Markdown summaries with cited public source URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are sorted newest first and include query, searched platforms, items, errors, creditsUsed, and sourceUrls.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
