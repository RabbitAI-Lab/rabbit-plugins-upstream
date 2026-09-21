## Description:

Analyze public customer reviews and discussions through Crawlora to identify complaint themes, feature requests, praise, and competitive gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, employees, and developers use this skill to collect bounded public feedback samples and turn them into traceable voice-of-customer briefs, product comparisons, complaint themes, feature requests, praise, and competitive gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product names, app IDs, business names, Reddit searches, filters, and research targets are sent to Crawlora under the user's API key.

Mitigation: Use only approved research targets, and avoid confidential project names or sensitive unpublished strategy terms unless the organization has approved Crawlora for that use.

Risk: Filtered or bounded public feedback samples can be mistaken for population-level customer sentiment or complaint prevalence.

Mitigation: Report sample bounds, dates, filters, exclusions, and n/N counts, and describe themes as observations from the collected sample.

Risk: Review excerpts and identifiers can expose more customer information than needed for a feedback brief.

Mitigation: Use brief excerpts, do not export reviewer contact details, and retain author identifiers only when needed for provenance.

## Reference(s):

- [Customer Feedback Analysis endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/customer-feedback-analysis)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown brief with tables, cited examples, sample counts, filters, gaps, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links, dates, deduplication notes, exclusions, and untested hypotheses.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
