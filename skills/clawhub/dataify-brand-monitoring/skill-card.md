## Description:

Monitor a brand across current news, search, reviews, forums, or public social sources and report material mentions, sentiment signals, and reputation risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect current public brand mentions, organize sourced evidence, and summarize reputation risks, channel mix, sentiment signals, and changes over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Dataify account token for collection and task polling.

Mitigation: Configure the token through the local DATAIFY_API_TOKEN environment variable, never paste it into chat or command arguments, and rotate it if exposure is suspected.

Risk: Brand queries, source URLs, and public collection targets are sent to Dataify services.

Mitigation: Use only approved public monitoring targets and avoid submitting sensitive internal strategy, private customer data, or confidential incident details.

Risk: External collection workflows can consume account credits or create broader-than-intended monitoring runs.

Mitigation: Use dry-run, freshness, max-actions, no-wait, and resume controls to bound scope and avoid resubmitting paid tasks after a timeout or interruption.

Risk: Generated command previews or parameters from untrusted input can be misleading if run without review.

Mitigation: Review generated commands and collection parameters before execution, especially when user-provided URLs or shell snippets affect the run.

## Reference(s):

- [Dataify Brand Monitoring on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-brand-monitoring)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with sourced evidence records, plus concise terminal guidance when setup or recovery is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create dated run folders containing state, raw evidence, report.json, and report.md; supports dry-run, bounded action counts, and resume commands.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
