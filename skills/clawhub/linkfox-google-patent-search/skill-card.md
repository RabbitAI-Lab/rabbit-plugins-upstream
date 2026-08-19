## Description:

Searches the public Google Patents database and returns ranked patent results with publication numbers, titles, inventors, assignees, key dates, classifications, patent links, and PDF links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and cross-border sellers use this skill to discover patents by keyword, inventor, assignee, country, date, status, and related Google Patents filters for prior-art review, FTO checks, and patent-infringement risk screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries, session metadata, and saved search results may include confidential research intent or commercially sensitive product information.

Mitigation: Use the skill only when provider data sharing and local saved JSON files are acceptable; avoid submitting confidential patent research unless that handling is approved.

Risk: The onboarding flow can handle phone/SMS login data, API-key creation, and API credentials.

Mitigation: Require explicit user confirmation before login or token-generation steps, and avoid exposing API keys in transcripts, logs, or shared files.

Risk: Searches, pagination, and paid-plan order creation can consume credits or initiate purchase flows.

Mitigation: Disclose credit impact before additional calls or pagination, and require explicit confirmation before any paid-plan order or payment step.

Risk: Automatic feedback reporting can send skill-use context to LinkFox.

Mitigation: Review feedback content before submission when it may contain user-sensitive or business-sensitive details.

## Reference(s):

- [Google Patents Search API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-google-patent-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with patent-result tables, inline shell commands, and saved JSON responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved as local JSON files; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
