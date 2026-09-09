## Description:

Finds Google coverage of industry events and conferences using apidojo's Google Search scraper, then helps classify and score results by coverage type, quality, and relevance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Industry analysts, competitive intelligence teams, PR professionals, and event marketers use this skill to find press coverage, recaps, announcements, speaker quotes, and session summaries for trade shows, conferences, and summits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event names, search terms, and resulting search data are sent to Apify.

Mitigation: Use the skill only when that data can be shared with Apify and avoid submitting confidential event intelligence or sensitive search terms.

Risk: API tokens can be exposed through shell history, shared logs, or copied command output.

Mitigation: Store APIFY_TOKEN in the environment or a local .env file and redact tokens from logs, command transcripts, and shared artifacts.

Risk: Saved CSV or JSON result files may contain third-party search results or sensitive analysis.

Mitigation: Review and sanitize saved outputs before distributing them outside the intended team.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/apidojo-io/skills/finding-industry-event-coverage-google)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs a structured article list with title, publication, date, coverage type, score, and summary insights.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
