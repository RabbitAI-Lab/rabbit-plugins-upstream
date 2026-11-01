## Description:

Turns a maintained company watchlist into an incremental daily digest of new disclosures, recent changes, and items needing human review, with official sources and as-of timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

People maintaining a company watchlist use it to create a source-linked daily digest of new disclosures and selected recent changes. It leaves interpretation to a human and is not for market prices, forecasts, ratings, or one-time historical reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional authenticated connection checks may expose the API key to an unapproved server; online company lookups also disclose watchlist interests to the provider.

Mitigation: Use the documented local-data workflow without an API key until authenticated examples enforce approved HTTPS destinations and redirect protections. Consider the disclosure to the lookup provider before sending company interests online.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-watchlist-digest-cn)

## Skill Output:

**Output Type(s):** [Markdown, JSON, JSONL]

**Output Format:** [A five-section Markdown daily digest with JSON run and snapshot records and a JSONL source index.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries include official source links and as-of times; same-day reruns reuse that day's recorded increment. Items requiring judgment are reserved for human review.]

## Skill Version(s):

0.2.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
