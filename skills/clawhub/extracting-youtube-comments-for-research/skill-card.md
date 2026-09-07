## Description:

Extracts and analyzes YouTube comments for audience research using apidojo's YouTube scraper on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

Apache-2.0

## Use Case:

External researchers, content creators, brand researchers, product teams, and audience insight analysts use this skill to collect YouTube comments and turn them into sentiment summaries, common questions, themes, and high-signal examples.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected public YouTube targets and scrape job details to Apify.

Mitigation: Use the skill only when that third-party data flow is acceptable for the research task.

Risk: APIFY_TOKEN can be exposed through shared logs, shell history, or token-bearing URLs.

Mitigation: Keep APIFY_TOKEN in environment or managed tooling, and avoid pasting token-bearing curl URLs into shared places.

Risk: Large comment collection jobs can consume more time or service quota than intended.

Mitigation: Set explicit maximum limits such as maxComments or maxItems before running broad research jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/extracting-youtube-comments-for-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional shell commands and JSON or CSV file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes comment text, likes, reply count, usernames, timestamps, filtered themes, sentiment summaries, top comments, and frequently asked questions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
