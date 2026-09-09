## Description:

Finds designers and creative professionals to recruit using apidojo's Twitter scrapers on Apify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External hiring teams, design agencies, product design leads, and creative directors use this skill to discover, enrich, and score Twitter/X profiles for designer and creative recruiting pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API tokens may be exposed through URLs, command history, logs, or shared transcripts.

Mitigation: Use APIFY_TOKEN from an environment variable or secret manager, avoid putting live tokens in URLs, and redact tokens from logs and transcripts.

Risk: Candidate exports contain personal data from public social profiles.

Mitigation: Minimize exported fields, restrict file access, follow applicable recruiting and privacy requirements, and delete exports when they are no longer needed.

Risk: Automated profile filtering and scoring may misclassify companies, bots, inactive profiles, or candidate availability.

Mitigation: Manually review shortlisted profiles before outreach and treat scores as prioritization signals rather than hiring decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/finding-designers-and-creatives-on-twitter)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Files, Guidance]

**Output Format:** [Markdown candidate lists with tables, plus optional CSV or JSON exports and shell/API command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidate outputs can include social profile identifiers, public bio details, portfolio links, follower counts, activity signals, and fit scores.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
