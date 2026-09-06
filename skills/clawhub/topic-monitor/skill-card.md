## Description:

Monitor topics of interest and proactively alert when important developments occur. Use when the user wants automated monitoring of specific subjects like product releases, news topics, technology updates, RSS/Atom feeds, or GitHub releases. Supports scheduled web search plus feed polling, boolean topic filters, AI importance scoring with sentiment tracking, smart alerts vs weekly digests, and memory-aware contextual summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbyczgw-cla](https://clawhub.ai/user/robbyczgw-cla)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to configure recurring monitoring for topics, feeds, GitHub releases, product updates, news, competitors, prices, and research papers, then receive immediate alerts or weekly digests when relevant developments appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured topics, queries, feed URLs, and GitHub repositories may be sent to search providers or feed hosts during monitoring.

Mitigation: Configure only topics and sources you are comfortable sharing with the relevant providers and hosts.

Risk: Imported OPML or feed lists can introduce untrusted external sources into scheduled monitoring.

Mitigation: Review feed and OPML inputs before import, and remove sources that are not trusted for the intended workflow.

Risk: The skill stores findings, alert history, and state locally in the configured data directory.

Mitigation: Set TOPIC_MONITOR_DATA_DIR to a location with access controls appropriate for the monitored content.

Risk: The monitor can invoke a local web-search-plus script through WEB_SEARCH_PLUS_PATH.

Mitigation: Keep WEB_SEARCH_PLUS_PATH pointed at a trusted local script.

## Reference(s):

- [DigitalOcean OpenClaw Skills guide](https://www.digitalocean.com/resources/articles/what-are-openclaw-skills)
- [feedparser project](https://github.com/kurtmckee/feedparser/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON alert, digest, state, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local state and findings files under the configured data directory and emits structured alert lines for agent-delivered channels.]

## Skill Version(s):

1.6.0 (source: frontmatter, CHANGELOG, skill.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
