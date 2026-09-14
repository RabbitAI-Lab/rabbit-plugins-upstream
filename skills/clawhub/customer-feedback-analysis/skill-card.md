## Description:

Analyzes public customer reviews and discussions through Crawlora to identify complaint themes, feature requests, praise, and competitive gaps for voice-of-customer briefs and product-feedback comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, product teams, and developers use this skill to collect bounded public feedback samples and turn them into traceable theme tables, cited examples, sample counts, and follow-up hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, product identifiers, and request parameters are shared with Crawlora as an external provider.

Mitigation: Use public, non-confidential collection briefs and avoid sending private customer records, internal notes, or sensitive product plans.

Risk: The Crawlora API key could be exposed if copied into prompts, command history, logs, or shared files.

Mitigation: Keep CRAWLORA_API_KEY in the environment and use the bundled helper, which avoids placing the key directly on the curl command line.

Risk: Filtered, ranked, or bounded public feedback samples can be mistaken for overall complaint prevalence.

Mitigation: Report n/N with source, product, filters, dates, deduplication rules, and gaps instead of treating the sample as a controlled measurement.

Risk: Review excerpts and author identifiers can expose unnecessary personal or platform-specific user data.

Mitigation: Use brief attributed examples only when needed for provenance and do not export reviewer contact details.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with tables and inline shell command examples; helper calls return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample counts, source and product filters, dates, deduplication notes, gaps, and untested hypotheses.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
