## Description:

Company enrichment API - turn a business website or a Google Maps place_id into contact data as structured JSON - the company's published emails, phone numbers, social profiles (Facebook, Instagram, LinkedIn, X, TikTok, YouTube, Pinterest) and contact page, plus the owner or founder's name and title with the page that names them. Built for the step after a Google Maps search - enrich every local result into a lead. 1 endpoint, 10 credits from a website, 20 from a place_id; an unreachable site is free.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, marketing, and operations agents can use the skill to enrich a business website or Google Maps place ID with published contact details and social profiles. It can also identify an owner or founder when a visited page names them, with the source page included.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business URLs, place IDs, and Google Maps search queries are sent to Scavio; Maps search is an additional capability beyond enriching supplied targets.

Mitigation: Review Scavio's data practices and make sure you are comfortable sharing the targets and queries before using the skill.

Risk: Security review coverage is partial because some local references could not be resolved, leaving the evidence incomplete.

Mitigation: Review the linked API documentation and skill behavior before installation, especially if handling sensitive business data.

## Reference(s):

- [Scavio Company Enrich API documentation](https://scavio.dev/docs/company-enrich?utm_source=agent-skills&utm_medium=skill&utm_campaign=company-enrichment-api)
- [Company Enrich API endpoint](https://api.scavio.dev/api/v1/company/enrich)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [Structured JSON containing company contact details, any sourced owner information, and pages read; the agent can present these as a concise text summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only information returned by the API is reported; owner details may be null when no page names an owner.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
