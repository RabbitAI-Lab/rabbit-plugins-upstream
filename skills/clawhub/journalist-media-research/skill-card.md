## Description:

Build a relevant journalist and media shortlist for a story or PR brief using Crawlora's journalists dataset, news search, and public author pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and communications teams use this skill to research reporters whose recent coverage fits a story or PR brief, then produce a sourced media shortlist with public contact channels and verification status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Journalist research queries, requested public scrape URLs, and the Crawlora API key are sent to Crawlora's API.

Mitigation: Keep the API key in the environment, use the bundled helper's documented endpoints, and avoid private or sensitive URLs in scrape requests.

Risk: Public contact details may be mistaken for consent to receive outreach.

Mitigation: Treat contact details as leads, preserve verification status, and do not send pitches unless the user explicitly requests that separate action.

Risk: The curated journalist dataset and best-effort beat labels may be incomplete or stale.

Mitigation: Verify current affiliation and recent bylined work on source pages, label bio-only matches as unverified, and explain any shortlist shortfall.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/journalist-media-research)
- [Crawlora](https://crawlora.net)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown table or CSV with supporting URLs and verification status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected fields include name, outlet, title, beat, profile_url, relevant_article_urls, article_dates, fit_reason, public_contact, contact_source_url, retrieved_at, and verification_status.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
