## Description:

Finds law firms and legal practices through Google Search using apidojo's Google Search Scraper on Apify, returning candidate firm names, website URLs, and result snippets for prospecting workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and business development teams use this skill to discover law firms by location and practice area, then rank and classify results for outreach list building. It is also useful for agents helping LegalTech vendors or B2B service providers assemble initial prospect research from Google results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to Apify and require use of an APIFY_TOKEN for the external service.

Mitigation: Use only search terms appropriate for the Apify service and manage the APIFY_TOKEN as a credential.

Risk: Saved CSV or JSON outputs may contain prospecting data that should not be shared without review.

Mitigation: Review generated files before sharing them, especially for sales outreach workflows.

Risk: Search result snippets may omit phone numbers, email addresses, or other contact details.

Mitigation: Treat results as a starting list and verify firm details before using them for outreach.

Risk: Legal directories or duplicate domains can appear in Google results and reduce lead quality.

Mitigation: Filter known directory domains and deduplicate results by domain before ranking prospects.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/apidojo-io/skills/finding-law-firms-via-google-search)
- [Apify Google Search Scraper run endpoint](https://api.apify.com/v2/acts/apidojo~google-search-scraper/runs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON, shell command examples, and structured prospect ranking labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save search results as CSV or JSON when the Apify runner is used with an output path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
