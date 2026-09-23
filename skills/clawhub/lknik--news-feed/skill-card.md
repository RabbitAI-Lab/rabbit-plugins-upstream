## Description:

Fetch latest news headlines from major RSS feeds (BBC, Reuters, AP, Al Jazeera, NPR, The Guardian, DW). No API keys required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lknik](https://clawhub.ai/user/lknik)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to fetch current headlines, daily news briefings, and topic-specific RSS digests from major international news sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled permission settings allow broader local commands than needed for fetching RSS headlines.

Mitigation: Review the packaged permissions before installation, narrow execution to the RSS reader command, and keep normal approval for arbitrary Python, git changes, directory enumeration, and unrelated web searches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lknik/skills/news-feed)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown grouped by news source with headlines, summaries, publication times, and links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports source, topic, item limit, and source-listing options.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
